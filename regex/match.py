import re
# metacaracteres: . (qq carácter), ^ (início da string), $ (fim da string)
frase = 'abc123abc456edf'


out1 = re.match('abc', frase)
out2 = re.search('abc', frase)
out3 = re.findall('abc', frase)

out4 = re.match('.', frase)
out5 = re.search('.', frase)
out6 = re.findall('.', frase)

out7 = re.findall('^.', 'abc\nedf\nhij')
out8 = re.findall('^.', 'abc\nedf\nhij', re.MULTILINE)

out9 = re.findall('.$', 'abc\nedf\nhij')
out10 = re.findall('.$', 'abc\nedf\nhij', re.MULTILINE)
# observer que volta o valor encontrado em duas linhas.
out11 = re.findall('^$', '\n', re.MULTILINE)

for i in range(1, 12):
    print(globals()['out'+str(i)])
