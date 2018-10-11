from calculator_menu_program import menu, functions

ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
MODULUS = 5
EXPONENT = 6
EXIT = 7

def main():
    print('+-*/%**+-*/%**+-*/%**+-*/%**')
    print('+-*/%**+-*/%**+-*/%**+-*/%**')
    print('Welcome to Simple Calculator')
    print('+-*/%**+-*/%**+-*/%**+-*/%**')
    print('+-*/%**+-*/%**+-*/%**+-*/%**')
    print()

    choice = 0

    while (choice != EXIT):

        menu.print_menu()

        #choice, op1, op2 = menu.get_input()
        choice = menu.get_choice()

        if choice == EXIT:
            break
        elif choice==-1:
            continue
        else:
            op1, op2 = menu.get_operands(choice)

            if (op1 == None):
                print('Error, try again.')
                print()
            else:
                if (choice==ADD):
                    ans = functions.add(op1, op2)
                    print(str(ans))
                    print()
                elif (choice==SUBTRACT):
                    ans = functions.subtract(op1, op2)
                    print(str(ans))
                    print()
                elif (choice==MULTIPLY):
                    ans = functions.multiply(op1, op2)
                    print(str(ans))
                    print()
                elif (choice==DIVIDE):
                    if (op2 ==0):
                        print('Error')
                    else:
                        ans = functions.divide(op1, op2)
                        print(str(ans))
                        print()
                elif (choice==MODULUS):
                    ans = functions.modulus(op1, op2)
                    print(str(ans))
                    print()
                elif (choice==EXPONENT):
                    ans = functions.exponent(op1, op2)
                    print(str(ans))
                    print()

    print('Thanks for using the calculator')

main()