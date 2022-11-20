import secrets
import string
#define the password generator
def pswgen(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits 
    
    if symbols:
        combination += string.punctuation
        
    if uppercase:
        combination += string.ascii_lowercase
        
    combination_length = len(combination)

    new_psw = ''

    for _ in range(length): 
        new_psw += combination[secrets.randbelow(combination_length)]
    return new_psw
#give rules to the pswgenerator
print(pswgen(length = 15, symbols = True, uppercase = True ))
#print the gen