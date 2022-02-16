# Defind python user defined exceptions

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmall(Exception):
    """Raised where value too small"""
    pass

class ValueTooLarge(Exception):
    """Raised where value too large"""
    pass
#you need to guess number
number=10

#user guesses a number until he/she right

while True:
    try:
        userGuess=int(input("Enter number"))
        if number==userGuess:
            print("Congrulations your guess is correct")
        elif userGuess<number:
            raise ValueTooSmall
        elif userGuess>number:
            raise ValueTooLarge
        else:
            print("Invalid input")
        break
    except ValueTooSmall:
        print("This value is too small")
        print()
    except ValueTooLarge:
        print("This value is too large")
        print()
