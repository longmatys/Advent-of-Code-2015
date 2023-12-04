from copy import deepcopy
debug = True
def can_cast_spell(status, spell):
    if status['wizard']['mana'] >= spell['cost']:
        return True
    return False
def get_damage(enemy_attack, wizard_defense):
    if wizard_defense >= enemy_attack:
        return 1
    return enemy_attack - wizard_defense
def evaluate_turn_effects(status):
    global debug
    return_status = deepcopy(status)
    return_status['wizard']['shield'] = 0
    if status['turn'] == 'wizard':
        return_status['wizard']['hit points'] -= 1
        
    if len(status['effects']) > 0:
        
        for effect in return_status['effects']:
            if effect['value'][0] > 0:
                effect['value'][0] -= 1
                if effect['type'] == 'time_shield':
                    if debug:
                        print(f"Shield provides {effect['value'][1]} and lasts {effect['value'][0]}")
                    return_status['wizard']['shield'] += effect['value'][1]
                if effect['type'] == 'time_damage':
                    if debug:
                        print(f"Poison deals {effect['value'][1]} damage and lasts {effect['value'][0]}")
                    return_status['enemy']['hit points'] -= effect['value'][1]
                if effect['type'] == 'time_recharge':
                    if debug:
                        print(f"Regarge adds {effect['value'][1]} mana and lasts {effect['value'][0]}")
                    return_status['wizard']['mana'] += effect['value'][1]
                    
                #if effect['value'][0] > 1:
                
    
    
    return return_status
def get_battle_status(status):
    if not status:
        #print(f'Dosla mi mana')
        return -1
    if status['enemy']['hit points'] <= 0:
        return 1
    if status['wizard']['hit points'] <= 0:
        return -1
    return 0
global_best_mana = None
def cast_spell(status,spells,spell_i):
    global global_best_mana
    global debug
    if debug :
        debug_spells = [3,0]
        debug_spells = [4,2,1,3,0]
        debug_spells = [3,4,3,3,0,0]
        debug_spells = [4,0,4,0,0]
        spell = spells[debug_spells[len(status['spells_casted'])]]
        
    else:
        spell = spell_i
    if spell['cost'] > status['wizard']['mana']:
        return None
    if  global_best_mana and status['mana_spent'] + spell['cost'] > global_best_mana:
        return None
    if debug:
        print(f"Player casts {spell['name']}")
    for effect in status['effects']:
        if effect['value'][0] > 0 and effect['name'] == spell['name']:
            return None
    return_status = deepcopy(status)
    if spell['type'].startswith('time'):
        return_status['effects'].append(deepcopy(spell))
    elif spell['type'] == 'instant_damage':
        return_status['enemy']['hit points'] -= spell['value']
    elif spell['type'] == 'instant_drain':
        return_status['wizard']['hit points'] += spell['value'][0]
        return_status['enemy']['hit points'] -= spell['value'][1]
    return_status['mana_spent'] += spell['cost']
    return_status['wizard']['mana'] -= spell['cost']
    return_status['spells_casted'].append(spell['name'])
    return return_status

def battle(status, spells):
        global global_best_mana
        if debug:
            print(f"-- {status['turn']} turn --")
            print(f"- wizard has {status['wizard']['hit points']} hit points, {status['wizard']['mana']} mana")
            print(f"- Boss has {status['enemy']['hit points']} hit points")
    #while(get_battle_status(status)):
        new_status = evaluate_turn_effects(status)
        battle_status = get_battle_status(new_status)
        if battle_status:
            return  new_status
        if status['turn'] == 'wizard':
            
            best_status = None
            for spell in spells:
                new_status2 = cast_spell(new_status,spells,spell)
                if new_status2:
                    battle_status = get_battle_status(new_status2)
                    if battle_status == 0:
                        new_status2['turn'] = 'enemy'
                        new_status2 = battle(new_status2, spells)
                    battle_status = get_battle_status(new_status2)
                    if battle_status:
                        if battle_status == 1:
                            if new_status2 and (not best_status or new_status2['mana_spent'] < best_status['mana_spent']):
                                
                                best_status = new_status2
                                if not global_best_mana or global_best_mana > best_status['mana_spent']:
                                    global_best_mana = best_status['mana_spent']
                                    print(f"Nasel jsem viteznou kombinaci {best_status['mana_spent']}: {best_status['spells_casted']}")
            return best_status 
                
            
        else:
            if debug:
                print(f"Boss attacks for {get_damage(new_status['enemy']['damage'],new_status['wizard']['shield'])} damage")
            new_status['wizard']['hit points'] -= get_damage(new_status['enemy']['damage'],new_status['wizard']['shield'])
            new_status['turn'] = 'wizard'
        battle_status = get_battle_status(new_status)
        if battle_status:
            return new_status
        return battle(new_status,spells)
        
            
            
        new_status = evaluate_turn(status)
                
    
def main():
    global debug
    debug = False
    enemy = {
        'hit points': 51,
        'damage': 9
    }
    wizard = {
        'hit points': 50,
        'mana': 500,
        'shield': 0
    }
    #Testing
    if debug and False:
        enemy = {
            'hit points': 13,
            'damage': 8
        }
        wizard = {
            'hit points': 10,
            'mana': 250,
            'shield': 0
        }
    effects = [
        #[]
    ]
    spells = [{
            'name': 'Magic Missile',
            'type': 'instant_damage',
            'value': 4,
            'cost': 53
        },{
            'name': 'Drain',
            'type': 'instant_drain',
            'value': [2,2], #my heal, enemy hurts
            'cost': 73
        },{
            'name': 'Shield',
            'type': 'time_shield',
            'value': [6,7], #time, shield_up
            'cost': 113
        },{
            'name': 'Poison',
            'type': 'time_damage',
            'value': [6,3], #time, enemy hurts
            'cost': 173
        },{
            'name': 'Recharge',
            'type': 'time_recharge',
            'value': [5,101],
            'cost': 229
        }
        
    ]
    status = {
        'wizard': wizard,
        'enemy': enemy,
        'mana_spent': 0,
        'effects': [],
        'turn': 'wizard',
        'spells_casted': []
    }
    status2 = deepcopy(status)
    status2['wizard']['mana'] =10
    
    print(battle(status,spells))
        
if __name__ == '__main__':
# Get the name of the Python script
    main()
    #801 is too low
    #2052 is too high