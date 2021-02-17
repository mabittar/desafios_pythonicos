"""
Fermat's Last Theorem says that there are no integers a, b, and c such that
a^n + b^n = c^n
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters-a, b, c and n-and that checks to see if 
Fermat's theorem holds. If n is greater than 2 and it turns out to be true that 
a^n + b^n = c^n
the program should print, "Holy smokes, Fermat was wrong!" 

Otherwise the program should  print, "No, that doesn't work."


2. Write a function that prompts the user to input values for a, b, c and n,
converts them to integers, and uses check_fermat to check whether they 
violate Fermat's theorem.
"""


def fermat_check(a, b, c, n):
    if (a ** n) + (b ** n) == (c ** n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that does not  work')


def getInput():
    print("This program will test the fermat theorem. Please enter a, b, c and  n.")
    a = int(input("Entre com o primeiro número: \n"))
    b = int(input("Entre com o segundo número: \n"))
    c = int(input("Entre com a igualdade: \n"))
    n = int(input("Entre com a potencia número (maior que 2!): \n"))

    print(fermat_check(a, b, c, n))


getInput()
