import os
import json
def add_transition(book, src, dst):
    if not book['trans'].get(src):
        book['trans'][src] = []
    book['trans'][src].append(dst)
    if book['trans_r'].get(dst):
        raise ValueError
    book['trans_r'][dst] = src
    
def walk_it(book):
    i = 0
    counter = 0
    
    while i < len(book['source']):
        mod = 1
        valid = False
        if not book['trans'].get(book['source'][i]):
            if book['trans'].get(book['source'][i:i+2]):
                mod = 2
                valid = True
        else:
            valid = True
        if valid:
            for variant in book['trans'].get(book['source'][i:i+mod]):
                candidate = book['source'][0:i] + variant + book['source'][i+mod:]
                if not book['results'].get(candidate):
                    book['results'][candidate] = True
        i+=mod
    return counter
def dump_cache(cache):
    script_name = os.path.basename(__file__)
    filename = script_name.split('.')[0]+'.cache.json'
    with open(filename,'w') as f:
        json.dump(cache,f, indent=2)
def read_cache():
    return ""
    script_name = os.path.basename(__file__)
    filename = script_name.split('.')[0]+'.cache.json'
    with open(filename,'r') as f:
        cache = json.load(f)
    return cache
def reduce_it(book,medicine):
    i = 0
    global global_counter
    global_counter+=1
    if medicine == 'e':
        return 0
    best = -1
    counter = 0
    while medicine != 'e':
        
        for klic,value in book['trans_r'].items():
            if klic not in medicine:
                continue
            medicine = medicine.replace(klic,value,1)
            counter+=1

                    
        
    return counter
book = {
    'trans': {},
    'trans_r': {},
    'source': '',
    'results': {},
    'cache': read_cache(),
    'last_dump': 0,
    'last_print': 0
}
global_counter = 0
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
        
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            if line == '':
                continue
            if line.find('=>')>0:
                [src,dst] = line.split(' => ')
                add_transition(book, src,dst)
            else:
                book['source'] = line
    print(walk_it(book),len(book['results']))
    print("Zde",reduce_it(book,book['source']))
    