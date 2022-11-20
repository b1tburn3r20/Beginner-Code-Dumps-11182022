import string
import secrets

def pswgen(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
        
    if uppercase:
        combination += string.ascii_lowercase
    
    combination_length = len(combination)
    
    new_psw = ''
    
    for _ in range(length):
        new_psw+=combination[secrets.randbelow(combination_length)]
    return new_psw

print(pswgen(length= 20, symbols= True, uppercase= True))
    
    
