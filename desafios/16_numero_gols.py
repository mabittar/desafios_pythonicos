""" 
Considere:
A equipe A jogou 4 partidas e marcou 0, 7, 5, 2 gols em cada partida respectivamente (equipeA = [0, 7, 5, 2]).
A equipe B jogou 3 partidas e marcou 6, 1 e 5 gols em cada partida respectivamente (equipeB = [6, 1, 5]).
Para cada partida da equipe B, calcule o número total de partidas em que a equipe A marcou menos ou a 
mesma quantidade de gols.

entradas:
4 // número de partidas da equipe A
0 // número de gols na primeira partida
7 // número de gols na segunda partida
5 // número de gols na terceira partida
2 // número de gols na quarta partida
3 // número de partidas da equipe B
6 // número de gols na primeira partida
1 // número de gols na segunda partida
5 // número de gols na terceira partida

saída esperada:
[3, 1, 3]

Descrição da Função
A função deve imprimir o array m de números inteiros positivos, um elemento por linha. 
Para cada elemento equipeB[i] selecione a quantidade de elementos em equipeA onde, 
equipeA[j] ≤ equipeB[i], 0 ≤ j < n e 0 ≤ i < m, na ordem dada.


Restrições conhecidas:
2 ≤ n, m ≤ 105
1 ≤ equipeA[j] ≤ 109, onde 0 ≤ j < n.
1 ≤ equipeB[i] ≤ 109, onde 0 ≤ i < m.
"""

def resultados(val):
    # entradas = []
    # entradas.append(val)
    entradas = val
 
    lengthA = entradas[0]
    lengthB = entradas[(lengthA+1)]
    equipeA = entradas[0:lengthA]
    equipeB = entradas[(lengthA+2):]

    return equipeA, equipeB

def compara(scores):
    """
    Para cada elemento de b conta a quantidade de elementos em A que são menores ou iguais
    Args:
        a ([array]): [número de gols marcados pela equipe A por partida]    
        b ([array]): [número de gols marcados pela equipe B por partida]
    """
    a = scores[0]
    b = scores[1]
    output = [sum(1 for x in a if x <= m) for m in b]
    return output


equipeA = [0, 7, 5, 2]
equipeB = [6, 1, 5]
entradas = [4, 0, 7, 5, 2, 3, 6, 1, 5]

print(resultados(entradas))

print(compara(resultados(entradas)))
