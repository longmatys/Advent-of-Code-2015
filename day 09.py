import os
def travel_santa(towns,current_town, towns_to_visit, path):
        
    if towns_to_visit == 0:
        
        return (0,f'{path}, {current_town}')
    global ways
    towns[current_town] = True
    rest_way_length_best = None
    best_path = ''
    for candidate in ways[current_town].keys():
        if not towns[candidate]:
            
            (rest_way_length,rest_path) = travel_santa(towns.copy(),candidate,towns_to_visit-1, f'{path}, {current_town} ({ways[current_town][candidate]})')
            #Just invert < to > and it will find shortest distance
            if not rest_way_length is None and (not rest_way_length_best or rest_way_length_best < rest_way_length  + ways[current_town][candidate]):
                rest_way_length_best = rest_way_length + ways[current_town][candidate]            
                best_path = rest_path
    
    return (rest_way_length_best, best_path)
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    output_wires = {}
    towns = {}
    ways = {}
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line[0] == '#':
                break
            line_a = line.split(' ')
            towns [line_a[0]] = False
            towns [line_a[2]] = False
            if not ways.get(line_a[0]):
                ways[line_a[0]] = {}
            if not ways.get(line_a[2]):
                ways[line_a[2]] = {}
            ways [line_a[0]][line_a[2]]= int(line_a[4])
            ways [line_a[2]][line_a[0]]= int(line_a[4])
            print(line)
    
    
    delka = len(towns)
    for town in towns.keys():    
        (len, path) = travel_santa(towns.copy(),town,delka-1, '')
        print(path[2:], len)
