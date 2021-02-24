from re import match, search, findall

m = match(r'\d+', '12345')
# retorna a classe do objeto
print(type(m))

# retorna os valores encontrados, o que ele fez match
print(m.group())

# retorna a primeira posição encontrada, onde ele começou encontrando
print(m.start())

# retorna a última posição enconrtada, onde ele  terminou de encontrar
print(m.end())

# retorna uma tupla com start e end
print(m.span())
