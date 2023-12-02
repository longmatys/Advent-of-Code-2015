import os
import json
import math
def get_winner(deers, racetime):
    best_r = ['',0]
    for k,v in deers.items():
        units_float = racetime/(v["flytime"]+v["resttime"])
        units_int = math.floor(units_float)
        units_rest = racetime - (units_int * (v["flytime"]+v["resttime"]))
        if units_rest < v["flytime"]:
            fly_rest = units_rest
        else:
            fly_rest = v["flytime"]
            
        fly_distance = (units_int * v["flytime"] + fly_rest) * v["speed"]
        if fly_distance > best_r[1]:
            best_r = [k, fly_distance]
        
    return best_r
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    deers = {}
    racetime = 2503
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            line_a = line.split(' ')
            deers[line_a[0]] = {
                'speed': int(line_a[3]),
                'flytime': int(line_a[6]),
                'resttime': int(line_a[13]),
                'points': 0
            }
            
        result = get_winner(deers,racetime)
        print("Winner of the first race:", result)
        
        for i in range(racetime):
            result = get_winner(deers,i+1)
            deers[result[0]]['points'] +=1
        best_r = ['',0]
        for k,v in deers.items():
            if v['points'] > best_r[1]:
                best_r = [k,v['points']]
                
        print(json.dumps(deers, indent=2))
        print(best_r)
            
