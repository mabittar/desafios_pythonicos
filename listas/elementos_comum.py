# encontre os elementos comuns entre dois dicionários

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print('Chaves comuns: ', a.keys() & b.keys())
print('Chave em a e não presente em b: ', a.keys() - b.keys())
print('(Chave, valor) comuns: ', a.items() & b.items())
