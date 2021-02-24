# Classe de caracteres

# nessa estapa iremos explorar a parte ligada ao regex sobre classe de caracteres.

import re

frase = 'abc\n123abc\n456edf'
nome = 'Marcel Bittar'

# busca um caracter ou outro dentro dos []
out1 = re.findall('[aeiou]', frase)
out2 = re.findall('[aeiou]', nome)

# busca os caracter que não estão nos []
out3 = re.findall('[^aeiou]', frase)
out4 = re.findall('[^aeiou]', nome)  # aqui inclusive retorna o espaço

# busca os caracter que no range por exemplo de a até f
out5 = re.findall('[a-f]', frase)
out6 = re.findall('[a-f]', nome)  # apenas minúsculos
out7 = re.findall('[A-F]', nome)  # apenas maiúsculos

# sequênciias especiiais
# todos os caracteres aceitáveis inclusive _ [a-zA-Z0-9_]
out8 = re.findall('[\w]', nome)
# negação de todos os caracteres aceitáveis inclusive _ [^a-zA-Z0-9_]
out9 = re.findall('[\W]', nome)
# todos os números aceitáveis [0-9]
out10 = re.findall('[\d]', frase)
# negação de todos os números aceitáveis [^0-9]
out11 = re.findall('[\D]', frase)
# caracteres especiais [\t \n \r \f \v]
out12 = re.findall('[\s]', frase)
# negação dos caracteres especiais [\t \n \r \f \v]
out13 = re.findall('[\S]', frase)

# para imprimir as respostas
for i in range(1, 14):
    print(globals()['out'+str(i)])
