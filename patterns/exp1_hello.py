# junte as palavras utilizando marcadores


# modo 1 - sem padrão
lista = ['hello', 'say', 'yes']
print("." + lista[0] + "." + lista[1] + "." + lista[2])


# modo 2 - passo 1
out = ""
for i in range(len(lista)):
    out += ("." + lista[i])

print(out)

# modo 3 - utilizando padrões
DELIMITER = "."
print(DELIMITER+DELIMITER.join(lista))
# agora é possível trocar o delimitador apenas em uma variável
