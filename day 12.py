import os
import json
def get_sum(my_object):
    obj_type = type(my_object).__name__
    counter = 0
    if obj_type == 'list':
        for i in my_object:
            counter += get_sum(i)
    elif obj_type == 'dict':
        for k,v in my_object.items():
            if k.isnumeric():
                counter+= int(k)
            if v == 'red':
                counter = 0
                break
            counter+= get_sum(v)
    elif obj_type == 'int':
        counter = my_object
    elif obj_type == 'str':
        #print(my_object)
        ""
    else:
        print(f'Neumim: {obj_type}')
    return counter
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    output_wires = {}
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            log = json.loads(line)
            print(type(log).__name__,len(log))
            print(get_sum(log))
            