import os
def counter_it(retez: str) -> int:
    counter_mem = 0
    
    i = 1
    while i < len(retez)-1:
        increment = 1
        if retez[i] == "\\":
            if retez[i+1] == 'x':
                increment = 4
            else:
                increment = 2
        print(i,retez[i])
        i+=increment
        counter_mem += 1
    return counter_mem
def counter_it2(retez: str) -> int:
    counter_mem = len(retez)+4
    
    i = 1
    while i < len(retez)-1:
        increment = 1
        counter_mem_more = 0
        if retez[i] == "\\":
            if retez[i+1] == 'x':
                increment = 4
                counter_mem += 1
            else:
                counter_mem += 2
                increment = 2
        i+=increment
        
    return counter_mem
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    output_wires = {}
    counter_mem_global = 0
    counter_mem_global2 = 0
    counter_real_global = 0
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            counter_mem_global += counter_it(line)
            counter_mem_global2 += counter_it2(line)
            counter_real_global += len(line)
            print(line, counter_it(line), counter_it2(line))
    print(f'Real: {counter_real_global}, Mem: {counter_mem_global}, Diff: {counter_real_global-counter_mem_global}')
    print(f'Real: {counter_real_global}, Mem2: {counter_mem_global2}, Diff: {-counter_real_global+counter_mem_global2}')