# Import modules
import random
import string

# Program says hello!
print(
    '\nHello! Welcome to a Password Generator!\n'
)

# Define characters
letters = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

# Other definitions
# def 

# Main
def main():
    options = {
        "1":"Generate Pincode",
        "2":"Generate Passcode",
        "3":"Exit"
    }
    
    choice = 0
    while choice < 1 or choice > 3:
        try:
            for key in options:
                print(f'{key}:{options[key]}')

            choice = int(input("\nEnter your choice:"))

            if choice == 1 or choice == 2:
                break
            elif choice == 3:
                exit()
            else:
                print("\nInvalid input. Please enter an integer from 1 to 3\n")
        except:
                if choice > 3:
                    print("\nInvalid input. Please enter an integer from 1 to 3\n")
main()