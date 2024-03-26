from config import app, db, api
from models import Combat, Status, Character, Player, KnownTech, Technique, Enemy
from sqlalchemy import and_

def begin_combat():
    combat = Combat.query.first()
    setattr(combat, 'turn', 1)
    if combat.player.spd >= combat.enemy.spd:
        setattr(combat.player, "order", 1)
        setattr(combat.enemy, "order", 2)
        setattr(combat, "player_next", True)
    elif combat.enemy.spd > combat.player.spd:
        setattr(combat.enemy, "order", 1)
        setattr(combat.player, "order", 2)
        setattr(combat, "player_next", False)
    db.session.commit()
    updated_combat = Combat.query.first()
    return updated_combat
    # if combat.player.order == 1:
    #     get_player_action(combat)
    # elif combat.enemy.order == 1:
    #     get_enemy_action(combat)

def end_combat(victor, combat):
    #delete all statuses
    for status in combat.statuses:
        remove_status(status)
    #reset hp (later handle gameover)
    setattr(combat.player, 'crnt_hp', combat.player.max_hp)
    setattr(combat.enemy, 'crnt_hp', combat.enemy.max_hp)
    setattr(combat, 'victor', victor)
    
    ##Player Rewards##
    if victor == 'player':
        ###Gain AP###
        new_points = combat.player.adv_points + combat.enemy.threat_rating
        setattr(combat.player, 'adv_points', new_points)
        db.session.commit()
        print(combat.player)
        print(combat.player.adv_points)
        ###Unlock Monster's Techs###
        monsters_known_techs = combat.enemy.known_techs
        for known_tech in monsters_known_techs:
            setattr(known_tech.tech, 'unlocked', True)
            db.session.commit()

    db.session.commit()

def advance_turn(combat, crnt_combatant):
    #check hps
    if combat.player.crnt_hp <= 0:
        end_combat(combat.enemy.name, combat)
        return
        
    elif combat.enemy.crnt_hp <= 0:
        end_combat("player", combat)
        return
        

    if combat.turn == 1:
        setattr(combat, 'turn', 2)
    elif combat.turn == 2:
        advance_rnd(combat)
    db.session.commit()
        

        
def advance_rnd(combat):
    setattr(combat, 'turn', 1)
    setattr(combat, 'rnd', combat.rnd+1)
    for status in combat.statuses:
        setattr(status, 'remaining_duration', status.remaining_duration-1)
        if status.remaining_duration <= 0:
            remove_status(status)

    if combat.player.order == 1:
        #get_player_action(combat)
        setattr(combat, 'player_next', True)
    elif combat.enemy.order == 1:
        #get_enemy_action(combat)
        setattr(combat, 'player_next', False)
    db.session.commit()

def get_player_action(tech_id):
    combat = Combat.query.first()
    setattr(combat, 'player_next', False)
    db.session.commit()
    take_action(combat.player, tech_id, combat)
    updated_combat = Combat.query.first()
    return updated_combat

def get_enemy_action():
    combat = Combat.query.first()
    setattr(combat, 'player_next', True)
    db.session.commit()
    action_number = combat.rnd % len(combat.enemy.actions)
    action_slot = combat.enemy.actions[action_number-1]
    int_slot = int(action_slot)
    known_tech = KnownTech.query.filter(and_(KnownTech.slot == int_slot, KnownTech.character_id == combat.enemy_id)).first()
    enemy_action = take_action(combat.enemy, known_tech.tech_id, combat)
    enemy_action_str = f"{combat.enemy.name} used {enemy_action}!"
    setattr(combat, 'enemy_action', enemy_action_str)
    db.session.commit()
    updated_combat = Combat.query.first()
    return updated_combat

def take_action(actor, action_id, combat):
    action = Technique.query.filter(Technique.id == action_id).first()

    if action.target == "self":
        target = actor
    elif action.target == "opponent":
        if actor == combat.player:
            target = combat.enemy
        elif actor == combat.enemy:
            target = combat.player

 #####DEAL DMG#####
    if action.duration == 0:
        if action.stat == "hp":
            if target != actor:
                new_hp = target.crnt_hp - calculate_dmg(actor.temp_pwr, target.temp_def, action.modifier, action.amnt)
                #print(f"new_hp: {new_hp}")
    ####HEAL####
            elif target == actor:
                new_hp = calculate_healing(target.temp_pwr, target.crnt_hp, target.max_hp, action.modifier, action.amnt)
            setattr(target, 'crnt_hp', new_hp)
            db.session.commit()

    ###CHANGE ORDER###
        elif action.stat == "order":
            if target.id == combat.enemy_id:
                other_combatant = combat.player
            elif target.id == combat.player_id:
                other_combatant = combat.enemy
            setattr(target, 'order', action.amnt)
            other_order = 3 - action.amnt
            setattr(other_combatant, 'order', other_order)
            db.session.commit()

    ###CREATE STATUS###
    else: 
        #print("this runs")
        add_status(target, action.duration, action.stat, action.amnt, combat)
    print(f"player order: {combat.player.order}")
    print(f"enemy order: {combat.enemy.order}")
    advance_turn(combat, actor)
    return action.name

    
def calculate_dmg(pwr, defence, mod, amnt):
    dmg = (pwr * mod) + amnt - defence
    #print(f"dmg: {dmg}")
    return dmg

def calculate_healing(pwr, crnt_hp, max_hp, mod, amnt):
    new_hp = crnt_hp + (mod * pwr) + amnt
    if new_hp < max_hp:
        return new_hp
    else:
        return max_hp

def add_status(target, duration, stat, amnt, combat):
    #takes in target, duration, stat, amnt
    #Checks if target has a status w/ affected_stat == stat (runs remove_status if so)
    prior_statuses = Status.query.filter(Status.affected_stat == stat and Status.character_id == target.id).all()
    if prior_statuses:
        for status in prior_statuses:
            remove_status(status)

    #updates targets temp_stats
    str_stat = f"temp_{stat}"
    new_stat = getattr(target, str_stat) + amnt
    setattr(target, str_stat, new_stat)

    #makes a new status
    new_status = Status(
        remaining_duration = duration,
        affected_stat = stat,
        amnt = amnt,
        combat_id = combat.id,
        character_id = target.id
    )

    db.session.add(new_status)
    db.session.commit()
    

def remove_status(status):
    #undoes stat changes to status.character
    str_stat = f"temp_{status.affected_stat}"
    base_stat_str = f"base_{status.affected_stat}"
    base_stat = getattr(status.character, base_stat_str)
    setattr(status.character, str_stat, base_stat)
    #deletes the status
    db.session.delete(status)
    db.session.commit()





#def player_action(actor, action_id, combat):
#     # print(f"Actor: {actor['name']}")
   
#     action = Technique.query.filter(Technique.id == action_id).first()
#     actor_obj = Character.query.filter(Character.id == actor['id']).first()
#     combat_obj = Combat.query.filter(Combat.id == combat['id']).first()
#     # print(f"Action: {action.name}")
#     # print(f"Actor type: {type(actor_obj)}")
#     if action.target == "self":
#         target = actor_obj
#     elif action.target == "opponent":
#         if actor_obj == combat_obj.player:
#             target = combat_obj.enemy
#         elif actor_obj == combat_obj.enemy:
#             target = combat_obj.player

#     #else:
#         #raise ValueError
#     # print(f"Target: {target.name}")
#     # print(f"Target type: {type(target)}")
#     # print(f"Combat type: {type(combat_obj)}")
#     # print(f"Action type: {type(action)}")
#     # print(f"Action mod: {action.modifier}")

#     #####DEAL DMG#####
#     if action.duration == 0:
#         if action.stat == "hp":
#             if target != actor_obj:
#                 new_hp = target.crnt_hp - calculate_dmg(actor_obj.temp_pwr, target.temp_def, action.modifier, action.amnt)
#                 #print(f"new_hp: {new_hp}")
#     ####HEAL####
#             elif target == actor_obj:
#                 new_hp = calculate_healing(target.temp_pwr, target.crnt_hp, target.max_hp, action.modifier, action.amnt)
#             setattr(target, 'crnt_hp', new_hp)
#             db.session.commit()

#     ###CHANGE ORDER###
#         elif action.stat == "order":
#             if target.id == combat.enemy_id:
#                 other_combatant = combat.player
#             elif target.id == combat.player_id:
#                 other_combatant = combat.enemy
#             setattr(target, 'order', action.amnt)
#             other_order = 3 - action.amnt
#             setattr(other_combatant, 'order', other_order)
#             db.session.commit()

#     ###CREATE STATUS###
#     else: 
#         #print("this runs")
#         add_status(target, action.duration, action.stat, action.amnt, combat_obj)

