"""
Um fractal é um objeto geométrico que pode ser dividido em partes, cada uma das quais semelhante ao objeto original. 
Fractais são muito usados em arte gerada por computador. O objetivo deste exercício é fazer um programa em Python, 
usando funções recursivas, para gerar imagens (no formato PGM) com os desenhos de um fractal conhecido como Tapete de Sierpinski.

A construção do Tapete de Sierpinski parte de um quadrado, que é subdividido em nove partes. 
A parte central é removida, de modo que sobram então oito pequenos quadrados. Para cada um deles, é aplicado o mesmo processo de 
divisão em nove partes, retirando a parte central, e assim sucessivamente. Este processo pode ser repetido infinitamente, 
mas no contexto de imagens a repetição é feita até atingir um número máximo de iterações.
"""


def cria_matriz(m, n, val):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(val)
        matriz.append(linha)
    return matriz


def grava_figura(matriz, nomearquivo):
    arquivo = open(nomearquivo, "w")
    arquivo.write("P2\n")
    m = len(matriz)
    n = len(matriz[0])
    arquivo.write("%d %d\n" % (n, m))
    arquivo.write("255\n")
    for i in range(m):
        for j in range(n):
            arquivo.write(" %3d" % (matriz[i][j]))
        arquivo.write("\n")
    arquivo.close()


def tapete_sierpinski_aux(matriz, x1, y1, x2, y2, niveis):
    if niveis > 0:
        tam = x2-x1+1
        xa = x1 + tam//3
        xb = xa + tam//3
        ya = y1 + tam//3
        yb = ya + tam//3
        tapete_sierpinski_aux(matriz, x1, y1, xa-1, ya-1, niveis-1)
        tapete_sierpinski_aux(matriz, x1, ya, xa-1, yb-1, niveis-1)
        tapete_sierpinski_aux(matriz, x1, yb, xa-1, y2, niveis-1)
        tapete_sierpinski_aux(matriz, xa, y1, xb-1, ya-1, niveis-1)
        tapete_sierpinski_aux(matriz, xa, yb, xb-1, y2, niveis-1)
        tapete_sierpinski_aux(matriz, xb, y1, x2, ya-1, niveis-1)
        tapete_sierpinski_aux(matriz, xb, ya, x2, yb-1, niveis-1)
        tapete_sierpinski_aux(matriz, xb, yb, x2, y2, niveis-1)
        for i in range(ya, yb):
            for j in range(xa, xb):
                matriz[i][j] = 0


def tapete_sierpinski(n, niveis):
    M = cria_matriz(n, n, 255)
    tapete_sierpinski_aux(M, 0, 0, n-1, n-1, niveis)
    return M


def main():
    n = 3**6
    T = tapete_sierpinski(n, 5)
    grava_figura(T, "tapete.pgm")


main()
