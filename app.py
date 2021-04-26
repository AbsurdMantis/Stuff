import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation    

def get_password_length():
    '''
      Retrieves the length of a password
      :returns number <class 'int'>
    '''
    length = input("How long do you want your password: ")
    return int(length)

def password_generator(length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified.
    :returns string <class 'str'>
    '''
    # create alphanumerical from string constants
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password
    # testing password generator with it's default length of 8
    password_one = password_generator()

    # testing password generator using user's input as length
    password_length = get_password_length()
    password_two = password_generator(password_length)

    print("password one (" + str(len(password_one)) + "):\t\t" + password_one )
    print("password one (" + str(len(password_two)) + "):\t\t" + password_two )