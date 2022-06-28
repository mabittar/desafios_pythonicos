from re import match, search, findall

#  quantidades especificas

# solicitando encontrar quantidade exata (4) com a utilização de {}

print(match(r'\d{4}', '1234'))
print(match(r'\d{4}', '12345'))
print(match(r'\d{4}', '123'))

# solicitando encontrar quantidade minima de (2) com a utilização de {}

print(match(r'\d{2,}', '1234'))
print(match(r'\d{2,}', '12345'))
print(match(r'\d{2,}', '1'))

# solicitando encontrar somente os (3) primeiros
# a ? transforma a repetição de gulosa para preguiçosa
print(match(r'\d{3,}?', '1234'))

# solicitando encontrar minima de (2) e máximo (4)
print(match(r'\d{2,4}', '12345'))
print(match(r'\d{2,4}', '123'))
print(match(r'\d{2,4}', '12'))
print(match(r'\d{2,4}', '1'))

# s0 ou 1 ocorrência
print(match(r'\d{0,1}', '12345'))
print(match(r'\d{0,1}', '1'))
print(match(r'\d{0,1}?', '123'))

#  0 ou mais ocorrências
print(match(r'\d{0,}', '12345'))
print(match(r'\d{,}', '12345'))
# o * indica que está buscando o anterior 0 ou mais vezes
print(match(r'\d*', '12345'))
print(match(r'\d*?', '12345'))

# 1 ou mais ocorrências
print(match(r'\d{1,}', '12345'))
print(match(r'\d+', '12345'))
print(match(r'\s+', '12345'))
print(match(r'\d+', 'abc'))

# diferença entre pesquisa gulosa e preguiçosa
text = 'attr1="valor1" attr="valor2"'

# buscando apenas o valor dos atributos que está entre ""
print(findall(r'".+"', text))
print(findall(r'".+?"', text))
# entretanto o + exige 1 ou mais ocorrências e no caso de um valor vazio?
text = 'attr1="" attr=""'
print(findall(r'".+?"', text))
# o * garante que sejam 0 ou mais ocorrências
print(findall(r'".*?"', text))
