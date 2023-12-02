import os
import json
def check_aunt(record):
    memory = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    #print(memory['vizslas'], memory.get('vizslasa'))
    valid = True
    for k,v in record.items():
        #if memory.get(k):
        try:
            if k in ['cats', 'trees']:
                if memory[k] >= v:
                    valid = False
                    break
            elif k in ['pomeranians', 'goldfish']:
                if memory[k] <= v:
                    valid = False
                    break
            elif memory[k] != v:
                valid = False
                break
        except KeyError:
            ""
    return valid
aunts = {}
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            
            aunt_id = line.split(':')[0].split(' ')[1]
            line = line.replace(',',':')
            aunts_detail = line.split(':')[1:]
            
            for i in range(0,len(aunts_detail),2):
                
                if not aunts.get(aunt_id):
                    aunts[aunt_id] = {}
                aunts[aunt_id] [aunts_detail[i].strip()] =  int(aunts_detail[i+1].strip())
            if check_aunt(aunts[aunt_id]):
                print(aunt_id,json.dumps(aunts[aunt_id],indent=2))
    
    print(check_aunt(aunts['116']))