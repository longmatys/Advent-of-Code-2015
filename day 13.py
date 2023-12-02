import os
def seat_them(nodes, remains):
    global edges
    if remains == 0:
        return {
                'value':0,
                'name_left':'',
                'name_right':'',
                'names':''}
    
    best_candidate = None
    best_candidate_name = ''
    for node,value in nodes.items():
        if value:
            continue
        nodes[node] = True
        rest = seat_them(nodes.copy(),remains-1)
        rest_candidate = rest.copy()
        if rest['name_left'] == '':
            rest_candidate['name_left'] = node
            rest_candidate['name_right'] = node
            rest_candidate['names'] = ''
            rest_candidate['value'] = 0
        elif edges[rest['name_left']][node] + edges[node][rest['name_left']] > edges[rest['name_right']][node] + edges[node][rest['name_right']]:
            if rest['name_right'] != rest['name_left']:
                rest_candidate['names'] = rest['name_left']+','+rest['names']
            rest_candidate['name_left'] = node
            rest_candidate['value'] = rest['value'] +  edges[rest['name_left']][node] + edges[node][rest['name_left']]
        else:
            if rest['name_right'] != rest['name_left']:
                rest_candidate['names'] = rest['names']+','+rest['name_right']
            rest_candidate['name_right'] = node
            rest_candidate['value'] = rest['value'] + edges[rest['name_right']][node] + edges[node][rest['name_right']]
        if not best_candidate or rest_candidate['value'] > best_candidate['value']:
            best_candidate = rest_candidate.copy()
            if nodes.get(best_candidate_name):
                nodes[best_candidate_name] = False
            best_candidate_name = node
        
        nodes[node] = False
    return best_candidate
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    output_wires = {}
    nodes = {}
    edges = {}
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            line_a = line.split('.')[0].split(' ')
            if line[0] == '#':
                break
            nodes[line_a[0]] = False
            nodes[line_a[10]] = False
            if not edges.get(line_a[0]):
                edges[line_a[0]] = {}
            multi = 1
            if line_a[2] == 'lose':
                multi = -1
            edges[line_a[0]][line_a[10]] = multi * int(line_a[3])
    hostitel = 'MATES'
    for name in nodes.keys():
        if not edges.get(hostitel):
            edges[hostitel] = {}
        edges[name][hostitel] = 0
        edges[hostitel][name] = 0
    nodes[hostitel] = False
    result = seat_them(nodes.copy(),len(nodes.keys()))
    
    print(result,result['value']+edges[result['name_right']][result['name_left']]+edges[result['name_left']][result['name_right']])
    print()

        
