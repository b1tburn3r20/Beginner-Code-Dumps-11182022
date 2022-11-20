import secrets
import string

def pwdgen(length: int, symbols: bool, uppercase: bool):
    
    combination = string.ascii_lowercase + string.digits
    
    if symbols: 
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_lowercase
    
    new_pwd = ''
    
    for _ in range(length):
        new_pwd+= combination[secrets.randbelow(combination_length)]
    return new_pwd
    

    combination = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
        
    if uppercase:
        combination += string.ascii_lowercase
        
    combination_length = len(combination)
    
    new_pwd = ''
    
    for _ in range(length):
        new_pwd+=combination[secrets.randbelow(combination_length)]
    return new_pwd
    
    for _ in range(length):
        new_pwd+=combination[secrets.randbelow(combination_length)]
    return new_pwd
    
print(pwdgen(length=20, symbols=True, uppercase=True))