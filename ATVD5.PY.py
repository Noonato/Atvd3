import re

def inverte(F1):
    if re.match(r'^\w+$', F1):
        return F1[::-1]
    return F1

frase = str(input( 'Digite a frase: '))
invertida = ''.join(inverte(F1) for F1 in re.split(r'(\W+)', frase))
print(invertida)
