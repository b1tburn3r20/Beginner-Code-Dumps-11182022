import string
import secrets

def pswgen(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.punctuation
    
    if symbols:
        combination += string.punctuation
        
    if uppercase:
        combination += string.ascii_lowercase
        
    combination_length = len(combination)
    
    new_pwd = ''
    
    for _ in range(length):
        new_pwd+=combination[secrets.randbelow(combination_length)]
    return new_pwd

print(pswgen(length=15, symbols=True, uppercase= True))
        
