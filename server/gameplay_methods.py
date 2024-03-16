from config import app, db, api
from models import Combat, Status, Character, Player, KnownTech, Technique, Enemy

def begin_combat():
    combat = Combat.query.first()
    if combat.player.order == 1:
        get_player_action(combat)
    elif combat.enemy.order == 1:
        get_enemy_action(combat)

def end_combat(winner, combat):
    pass
    #delete all statuses
    for status in combat.statuses:
        remove_status(status)
    #reset hp (later handle gameover)
    setattr(combat.player, 'crnt_hp', combat.player.max_hp)
    setattr(combat.enemy, 'crnt_hp', combat.enemy.max_hp)
    #delete combat
    db.session.delete(combat)
    db.session.commit()
    #navigate to ventures

def advance_turn(combat, crnt_combatant):
    pass
    #check hps
    if combat.player.crnt_hp <= 0:
        end_combat(combat.enemy, combat)
    elif combat.enemy.crnt_hp <= 0:
        end_combat(combat.player, combat)
    
    if crnt_combatant == combat.player:
        players_turn = True
        other_combatant = combat.enemy
    elif crnt_combatant == combat.enemy:
        players_turn = False
        other_combatant = combat.player
    

    if combat.turn == 1:
        setattr(combat, 'turn', 2)
        if players_turn:
            get_enemy_action(combat)
        elif not players_turn:
            get_player_action(combat)
    elif combat.turn == 2:
        setattr(combat, 'turn', 1)
        advance_rnd(combat)

        
def advance_rnd(combat):
    combat.turn = 1
    setattr(combat, 'rnd', combat.rnd+1)
    for status in combat.statuses:
        setattr(status, 'remaining_duration', status.remaining_duration-1)
        if status.remaining_duration <= 0:
            remove_status(status)

    if combat.player.order == 1:
        get_player_action(combat)
    elif combat.enemy.order == 1:
        get_enemy_action(combat)

def get_player_action(combat):
    pass
    #take_action(combat.player, chosen_action.id, combat)

def get_enemy_action(combat):
    action_number = combat.rnd % len(combat.enemy.actions)
    action_slot = combat.enemy.actions[action_number-1]
    known_tech = KnownTech.query.filter(KnownTech.character_id == combat.enemy_id and KnownTech.slot == action_slot).first()
    take_action(combat.enemy, known_tech.tech_id, combat)
    advance_turn(combat, combat.enemy)

def take_action(actor, action_id, combat):
    pass
    #

def player_action(actor, action_id, combat):
    # print(f"Actor: {actor['name']}")
   
    action = Technique.query.filter(Technique.id == action_id).first()
    actor_obj = Character.query.filter(Character.id == actor['id']).first()
    combat_obj = Combat.query.filter(Combat.id == combat['id']).first()
    # print(f"Action: {action.name}")
    # print(f"Actor type: {type(actor_obj)}")
    if action.target == "self":
        target = actor_obj
    elif action.target == "opponent":
        if actor_obj == combat_obj.player:
            target = combat_obj.enemy
        elif actor_obj == combat_obj.enemy:
            target = combat_obj.player

    #else:
        #raise ValueError
    # print(f"Target: {target.name}")
    # print(f"Target type: {type(target)}")
    # print(f"Combat type: {type(combat_obj)}")
    # print(f"Action type: {type(action)}")
    # print(f"Action mod: {action.modifier}")

    #####DEAL DMG#####
    if action.duration == 0:
        if action.stat == "hp":
            if target != actor_obj:
                new_hp = target.crnt_hp - calculate_dmg(actor_obj.temp_pwr, target.temp_def, action.modifier, action.amnt)
                #print(f"new_hp: {new_hp}")
    ####HEAL####
            elif target == actor_obj:
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
        add_status(target, action.duration, action.stat, action.amnt, combat_obj)


    
def calculate_dmg(pwr, defence, mod, amnt):
    dmg = (pwr * mod) + amnt - defence
    #print(f"dmg: {dmg}")
    return dmg

def calculate_healing(pwr, crnt_hp, max_hp, mod, amnt):
    new_hp = crnt_hp + (mod * pwr) + amnt
    if new_hp < max_hp:
        return new_hp
    else
        return max_hp

def add_status(target, duration, stat, amnt, combat):
    #takes in target, duration, stat, amnt
    #Checks if target has a status w/ affected_stat == stat (runs remove_status if so)
    #print("so does this")
    prior_statuses = Status.query.filter(Status.affected_stat == stat and Status.character_id == target.id).all()
    if prior_statuses:
        for status in prior_statuses:
            remove_status(status)
    str_stat = f"temp_{stat}"
    new_stat = getattr(target, str_stat) + amnt
    setattr(target, str_stat, new_stat)

    new_status = Status(
        remaining_duration = duration,
        affected_stat = stat,
        amnt = amnt,
        combat_id = combat.id,
        character_id = target.id
    )

    db.session.add(new_status)
    db.session.commit()

    
    

    #updates targets temp_stats
    #makes a new status

def remove_status(status):
    pass
    #takes in status
    #undoes stat changes to status.character
    #deletes the status


