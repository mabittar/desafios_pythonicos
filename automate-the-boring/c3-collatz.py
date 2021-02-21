# Source: Automate the Boring stuff with python Ch. 3 Project

def collatz(number):
    """Esta conjectura aplica-se a qualquer número natural inteiro, 
    e diz-nos para, se este número for par, o dividir por 2 (/2), e se for impar, 
    para multiplicar por 3 e adicionar 1 (*3+1). Desta forma, por exemplo, 
    se a sequência iniciar com o número 5 ter-se-á: 5; 16; 8; 4; 2; 1. 
    A conjectura apresenta uma regra dizendo que, qualquer número natural inteiro, 
    quando aplicado a esta regra, eventualmente sempre chegará a 4, que se converte em 2 e termina em 1.

    Args:
        number (inteiro)
    """
    if (number % 2) == 0:
        print(number // 2)
        return number // 2

    print(3 * number + 1)
    return (3 * number + 1)


if __name__ == '__main__':
    try:
        num = int(input('Entre com um número inteiro maior que 0: '))
        out = collatz(num)
        while (out != 1):
            out = collatz(out)

    except ValueError:
        print('Entre com um número inteiro maior que 0!')
