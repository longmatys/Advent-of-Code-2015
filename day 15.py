import os
def get_component_value(combination, component, debug = 0):
    ingrediant_value = 0
    for i, cookie_name in enumerate(list(cookies.keys())):
        
        ingrediant_value += combination[i]*cookies[cookie_name][component]
        if debug > 5:
            print(f'{component}: Calculate({combination}) {i},{cookie_name}: {combination[i]}*{cookies[cookie_name][component]} ,value={ingrediant_value}, result={result}')
    if ingrediant_value < 0:
        ingrediant_value = 0
    
    return ingrediant_value
    
def calculate_cookie(combination, debug = 0, calories_limit = 500):
    global cookies
    
    result = 1
    for component in ['capacity', 'durability', 'flavor', 'texture']:
        result *= get_component_value(combination, component)
    calories = get_component_value(combination, 'calories')
    if calories_limit > 0 and calories != calories_limit:
        result = 0
    if debug > 0:
        print(f'Calculate returns: {result}\n')
    return result
def generate_cookie_combination(starting_combination, index):
    #print(f'Called {starting_combination}, index: {index}')
    if starting_combination[0] == 0:
        return [calculate_cookie(starting_combination, 0), starting_combination]
    best_value = [calculate_cookie(starting_combination,0), starting_combination]
    for i in range(index,len(starting_combination)):
        new_combination = list(starting_combination)
        new_combination[0] = new_combination[0] - 1
        new_combination[i] += 1
        #print(f'Created new combinations: {new_combination}, i:{i}')
        
        #generate_cookie_combination
        
        value = generate_cookie_combination(new_combination,i)
        #value = best_value
        #print(index, i, new_combination,f"Value: {value}",f"Best value: {best_value}")
        if value[0] > best_value[0]:
            #print(f"Nasel jsem lepsi value",new_combination,f"Value: {value}",f"Best value: {best_value}")
            best_value = value
    return best_value
            
cookies = {}
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()

            cookie_name = line.split(":")[0]
            
            for cookie_component in line.split(":")[1].split(","):
                cookie_component_arr = cookie_component.strip().split(' ')        
                if not cookies.get(cookie_name):
                    cookies[cookie_name] = {}
                cookies[cookie_name][cookie_component_arr[0]] = int(cookie_component_arr[1])
        print(cookies)
        #print(generate_cookie_combination([5,0,0,0],1))
    #print((list(cookies.keys())))
    #print(calculate_cookie([1,1,2,1],15))
    print(generate_cookie_combination([100,0,0,0],1))