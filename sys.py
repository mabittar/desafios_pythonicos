import sys
import pandas as pd

print(sys.version)
print(sys.executable)


def comprimentar(quem):
    comprimento = "Ola {}!".format(quem)
    return comprimento


print(comprimentar("Mundo"))
print(comprimentar("Marcel"))
