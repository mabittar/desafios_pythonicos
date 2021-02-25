"""
https://docs.python.org/pt-br/3/tutorial/classes.html

Classes proporcionam uma forma de organizar dados e funcionalidades juntos. 
Criar uma nova classe cria um novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. 
Cada instância da classe pode ter atributos anexados a ela, para manter seu estado. 
Instâncias da classe também podem ter métodos (definidos pela classe) para modificar seu estado.

Uma classe defini o comportamento de um objeto e a natureza dos dados que ela armazena.
A informação de uma classe é armazenada em seus atributos e funções que pertencem a essa classe são chamadas de métodos.
Uma subclasse herda os atributos e métodos da classe superior.
"""

class Dog():
    """ representa um cachorro. """
    def __init__(self, name):
        """Inicializa o objeto cachorro

        Args:
            name (str): nome do cachorro
        """
        self.name = name

    def sit(self):
        """simula o ato de sentar do cachorro
        """
        print(self.name + " sentado!")

# Herança
class Feed_Dog(Dog):
    def __init__(self, name):
        """inicializa a alimentação do cachorro

        Args:
            name ([type]): [description]
        """
        super().__init__(name)

    def feed(self):
        print("Vamos comer {}.".format((self.name)))

snoop = Dog("Snoop")
racao = Feed_Dog("Purina")

print(f'{snoop.name} come {racao.name}, uma boa ração!')
snoop.sit()
racao.feed()
