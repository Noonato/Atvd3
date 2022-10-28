N1 = int(input('Informe o primeiro número:'))
N2 = int(input('Digite o segundo valor:'))
N3 = int(input('Digite o terceiro valor:'))

if(N1<N3 and N1<N2):
    M = N1
if (N2 < N3 and N2 < N1):
    M = N2
if (N3 < N1 and N3 <N2 ):
    M = N3
print(f'O menor número digitado foi {M}')
