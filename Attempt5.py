import secrets
import string

def genpwd(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits
    
    if symbols: 
        combination += string.punctuation
    
    if uppercase: 
        combination += string.ascii_lowercase
    
    combination_length = len(combination)
        
    newpwd=''
    
    for _ in range(length):
        newpwd+=combination[secrets.randbelow(combination_length)]
    return newpwd

print(genpwd(length=15, symbols=True, uppercase=True))