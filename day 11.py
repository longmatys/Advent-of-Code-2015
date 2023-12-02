def get_next_password(pass_array, pos):
    
    if pass_array[pos] == ord('z'):
        pass_array[pos] = ord('a')
        get_next_password(pass_array,pos-1)
    else:
        pass_array[pos] = pass_array[pos]+1
def valid_test1(pass_array):
    for i in range(len(pass_array)-2):
        if pass_array[i] == pass_array[i+1]-1 and pass_array[i] == pass_array[i+2]-2:
            return True
    return False
def valid_test2(pass_array):
    return not ord('i') in pass_array and not ord('o') in pass_array and not ord('l') in pass_array
def valid_test3(pass_array):
    last_char = None
    dvojic = 0
    for i in range(len(pass_array)):
        if last_char == pass_array[i]:
            dvojic+= 1
            last_char = None
        else:
            last_char = pass_array[i]
    return dvojic > 1
        
def invalid_password(pass_array):
    test1 = valid_test1(pass_array)
    test2 = valid_test2(pass_array)
    test3 = valid_test3(pass_array)
    
    #print(test1,test2,test3)
    return not test1 or not test2 or not test3

    
old_password = 'cqjxjnds'
old_password = 'cqjxxzaa'



print(f'Starting password: {old_password}')
password_array = [ord(char) for char in old_password]

while invalid_password(password_array):
    get_next_password(password_array,len(password_array)-1)
print(''.join([chr(char) for char in password_array]))

#print(chr(ord(old_password[0])-1))
#old_password_array[0] = 1