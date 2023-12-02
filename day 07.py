import os
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    output_wires = {}
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            
            line_elements = line.split(' ')
            if len(line_elements) == 3:
                output_wires[line_elements[2]] = {
                    'operation' : 'ASSIGN',
                    'raw': line,
                    'operands' : [line_elements[0]]
                }
            elif line_elements[0]=='NOT':
                #Tohle je pouze NOT operace
                
                output_wires[line_elements[3]] = {
                    'operation' : line_elements[0],
                    'raw': line,
                    'operands' : [line_elements[1]]
                }
            else:
                
                output_wires[line_elements[4]] = {
                    'operation' : line_elements[1],
                    'raw': line,
                    'operands' : [line_elements[0], line_elements[2]]
                }
    start_wire = 'a'
    #It will never finish without caching results
    results_map = {'b': 16076}
    def get_wire_value(output_wires,wire,depth=0):
        global results_map
        if results_map.get(wire):
            return results_map.get(wire)
        depth+=1
        value = 0
        print(f'Pozaduji ({depth}): {output_wires[wire]["raw"]}')
        try:
            
            if output_wires[wire]['operation'] in ['AND','OR','LSHIFT','RSHIFT','ASSIGN','NOT']:
                values = []
                for i in range(len(output_wires[wire]['operands'])):
                    values.append(output_wires[wire]['operands'][i])    
                    if values[i].isnumeric():
                        values[i] = int(values[i]) & 0xffff
                    else:
                        values[i] = get_wire_value(output_wires,output_wires[wire]['operands'][i],depth)
                if output_wires[wire]['operation'] == 'AND':
                    return_value =  values[0] & values[1]
                if output_wires[wire]['operation'] == 'OR':
                    return_value =  values[0] | values[1]
                if output_wires[wire]['operation'] == 'LSHIFT':
                    return_value =  values[0] << values[1]
                if output_wires[wire]['operation'] == 'RSHIFT':
                    return_value =  values[0] >> values[1]
                if output_wires[wire]['operation'] == 'ASSIGN':
                    return_value =  values[0]
                if output_wires[wire]['operation'] == 'NOT':
                    return_value =  (~ values[0]) & 0xffff
                print(f"Final value of {wire} = {return_value}")
                results_map[wire] = return_value
                return return_value

            else:
                print(output_wires[wire]['operation'])
            
        except KeyError as e:
            print('TypeError:', e, output_wires[wire]['raw'],output_wires[wire]['operands'])
        return value
    print((get_wire_value(output_wires,start_wire)))
    
        
            