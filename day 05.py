import os
def check_condition_1(line: str) -> bool:
    vowels = 'aeiou'
    counter = 0
    for vowel in line:
        if vowel in vowels:
            counter+=1
    return counter >2
def check_condition_2(line:str) -> bool:
    last_char = ''
    for znak in line:
        if last_char == znak:
            return True
        last_char = znak
    return False
def check_condition_3(line:str) -> bool:
    for forbid in ['ab', 'cd', 'pq', 'xy']:
        if forbid in line:
            return False
    return True

def check_condition_4(line:str) -> bool:
    
    for i in range(len(line)-3):
        if line[i:i+2] in line[i+2:]:
            #print(2*i,2*i+1,line[2*i:2*i+2], line[2*i+2:])
            return True
    return False
def check_condition_5(line:str) -> bool:
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            return True
    return False
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
        counter = 0
        counter2 = 0
        for line in f.readlines():
            line = line.strip()
            if check_condition_1(line) and check_condition_2(line) and check_condition_3(line):
                counter+=1
            if check_condition_4(line) and check_condition_5(line):
                print('2:',line,check_condition_4(line),check_condition_5(line))
                counter2+=1
        print(f'Number of nice strings: {counter}/{counter2}')
        
    #for line in ['ugknbfddgicrmopn','aaa']:
    #    print(line,check_condition_1(line),check_condition_2(line), check_condition_3(line))