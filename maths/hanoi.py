"""
São dados um conjunto de n discos com diferentes tamanhos e três bases A, B e C.

O problema consiste em imprimir os passos necessários para transferir os discos da 
base A para a base B, usando a base C como auxiliar, nunca colocando discos maiores 
sobre menores.
"""


def hanoi(n, orig, dest, aux):
    if n == 1:
        print("Mover de {} para {}.".format(orig, dest))
    else:
        hanoi(n-1, orig, aux, dest)
        print("Mover de {} para {}.".format(orig, dest))
        hanoi(n-1, aux, dest, orig)


def main():
    n = int(input("Digite a quantidade de discos: "))
    hanoi(n, "A", "B", "C")


main()
