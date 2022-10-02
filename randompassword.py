# Import modules
import random
import string

# Variables
menu_options = {
    1: 'Generate passcode',
    2: 'Generate pincode',
    3: 'Exit'
}

# definitions and functions
def print_menu():
    for key in menu_options.keys():
        print(key,'-', menu_options[key])

# Program says hello!
print('\nHello! Welcome to the Password Generator.\n')

option = 0
while not int(option) in range(1,4):
    try:
        print_menu()
        option = int(input('\nEnter your choice:'))
    except:
        print('\nWrong input, try again.\n')
