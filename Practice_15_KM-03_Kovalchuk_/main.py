from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm
import sys


def better1_input():
    try:
        return float(input('> '))
    except:
        print('Oops. Valid characters are real numbers. Try again!')
        return better1_input()


def better3_input(number):
    flag = True
    try:
        while flag:
            number = int(input())
            if number > 0:
                return int(number)
            else:
                print("Oops! Valid characters are natural numbers. Try again!")
    except:
        print("Oops! Valid characters are natural numbers. Try again!")
        return better3_input(number)


def better4_input(number):
    flag = True
    try:
        while flag:
            number = int(input())
            if 0 < number < 9:
                return int(number)
            else:
                print("Oops! Valid characters are integers from 1 to 8. Please try again!")
    except:
        print("Oops! Valid characters are integers from 1 to 8. Please try again!")
        return better4_input(number)


def better5_input(number):
    flag = True
    try:
        while flag:
            number = float(input())
            if number > 0:
                return float(number)
            else:
                print("Oops! Valid characters are integers. Try again!")
    except:
        print("Oops! Valid characters are integers. Try again!")
        return better5_input(number)


def better6_input(number):
    flag = True
    try:
        while flag:
            number = float(input())
            if number > 1:
                return float(number)
            else:
                print("Oops! Valid characters are positive integers except 1. Try again!")
    except:
        print("Oops! Valid characters are positive integers except 1. Try again!")
        return better6_input(number)


def main():
    print(20 * '-')
    print('1 - factorial number. 2 - square numbers. 3 - cube number. 4 - square root of a number.'
          '5 - the root of the third power of a number. 6 - logarithm of a number. '
          '7 - natural logarithm of the number. 8 - decimal logarithm of the number')
    ans = 0
    ans = better4_input(ans)
    print(20 * '-')
    if ans == 1:
        n = 0
        print('Enter a natural number:')
        n = better3_input(n)
        print(f"Factorial of {n} is {factorial.fac(n)}")
    elif ans == 2:
        print('Enter a valid number:')
        n = better1_input()
        print(f"Square of {n} is {exponentiation.exp2(n)}")
    elif ans == 3:
        print('Enter a valid number:')
        n = better1_input()
        print(f"Cube of {n} is {exponentiation.exp3(n)}")
    elif ans == 4:
        n = 0
        print('Enter a positive number:')
        n = better5_input(n)
        print(f"Square root of {n} is {root.root2(n)}")
    elif ans == 5:
        n = 0
        print('Enter a positive number:')
        n = better5_input(n)
        print(f"Cube root of {n} is {root.root3(n)}")
    elif ans == 6:
        a = 0
        b = 0
        print('Enter the base of the logarithm:')
        a = better6_input(a)
        print('Enter a positive number:')
        b = better5_input(b)
        print(f"Logarithm of {b} to {a} is {logarithm.log(a, b)}")
    elif ans == 7:
        b = 0
        print('Enter a positive number:')
        b = better5_input(b)
        print(f"Natural logarithm of {b} is {logarithm.ln(b)}")
    else:
        b = 0
        print('Enter a positive number:')
        b = better5_input(b)
        print(f"Decimal logarithm of {b} is {logarithm.lg(b)}")
    print(20 * '-')
    print('Do you want to continue? Yes - any key. No- "no"')
    ans_2 = input()
    if ans_2 == 'no':
        sys.exit()
    else:
        main()


main()
