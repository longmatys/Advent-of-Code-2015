import os
import copy
def insert_to_sane(sane,oddil,balik):
    sane[oddil][0]+=balik
    sane[oddil][1]+=1
    sane[oddil][2]*=balik
    sane[oddil][-1].append(balik)
    return sane
def choose_better_sane(sane_best, sane_variant):
    if sane_variant:
        if not sane_best:
            return sane_variant
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
def sort_it(storage,sane):
    global best_middle
    #if choose_better_sane(best_middle,sane) == best_middle:
    #    return None
    if len(storage[1])==0:
        if sane[0][0] == sane[1][0] and sane[2][0] == sane[0][0]:
            if choose_better_sane(best_middle,sane) == sane:
                best_middle = sane
                print(f'Nasel jsem jednu variantu {sane}')
                return sane
            else:
                return None
        else:
            return None
    elif choose_better_sane(best_middle,sane) == best_middle:
        return None
    storage_new = copy.deepcopy(storage)
    balik = storage_new[1].pop()
    sane_best = None
    for i in range(3):
        if sane[i][0] + balik <= storage_new[0] / 3:
            sane_new = copy.deepcopy(sane)
            sane_variant = sort_it(storage_new,insert_to_sane(sane_new,i,balik))
            sane_best = choose_better_sane(sane_best,sane_variant)
    return sane_best
            
            
            
    
def main():
    storage = [0,[]]
    sane = [[0,0,1,[]],[0,0,1,[]],[0,0,1,[]]]
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            storage[0] += int(line)
            storage[1].append(int(line))
    print(sort_it(storage,sane))
if __name__ == '__main__':
    main()
