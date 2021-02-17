""" o objetivo desse capítulo é entender sobre o operador **if**

'//' - divisão pelo piso arrendondando para baixo 105 // 60 = 1
% - resto da divisão 3 % 2 = 1

"""

minutes = 105
print(minutes // 60)


resto = minutes % 60
print(resto)

# expressões booleanas
"""
x == y -> x é igual a y
x != y -> x não é igual a y
x >= y -> x é maior ou igual a y
...
"""
print(type(True))

# operadores lógicos
""" 
and, or ou not

n%2 ==0 or n%3==0 será verdadeiro se uma das igualdades forem atendidas
"""
x = 3

y = 2

if x < 0:
    pass

if x % 2 == 0:
    print("X é par")
else:
    print("X é ímpar")

if x == y:
    print('X é igual a Y')
else:
    if x < y:
        print('X  é menor que Y')
    else:
        print('X é maior que Y')

if 0 < x < 10:
    print('X é um número positivo com um dígito.')


# Recursividade

def contagem(n):
    if n <= 0:
        print('BOOOOOM!')
    else:
        print(n)
        contagem(n-1)


contagem(5)