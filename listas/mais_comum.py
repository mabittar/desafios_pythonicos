# determina o elemento mais comum em uma lista

palavras = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
conta_palavras = Counter(palavras)
top_three = conta_palavras.most_common(3)
for k,v in top_three:
    print("palavra: {} repetições: {} \n".format(k, v))
