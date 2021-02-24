from re import match, search, findall

# utiliza-se o  | para o comando ou

print(match('a|b', 'abc'))
print(match('a|b', 'bcd'))
print(match('a|b', 'cde'))