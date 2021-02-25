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


def resultados(scores):
    lengthA = scores[0]
    lengthB = scores[(lengthA+1)]
    equipeA = scores[0:lengthA]
    equipeB = scores[(lengthA+2):]

    return equipeA, equipeB


def compara(scores):
    return [sum(1 for x in scores[0] if x <= m) for m in scores[1]]


assert compara(resultados([1, 0, 1, 1])) == [1]
assert compara(resultados([4, 0, 7, 5, 2, 3, 6, 1, 5])) == [3, 1, 3]
