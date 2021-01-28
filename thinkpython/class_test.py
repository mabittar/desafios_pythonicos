"""
o objetivo desse exemplo é entender um pouco mais sobre POO e suas variações.
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
"""


class Employee():

    # contando número de empregados
    num_of_empls = 0
    # 3. iremos criar uma variável que reajusta os salários
    total_raise = 0.025
    #    pass
    # conforme comentado no 1. iremos criar a instância para receber os argumentos

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay

        # acrescendo o numero de empregados
        Employee.num_of_empls += 1

# iremos criar um método para garantir as letras minúsculas do email
#        self.mail = name + '.' + last + '@test.com'

    def fullname(self):
        name = self.name.capitalize()
        last = self.last.capitalize()
        return '{} {}'.format(name, last)

    def mail(self):
        name = self.name.lower()
        last = self.last.lower()
        mail = name + '.' + last + '@test.com'
        return mail

    def apply_raise(self):
        self.pay = float(self.pay * (1 + self.total_raise))

    @classmethod
    def set_raise_amt(cls, amt):
        cls.total_raise = amt


# 2. Agora que a classe está configurada para receber os argumentos podemos passá-los diretamente
# emp_1 = Employee()
# emp_2 = Employee()

emp_1 = Employee('eme', 'bi', 5000)
emp_2 = Employee('user', 'test', 3500)

# pode-se observar que cada emp é um objeto diferente, com atribuição em memória em locais distintos.
print("Tipo do Objeto e alocação do emp_1: ", emp_1)
print("Tipo do Objeto e alocação do emp_1: ", emp_2)

# 1. essa seria uma forma lenta e não pythonica para inserção dos dados em cada classe.
# A forma pythonica seria criar dentro da classe uma instância para receber os atributos
# emp_1.name = 'eme'
# emp_1.last = 'bi'
# emp_1.mail = 'eme.bi@test.com'
# emp_1.pay = 5000

# emp_2.name = 'teste'
# emp_2.last = 'user'
# emp_2.mail = 'teste.user@test.com'
# emp_2.pay = 3000

# 3. para acessar o método é necessário inserir os (), se não estamos acessando o atributo.
print(emp_1.mail())
print(emp_2.fullname())

print(emp_1.__dict__)

# valor de pagamento inserido
print(emp_1.pay)

Employee.set_raise_amt(0.1)

# criando o aumento no salário
emp_1.apply_raise()
# novo valário de salárrio
print(emp_1.pay)
# print("Novo salario com aumento: {}". format(emp_1.pay))

# imprimindo o número de empregados
print("Empregados registrados: ", Employee.num_of_empls)

# podemos ainda indicar o aumento apenas para um funcionário
emp_2.set_raise_amt(0.05)
print(emp_2.total_raise)
print(emp_1.total_raise)
