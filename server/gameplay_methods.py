from config import app, db, api
from models import Combat, Status, Character, Player, KnownTech, Technique, Enemy

def begin_combat():
    pass

def player_action(actor, action_id, combat):
    # print(f"Actor: {actor['name']}")
   
    action = Technique.query.filter(Technique.id == action_id).first()
    actor_obj = Character.query.filter(Character.id == actor['id']).first()
    combat_obj = Combat.query.filter(Combat.id == combat['id']).first()
    # print(f"Action: {action.name}")
    # print(f"Actor type: {type(actor_obj)}")
    if action.target == "self":
        target = actor_obj
    elif action.target == "enemy":
        target = Character.query.filter(Character.id == combat_obj.enemy_id).first()

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


