import secrets
import string

def genpsw(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_lowercase
        
    newpwd = ''
    
    combination_length = len(combination)
    
    for _ in range(length):
        newpwd+=combination[secrets.randbelow(combination_length)]
    return newpwd

print(genpsw(length=20, symbols= True, uppercase= True))