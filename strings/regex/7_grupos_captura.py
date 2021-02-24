from re import match, search, findall

html = '<input type="text" id="id_cpf" name="name_cpf">'

# obtendo o nome da tag
# indica que o grupo de captura contém qualquer caracter antes de um espaço
pattern = r'<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"'

m = match(pattern, html)
print(m)

print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(2, 1, 3))


html2 = '<input  id="id_cpf" type="text" name="name_cpf">'
# o ?P<> é exclusivo do python e serve para nomear os grupos
# foram acrescidos (?:) duas vezes de forma a indicar que a posiçõo dos elementos não importa e * no final
pattern2 = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"| id="(?P<id>.+?)" | name="(?P<name>.+?)") ?)*'

m2 = match(pattern, html2)
m3 = match(pattern2, html2)

print(m2)
print(m3)

# retorna o valor capturado
print(m3.groups())
# retorna a chave e o valor capturados
print(m3.groupdict())
