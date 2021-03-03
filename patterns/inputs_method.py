"""
Muitas listas de exercícios de lógica de programação pedem em algum
momento que um valor seja lido do teclado, e caso esse valor seja inválido, deve-se avisar,
e repetir a leitura até que um valor válido seja informado
exemplo de: http://pythonclub.com.br/encapsulamento-da-logica-do-algoritmo.html
"""


# Solução 1
# valor = int(input('Entre com o valor de 0 a 10: '))
# while valor < 0 or valor >10:
# 	print('Valor inválido!')
# 	valor = int(input('Entre com o valor de 0 a 10: '))
# print("Você entrou com a valor: ", valor)
"""
Conforme podemos observar essa é uma maneira simples para contornar o problema, entranto estamos presos no loop.
"""

# Solução 2
# while True:
# 	try:
# 		valor = int(input('Entre com um valor de 0 a 10: '))
# 		if 0 <= valor <= 10:
# 			break
# 	except ValueError:
# 		pass
# 	print('Valor inválido!')
# print("Você entrou com o valor: ", valor)
"""
Dessa forma não existe mais a repetição dentro do loop
Porém esses algoritmos validam apenas o valor lido, apresentando erro caso seja informado um 
valor com formato inválido, como letras em vez de números. 
Isso pode ser resolvido tratando as exceções lançadas.
"""

# Solução 3
# def valor_input(n):
# 	while True:
# 		try:
# 			valor = int(input(n))
# 			if 0 <= valor <= 10:
# 				print(f'Você entrou com o valor: {valor}')
# 				break
# 		except ValueError:
# 			pass
# 		print("valor inválido! Digite um valor entre 1 e 10")
# 	return  valor
#
# valor = valor_input('Digite o valor: ')
"""
Nessa solução realizamos o encapsulamento da lógica em função.
"""

# Solução 4
class ValorValidoInput:
	msg_valor_invalido = "Valor Inválido. Digite um valor entre 1 e 10. "

	def ler_entrada(self, n):
		return input(n)

	def transforma_entrada(self, entrada):
		return int(entrada)

	def valida_valor(self, valor):
		return 0 <= valor <= 10

	def __call__(self, n):
		while True:
			try:
				valor = self.transforma_entrada(self.ler_entrada(n))
				if self.valida_valor(valor):
					print(f'Você entrou com: {valor}')
					break
			except ValueError:
				pass
			print(self.msg_valor_invalido)
		return  valor

valor_input = ValorValidoInput()
valor = valor_input('Digite o valor entre 1 e 10: ')
"""
é possível encapsulá-la em uma classe, o que permitiria separar cada etapa do algoritmo em métodos, 
assim como ter um método responsável por controlar qual etapa deveria ser chamada em qual momento
Vale observar que o método __call__ permite que o objeto criado a partir dessa classe seja chamado como se fosse uma função.
"""