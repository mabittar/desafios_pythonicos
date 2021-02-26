"""
O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.
As regras são as seguintes:

Pedra empata com Pedra e esmaga a Tesoura
Tesoura empata com Tesoura e corta o Papel
Papel empata com Papel e embrulha a Pedra
"""
import random


def jkp(jogador1, jogador2):
	if jogador1 == jogador2:
		return "empate"
	if jogador1 == 'pedra':
		if jogador2 == 'papel':
			return 'papel'
		return 'pedra'
	if jogador1 == 'tesoura':
		if jogador2 == 'pedra':
			return 'pedra'
		return 'tesoura'
	if jogador1 == 'papel':
		if jogador2 == 'tesoura':
			return 'tesoura'
		return 'papel'


# elementos = ['pedra', 'papel', 'tesoura']
# computador = str(random.choice(elementos))
#
# print("Vamos jogar Jokenpo, eu já escolhi...")
# print("Entre com o respectivo número 1 = Pedra ; 2 = Papel ; 3 = Tesoura")
# jogador_entrada = int()
# while jogador_entrada not in range(1, 4):
# 	try:
# 		jogador_entrada = int(input("Entre com um número entre 1 e 3: "))
# 	except ValueError:
# 		print("Número inválido!")
#
# jogador = str(elementos[jogador_entrada - 1])
# print("Eu escolhi {} e você escolheu {}....".format(computador, jogador))
# print("Quem ganhou foi.... \n {}".format(jkp(computador, jogador).upper()))


assert jkp('pedra', 'pedra') == 'empate'
assert jkp('tesoura', 'tesoura') == 'empate'
assert jkp('papel', 'papel') == 'empate'
assert jkp('pedra', 'papel') == 'papel'
assert jkp('pedra', 'tesoura') == 'pedra'
assert jkp('tesoura', 'pedra') == 'pedra'
assert jkp('tesoura', 'papel') == 'tesoura'
