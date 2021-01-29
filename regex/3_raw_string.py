from re import match

text = '\\section\n'

print(text)
# observe que o comando anteior retornou apenas '\section'

len(text)
# observe que o comando anteior contou as duas barras

#erro - retorna vazio
print(match('\\section', text))

# encontra o objeto - é necessário passar pois aqui mistrura o algo do python com o RegEx
print(match('\\\\section', text))

print(match(r'\\section', text))