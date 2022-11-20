#imports for password
import secrets
import string

#define the alphabet
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

alphabet = letters + digits + punctuation

#decide how many characters is the password

pwdl = 12

#password string

#pwd = ''
#for i in range(pwdl):
#    pwd += ''.join(secrets.choice(alphabet))

#print(pwd)

#print password constraints

while True:
    pwd = ''
    for i in range(pwdl):
        pwd += ''.join(secrets.choice(alphabet))
    if(any(char in punctuation for char in pwd) and sum(char in digits for char in pwd)>=2):
        break

print(pwd)