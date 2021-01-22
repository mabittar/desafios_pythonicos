from math import pi
import unittest


def esf_volume(r):
    vol = round(((4/3)*pi*r**3), 0)
    return vol


# r = float((input("Entre com o raio para calcular o volume: ")))

# print(esf_volume(r))

### -- TEST BLOCK -- ###
class esf_volumeTest(unittest.TestCase):
    def test_say_4_when_1(self):
        self.assertAlmostEqual(esf_volume(1), 4)

    def test_say_34_when_2(self):
        self.assertAlmostEqual(esf_volume(2), 34)

    def test_say_113_when_3(self):
        self.assertAlmostEqual(esf_volume(3), 113)

    def test_say_268_when_4(self):
        self.assertAlmostEqual(esf_volume(4), 268)


if __name__ == '__main__':
    unittest.main()
