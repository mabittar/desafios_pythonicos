"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from collections import Counter

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).


# realiza a leitura do arquivo e retorna lista de palavras em caixa baixa
def get_data(filename):
    with open(filename, 'r') as file:
        lista = file.read().split()
    return [palavras.lower() for palavras in lista]


# conta as palabras obtidas da função get_data e retorna dicionário de palavras e numero de repetições
def contador(filename):
    cnt = Counter()
    words = get_data(filename)
    for word in words:
        cnt[word] += 1
    return cnt


# recebe da função contador o dicionário e retorna os elementos ordenando pelas palabras
def print_words(filename):
    c = contador(filename)
    for k, v in sorted(c.items()):
        print(k, v)


# recebe da função contador o dicionário e retorna os elementos ordenando pelas ocorrências
def print_top(filename):
    c = contador(filename)
    top = c.most_common(20)
    for k, v in top:
        print(k, v)


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
