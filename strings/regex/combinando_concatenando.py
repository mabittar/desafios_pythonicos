# combinando textos via geradores

def amostras():
    yield "Essa "
    yield "Sao Paulo "
    yield "não é "
    yield "Sao Paulo!"


# join simples
out = "".join(amostras())
print(out)

# redirecionando I/O
import sys
for amostra in amostras():
    sys.stdout.write(amostra)
sys.stdout.write('\n')

# Combinação de partes em buffers para Grandes I/O operações
def combine(fonte, maxsize):
    parts = []
    size = 0
    for part in fonte:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(amostras(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')