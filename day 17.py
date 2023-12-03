import os
def get_sum(pocty):
    global kybly
    suma = 0
    count_1 = 0
    for i in range(len(pocty)):
        if pocty[i]:
            count_1+=1
        suma += pocty[i] * kybly[i]
    return (suma,count_1)
def find_combinations(pocty,index):
    global kybly
    global limit
    (objem,count_i) = get_sum(pocty)
    #print(f'Testuji kombinaci {pocty} /{index }')
    if index >= len(pocty):
        return (0,0)
    if objem > limit:
        return (0,0)
    if objem == limit:
        print(f"Nasel jsem kombinaci: {pocty}")
        return (1,count_i)
    ret_value = 0
    best_packages = 0
    for i in range(index,len(pocty)):
        if pocty[i] == 1:
            continue
        nove_pocty = list(pocty)
        nove_pocty[i]+=1
        (local_count,local_packages) = find_combinations(nove_pocty,i)
        if best_packages == 0 or ( best_packages > local_packages and local_packages > 0):
            ret_value = local_count
            best_packages = local_packages
        elif best_packages == local_packages:
            ret_value += local_count
        
    
    
    
    return (ret_value, best_packages)
kybly = []
limit = 150

if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
    
        for line in f.readlines():
            line = line.strip()
            kybly.append(int(line))

    kybly.sort(reverse=True)
    
    print(kybly)
    print(find_combinations([0 for _ in range(len(kybly))],0))
    #print(get_sum([0, 1, 1, 0, 0]))