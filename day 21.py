import math
import os
import json
import sys
def init_store(store):
    store_txt = """\
Weapons*:    Cost  Damage  Armor
Dagger:        8     4       0
Shortsword:   10     5       0
Warhammer:    25     6       0
Longsword:    40     7       0
Greataxe:     74     8       0

Armor*:      Cost  Damage  Armor
Leather:      13     0       1
Chainmail:    31     0       2
Splintmail:   53     0       3
Bandedmail:   75     0       4
Platemail:   102     0       5

Rings*:      Cost  Damage  Armor
Damage +1:    25     1       0
Damage +2:    50     2       0
Damage +3:   100     3       0
Defense +1:   20     0       1
Defense +2:   40     0       2
Defense +3:   80     0       3
"""
    for line in store_txt.splitlines():
        line = line.strip()
        if line == '':
            continue
        if '*' in line:
            store_name = line.split('*')[0]
            attrs = []
            for el in line.split(':')[1].split(' '):
                if el == '':
                    continue
                attrs.append(el)
            if store_name != 'Weapons':
                store[store_name] = {'nic':{'Cost': 0, 'Damage': 0, 'Armor': 0}}
            else:
                store[store_name] = {}
            
        else:
            item_name = line.split(':')[0]
            values = []
            for el in line.split(':')[1].split(' '):
                if el == '':
                    continue
                values.append(el)
            
            
            store[store_name][item_name] = {}
            for i, value in enumerate(values):
                store[store_name][item_name][attrs[i]] = int(value)
                
    store['Rings offhand'] = store['Rings']
    print(f'|{json.dumps(store,indent=2)}|')
def get_damage(damage,armor):
    if armor >= damage:
        return 1
    return damage - armor
def get_result(me,enemy):
    result_enemy = get_damage(enemy['Damage'], me['Armor'])
    result_me = get_damage(me['Damage'], enemy['Armor'])
    enemy_needs = math.ceil(me['Hit Points'] / result_enemy)
    me_needs = math.ceil(enemy['Hit Points'] / result_me)
    ret_result = me_needs <= enemy_needs
    if not ret_result and me['Cost'] > 232:
        ""
        print(f'Result: Me({me}), Enemy({enemy}), Enemy dmg {result_enemy}, My dmg {result_me}, Vyhraju: {ret_result}, Kol: ja={me_needs}/{enemy["Hit Points"] / result_me}, enemy={enemy_needs}/{me["Hit Points"] / result_enemy}')
        print(me)
    return ret_result
def dump_list(store,me,shop_list):
    me['Damage'] = 0
    me['Armor'] = 0
    me['Cost'] = 0
    for (store_name,item_name) in shop_list:
        print(f'{store_name}:{item_name} ({store[store_name][item_name]["Cost"]})')
        for attr, value in store[store_name][item_name].items():
            if attr == 'nic':
                next
            print(f'{attr}:{value}')
            me[attr] += value
        print('')
def evaluate_list(store,me,enemy,shop_list):
    me['Damage'] = 0
    me['Armor'] = 0
    me['Cost'] = 0
    for (store_name,item_name) in shop_list:
        #print(item_name,store[store_name][item_name]['Cost'])
        for attr, value in store[store_name][item_name].items():
            if attr == 'nic':
                next
            me[attr] += value
    if not get_result(me,enemy):
        if me['Cost'] > 232:
            print(shop_list)
        return (me['Cost'],shop_list)
    return (None,None)
def check_rings_duplicity(shop_list,ring_name):
    for (shop_name,item_name) in shop_list:
        if shop_name.startswith('Rings'):
            return item_name == ring_name
    return False
def find_cheapest_combo(store,me,enemy,visited_shops,shop_list):
    if len(store.keys()) == len(visited_shops):
        return evaluate_list(store,me,enemy,shop_list)
    (best_value,best_combo) = (None,None)
    for store_name, store_items in store.items():
        if store_name in visited_shops:
            continue
        for item_name in store_items.keys():
            if store_name.startswith('Rings') and item_name !='nic' and check_rings_duplicity(shop_list,item_name):
                    continue
            (value,combo) = find_cheapest_combo(store,me,enemy,visited_shops + [store_name], shop_list + [(store_name,item_name)])
            if value != None and (best_value == None or  best_value < value):
                
                (best_value,best_combo) = (value,combo)
                if best_value > 230:
                    print(best_value)
    return (best_value,best_combo)
def try_it(enemy):
    #233 [('Weapons', 'nic'), ('Armor', 'Splintmail',3), ('Rings', 'Damage +3'), ('Rings offhand', 'Defense +3')]
    me = {
        'Armor': 6,
        'Hit Points': 100,
        'Damage': 3,
        'Cost': 300
    }
    get_result(me,enemy)
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    enemy = {}
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            enemy[line.split(":")[0]] = int(line.split(":")[1])
    print(enemy)
    me = {
        'Armor': 0,
        'Hit Points': 100,
        'Damage': 10
        
    }
    #try_it(enemy)
    #sys.exit(1)
    get_result(me,enemy)
    store = {}
    init_store(store)
    (v,c) = find_cheapest_combo(store,me, enemy, [], [])
    print(v,c)
    evaluate_list(store,me,enemy,c)
    #dump_list(store,me,[('Weapons', 'nic'), ('Armor', 'Splintmail'), ('Rings', 'Damage +3'), ('Rings offhand', 'Defense +3')])
    #233 is too high!