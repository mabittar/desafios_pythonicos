"""
o objetivo desse exemplo é entender um pouco mais sobre POO e suas variações.
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
"""


class Employee():
    #    pass
    # conforme comentado no 1. iremos criar a instância para receber os argumentos
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
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
# 2. Agora que a classe está configurada para receber os argumentos podemos passá-los diretamente
# emp_1 = Employee()
# emp_2 = Employee()


emp_1 = Employee('eme', 'bi', 5000)
emp_2 = Employee('user', 'test', 3500)

# pode-se observar que cada emp é um objeto diferente, com atribuição em memória em locais distintos.
print(emp_1)
print(emp_2)

# 1. essa seria uma forma lenta e não pythonica para inserção dos dados em cada classe.
# A forma pythonica seria criar dentro da classe uma instância para receber os atriutos
# emp_1.name = 'eme'
# emp_1.last = 'bi'
# emp_1.mail = 'eme.bi@test.com'
# emp_1.pay = 5000

# emp_2.name = 'teste'
# emp_2.last = 'user'
# emp_2.mail = 'teste.user@test.com'
# emp_2.pay = 3000

# 3. para acessar o método é necessário inserir os (), se não estamos acessando o atributo.
print(emp_2.mail())
print(emp_1.fullname())
