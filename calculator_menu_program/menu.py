ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
MODULUS = 5
EXPONENT = 6
EXIT = 7
def print_menu():
    print('Choose your option from the menu:')
    print()
    print('1. Add +')
    print('2. Subtract -')
    print('3. Multiply *')
    print('4. Divide /')
    print('5. Modulus %')
    print('6. Exponent ^')
    print('7. Exit ')
    print()

def get_choice():
    try:
        choice = int(input('Selection: '))
        print()
        while (choice < ADD or choice > EXIT):
            choice = int(input('Invalid choice, enter a valid menu option: '))
            print()
        return choice
    except ValueError:
        print('Invalid entry. Try again with number entries only.')
        print()
        return -1

def get_operands(choice):
    try:
        operand1 = float(input('Enter first operand: '))
        operand2 = float(input('Enter second operand: '))
        print()
        return operand1, operand2

    except ValueError:
        print('Invalid entry. Try again with number entries only.')
        print()
        return None, None


def get_input():
    try:
        choice = int(input('Selection: '))
        print()

        if (choice==EXIT):
            return choice, 1, 1

        else:
            operand1 = float(input('Enter first operand: '))
            operand2 = float(input('Enter second operand: '))

            while (choice < ADD or choice > EXIT):
                choice = int(input('Invalid choice, enter a valid menu option: '))
                print()

            if (choice==DIVIDE and operand2==0):
                while (operand2==0):
                    operand2 = float(input('Error: Cannot divide by zero. Enter a different operand: '))
                    print()
        return choice, operand1, operand2

    except ValueError:
        print('Invalid entry. Try again with number entries only.')
        print()
        return 0, 0, 0