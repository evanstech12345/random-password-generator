import random


letter_list = 'abcdefghijklmnopqrstuvwrxyz'

def password_gen():
    
    start = input('would you like to generate a password[y/n]:>>>')
    if start == 'n':
        print('ok, come back later!')
    else:
        random_password = []
        print(start)
        for x in range(10):
            random_password.append(random.choices(letter_list)[0])
            # newcharacter = random.choices(letter_list)[0]
            # random_password += newcharacter            
        print(''.join(random_password))
        
  
password_gen()
    