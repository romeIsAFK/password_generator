# Import modules
import random
import string

# Program says hello!
print(
    '\nHello! Welcome to Password Generator!\n'
)

# Print Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Define characters
lowerLetters = string.ascii_lowercase
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Other definitions
def complexityHelp():
    print(f'\n{bcolors.OKBLUE}Simple passcode: 5 randomized lowercased letters + 3 digits. Total length: 8 characters.\nComplex passcode: Mix of lowercase letters, uppercase letters, digits, and special characters. Program will ask user for length of passcode.{bcolors.ENDC}')

def pinCode():
    temp = random.sample(digits,4)
    pincode = ''.join(temp)
    print(f'{bcolors.OKGREEN}\nPincode: {pincode}\n{bcolors.ENDC}')
    exit()

def simplePass():
    passSetup = lowerLetters + digits
    temp = random.sample(lowerLetters,5)+random.sample(digits,3)
    passCode = ''.join(temp)
    print(f'{bcolors.OKGREEN}\nPincode: {passCode}\n{bcolors.ENDC}')

# Main function
def main():
    options = {
        '1':'Generate Pincode',
        '2':'Generate Passcode',
        '3':'Exit'
    }

    complexity ={
        '1':'Simple Passcode',
        '2':'Complex Passcode',
        '3':'Help'
    }
    
    choice = 0
    while not choice in range(1,4):
        try:
            for key in options:
                print(f'\n{bcolors.BOLD}{key}:{options[key]}{bcolors.ENDC}')

            choice = int(input('\nEnter your choice:'))

            if choice == 1 or choice == 2:
                break
            if choice == 3:
                break
                exit()
        except:
                    print('\nInvalid input. Please enter an integer from 1 to 3.\n')
    
    if choice == 1:
        pinCode()
    if choice == 2:
        complexity_choice = 0
        while not complexity_choice in range(1,4):
            try:
                for key in complexity:
                    print(f'\n{bcolors.BOLD}{key}:{complexity[key]}{bcolors.ENDC}')

                complexity_choice = int(input('\nEnter your choice:'))

                if complexity_choice >= 1 and complexity_choice < 4 and complexity_choice != 3:
                    break
                elif complexity_choice == 3:
                    complexityHelp()
                    complexity_choice = 0
                    continue
                else:
                    print('\nInvalid input. Please enter an integer from 1 to 3.\n')
            except:
                    print('\nInvalid input. Please enter an integer from 1 to 3.\n')
    
    match complexity_choice:
        case 1:
            simplePass()
main()