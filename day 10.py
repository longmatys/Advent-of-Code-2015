from memory_profiler import profile
from line_profiler import LineProfiler

lp = LineProfiler()

#@profile
#@lp.profile
def transform_sentence(retez):
    last_char = retez[0]
    counter_char = 1
    ret = ''
    for znak in retez[1:]:
        if znak == last_char:
            counter_char +=1
        else:
            #ret = f'{ret}{counter_char}{last_char}'
            ret += str(counter_char) + last_char
            last_char = znak
            counter_char = 1
    #ret = f'{ret}{counter_char}{last_char}'
    ret += str(counter_char) + last_char
    return ret
sentence = '1113122113'
lp_wrapper = lp(transform_sentence)
for i in range(50):
    new_sentence = transform_sentence(sentence)
    
    
    
    #new_sentence = lp_wrapper(sentence)
    #lp.print_stats()
    #print(f'{sentence} -> {new_sentence}')
    sentence = new_sentence
    print(i,len(sentence))