"""
Robo FizzBuzz
 1. Para todo número múltiplo de 3: retornar Fizz
 2. Para todo número múltiplo de 5: retornar Buzz
 3. Para todo número múltiplo de 3 e 5: retornar FizzBuzz
 4. Caso não obdeça as condições anteriores retornar o número

"""
import unittest


def robot(n):
    out = ("Fizz"*(n % 3 == 0)+"Buzz"*(n % 5 == 0) or str(n))
    return out

# robot(3)


class FizzBuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_Fizz_when_3(self):
        self.assertEqual(robot(3), 'Fizz')

    def test_say_Buzz_when_5(self):
        self.assertEqual(robot(5), 'Buzz')

    def test_say_FizzBuzz_when_15(self):
        self.assertEqual(robot(15), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     assert robot(1) == '1'
#     assert robot(2) == '2'
#     assert robot(3) == 'Fizz'
#     assert robot(5) == 'Buzz'
#     assert robot(15) == 'FizzBuzz'
