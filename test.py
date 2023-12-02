retez='Arbre (24), Faerun (58), Tristram (49), Tambi (15), Snowdin (12), AlphaCentauri (15), Norrath (54), Straylight'
retez_a = retez.split(' ')
print(retez_a)
counter = 0
for k,v in enumerate(retez_a):
    if v[0] == '(':
        print(k,v,int(v[1:-2]))
        counter+=int(v[1:-2])
print(counter)