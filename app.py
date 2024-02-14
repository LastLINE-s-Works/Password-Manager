import os
import sys
import random
import string

def add_pass_logic():
    get_pass_name = input('Phrase: ')
    get_pass = input('Password: ')
    get_2fa = input('2FA Protection (Y/N): ')
    with open(f'data/{get_pass_name}-pass.txt','w') as f:
        pass
    with open(f'data/{get_pass_name}-pass.txt','r+') as f:
        old = f.read()
        f.write('Pass Phrase: ' +get_pass_name)
        f.write(' Password: ' +get_pass)
        f.write(' 2FA: '+get_2fa)

def read_pass_logic():
    get_phrase = input('Phrase: ')
    with open(f'data/{get_phrase}-pass.txt') as f:
        read = f.read()
        print(read)

def delete_pass_logic():
    get_phrase = input('Phrase: ')
    with open(f'data/{get_phrase}-pass.txt','w') as f:
         f.close()
         os.remove(f.name)

def generate_pass_logic():
    alphabets = input('Alphabets (y/n): ')
    integers = input('Integers (y/n): ')
    special_chr = input('Special Characters (y/n): ')
    if alphabets == 'y' and integers == 'y' and special_chr == 'y':
        all_characters = string.ascii_letters + string.digits + string.punctuation
        length = int(input("Enter the length of the password: "))
        password = ''.join(random.choices(all_characters, k=length))
        print('Your Generated Passaord is: ',password)
    if alphabets == 'n' and integers == 'n' and special_chr == 'n':
        print('Password Cant Be Generated')
    if alphabets == 'y' and integers == 'n' and special_chr=='n':
        all_characters = string.ascii_letters
        length = int(input('Enter the length of the password: '))
        password = ''.join(random.choices(all_characters,k=length))
        print('Your Generated Passaord is: ',password)
    if alphabets == 'n' and integers == 'y' and special_chr=='n':
        all_characters = string.digits
        length = int(input('Enter the length of the password: '))
        password = ''.join(random.choices(all_characters,k=length))
        print('Your Generated Passaord is: ',password)
    if alphabets == 'n' and integers == 'n' and special_chr == 'y':
        all_characters = string.punctuation
        length = int(input('Enter the length of the password: '))
        password = ''.join(random.choices(all_characters,k=length))
        print('Your Generated Passaord is: ',password)
    if alphabets == 'y' and integers == 'y' and special_chr=='n':
        all_characters = string.ascii_letters + string.digits
        length = int(input('Enter the length of the password: '))
        password = ''.join(random.choices(all_characters,k=length))
        print('Your Generated Passaord is: ',password)
    if alphabets == 'y' and integers=='n' and special_chr=='y':
        all_characters = string.ascii_letters + string.punctuation
        length = int(input('Enter the length of the password: '))
        password = ''.join(random.choices(all_characters,k=length))
        print('Your Generated Passaord is: ',password)
    if alphabets == 'n' and integers=='y' and special_chr=='y':
        all_characters = string.digits + string.punctuation
        length = int(input('Enter the length of the password: '))
        password = ''.join(random.choices(all_characters,k=length))
        print('Your Generated Passaord is: ',password)

print('a. Add Password: ')
print('b. Read Password: ')
print('c. Delete Password: ')
print('d. Generate Password: ')
print('')
greet = input('Select B/W: ')

if greet == 'a':
    add_pass_logic()

if greet == 'b':
    read_pass_logic()

if greet == 'c':
    delete_pass_logic()

if greet == 'd':
    generate_pass_logic()