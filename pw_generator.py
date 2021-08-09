# basic random password generator

import random
import string

password = ''
pw_characters = string.ascii_letters + string.digits

for i in range(12):
    password += random.choice(pw_characters)

print(password)