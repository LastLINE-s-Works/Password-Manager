import os
import sys
import random

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

print('a. Add Password: ')
print('b. Read Password: ')
print('c. Delete Password: ')
print('')
greet = input('Select B/W: ')

if greet == 'a':
    add_pass_logic()

if greet == 'b':
    read_pass_logic()

if greet == 'c':
    delete_pass_logic()