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
while (True):
    option = 0
    while 1 > option or 3 < option:
        try:
            print_menu()
            option = int(input('\nEnter your choice:'))
        except:
            print('\nWrong input, try again.\n')
