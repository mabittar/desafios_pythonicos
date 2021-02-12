from util import list_functions, hash_functions
# para utilizar esse import é necessário criar o arquivo __init__.py na pasta util


lista = [1, 2, 3, 4, 5, 9]
hs = {"first": 5, "second": 10}


print("O maior número da lista é: {}.".format((list_functions.get_max(lista))))
print("O menor número da lista é: {}.".format((list_functions.get_min(lista))))
print("A média da lista é: {}.".format((list_functions.get_avg(lista))))
print("A mediana da lista é: {}.".format((list_functions.get_median(lista))))

print("As chaves do dicionário são: {}".format(hash_functions.get_key(hs)))
print("O maior valor no dicionário é: {}".format(hash_functions.max_value(hs)))
print("O menor valor no dicionário é: {}".format(hash_functions.min_value(hs)))
