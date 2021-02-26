"""
Robo FizzBuzz
 1. Para todo número múltiplo de 3: retornar Fizz
 2. Para todo número múltiplo de 5: retornar Buzz
 3. Para todo número múltiplo de 3 e 5: retornar FizzBuzz
 4. Caso não obdeça as condições anteriores retornar o número

"""


def robot(n):
    out = (str("Fizz"*(n % 3 == 0))+str("Buzz"*(n % 5 == 0)) or str(n))
    return out

# robot(3)


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(3) == 'Fizz'
    assert robot(5) == 'Buzz'
    assert robot(15) == 'FizzBuzz'
