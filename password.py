import string
import secrets

num = string.digits
letters = string.ascii_letters
char = string.punctuation

alphabet = num + letters + char

pwd_length = 13

pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print(pwd)