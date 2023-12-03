import os
def add_transition(transitions, src, dst):
    if not transitions.get(src):
        transitions[src] = []
    transitions[src].append(dst)
def walk_it(book):
    i = 0
    counter = 0
    
    while i < len(book['source']):
        print(i)
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
book = {
    'trans': {},
    'source': '',
    'results': {}
}
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
        
        for line in f.readlines():
            line = line.strip()
            if line == '':
                continue
            if line.find('=>')>0:
                [src,dst] = line.split(' => ')
                add_transition(book['trans'], src,dst)
            else:
                book['source'] = line
    print(book,walk_it(book),len(book['results']))
    