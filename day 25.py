import os
def calculate_value(value):
    #return value+1
    return (252533*value)%33554393
def main():
    row = 2981
    column = 3075
    #row = 3
    #column = 4
    code_table=[[]]
    start_line = 1
    print_line = 0
    start_value = 20151125
    #start_value = 1
    
    value = start_value
    for diagonal in range(1,(row+1)*(column+1)):
        if start_value == value:
            print(f'Opakuje se to {start_line}')
        if start_line % 10000 == 0:
            print(f"Zpracovavam radek {start_line}")
            ""
        radek = start_line
        sloupec = 1
        #if start_line > 1:
        #    code_table.append([])
        
        while sloupec <= start_line:
            if radek==row and column==sloupec:
                print(f'!!!   Pozice {row},{column} je {value} !!!')
                return
            #code_table[radek-1].append(value)
            value = calculate_value(value)
            radek-=1
            sloupec+=1
        start_line +=1
    #for line in code_table:
        #print(line)
    #print("Hotovo", code_table[row-1][column-1])
if __name__ == '__main__':

    main()