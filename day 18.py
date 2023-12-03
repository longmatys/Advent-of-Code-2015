import os
import copy
field1 = []
field2 = []
def get_state(field,x,y):
    if y<0 or x<0 or y>=len(field) or x>=len(field[0]):
        return False
    return field[x][y] == '#'
def get_neighbors(field,x,y):
    ret_count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if get_state(field,x+i,y+j):
                ret_count+=1
    return ret_count
def animate(field_in,field_out):
    for i in range(len(field_in)):
        for j in range(len(field_in[0])):
            count = get_neighbors(field_in,i,j)
            if field_in[i][j] == '#':
                if count in [2,3]:
                    field_out[i][j] = '#'
                else:
                    field_out[i][j] = '.'
            elif field_in[i][j] == '.':
                if count == 3:
                    field_out[i][j] = '#'
                else:
                    field_out[i][j] = '.'
def break_lights(field):
    for i in [0,len(field)-1]:
        for j in [0, len(field[0])-1]:
            field[i][j] = '#'
                
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
        
        for line in f.readlines():
            line = line.strip()
            if line.startswith('X'):
                break
            field1.append(list(line))
            field2.append(list(line))
field_a = field1
field_b = field2
field_temp = field2
def dump_field(field):
    for i in field:
        print(''.join(i))
    print('')
for i in range(100):
    break_lights(field_a)
    animate(field_a,field_b)
    #print('INPUT:')
    #dump_field(field_a)
    #print('OUTPUT:')
    #dump_field(field_b)
    field_temp = field_a
    field_a = field_b
    field_b = field_temp
break_lights(field_a)
counter = 0
for i in range(len(field_a)):
    for j in range(len(field_a)):
        if field_a[i][j] == '#':
            counter+=1
print(counter)