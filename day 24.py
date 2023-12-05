import os
import copy
def insert_to_sane(sane,oddil,balik):
    sane[oddil][0]+=balik
    sane[oddil][1]+=1
    sane[oddil][2]*=balik
    #sane[oddil][-1].append(balik)
    return sane
def compare_simple(sane_best, sane_variant):
    ret_value = True
    for i in range(len(sane_best)):
        ret_value &= (sane_best[i][0] == sane_variant[i][0])
    return ret_value
def choose_better_sane(sane_best, sane_variant):
    if sane_variant:
        if not sane_best:
            return sane_variant
        elif not compare_simple(sane_best, sane_variant):
            return sane_best
        elif sane_variant[0][1] == sane_best[0][1]:
            if sane_variant[0][2]<sane_best[0][2]:
                return sane_variant
            else:
                return sane_best
        elif sane_variant[0][1] < sane_best[0][1]:
            return sane_variant
        else:
            return sane_best
    else :
        return sane_best
#[[512, 7, 707927634298, [101, 97, 89, 83, 73, 67, 2]], [512, 6, 10723906903, [113, 109, 107, 103, 79, 1]], [512, 16, 8053650944408022185505, [71, 61, 59, 53, 43, 41, 37, 31, 29, 23, 19, 17, 13, 7, 5, 3]]]
best_middle = None
global_counter = 0
#[[384, 4, 83754556, [103, 101, 97, 83]],[384, 5, 139699414, [113, 109, 107, 53, 2]],  [384, 6, 12207960455, [89, 79, 73, 71, 67, 5]], [384, 14, 428044163933458527, [61, 59, 43, 41, 37, 31, 29, 23, 19, 17, 13, 7, 3, 1]]]
def sort_it(storage,sane):
    global best_middle
    global global_counter
    global_counter += 1
    #if global_counter%100000 == 0:
    #    print(f'{global_counter}: zkousim {sane} ({storage})')
    #if choose_better_sane(best_middle,sane) == best_middle:
    #    return None
    if len(storage[1])==0:
        if sane[0][0] == sane[1][0] and sane[2][0] == sane[0][0] and sane[3][0] == sane[1][0]:
            if choose_better_sane(best_middle,sane) == sane:
                best_middle = sane
                print(f'Nasel jsem jednu variantu {sane}')
                return sane
            else:
                return None
        else:
            return None
    elif best_middle:
        if best_middle[0][1] < sane[0][1]:
            return None
        if best_middle[0][1] == sane[0][1] and best_middle[0][2] < sane[0][2]:
            return None
    storage_new = copy.deepcopy(storage)
    #balik = storage_new[1][-1]
    
    balik = storage_new[1].pop()
    sane_best = None
    for i in range(len(sane)):
        if sane[i][0] + balik <= storage_new[0] :
            sane_new = copy.deepcopy(sane)
            sane_variant = sort_it(storage_new,insert_to_sane(sane_new,i,balik))
            sane_best = choose_better_sane(sane_best,sane_variant)
    return sane_best
            
            
            
    
def main():
    global best_middle
    storage = [0,[]]
    sane = [[0,0,1] for _ in range(4)]
    
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            storage[0] += int(line)
            storage[1].append(int(line))
            
        storage[0] = int(storage[0]/len(sane))
    best_middle = [[storage[0],len(storage[1]),1] for _ in range(len(sane))]
    
    maska = 0
    for i in range(len(storage[1])):
        maska = (maska << 1) + 1
    print(bin(2**len(storage[1])-1))        
    print(sort_it(storage,sane))
if __name__ == '__main__':
    main()
