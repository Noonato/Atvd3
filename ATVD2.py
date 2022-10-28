A =int(input('Informe o valor de A:'))
B = int(input('Informe o valor de B:'))
C = int(input('Informe o valor de C:'))

altura =(A+B+C)/2
areaA=0
areaB=0
areaC=0



if(A>=B+C):
    print(f'Não é possivel formar um triangulo\n Valores lidos:\nA:{A}\nB:{B}\nC:{C}')
else:
    areaA=(altura *A)/2
    print(f'Forma um triangulo, e caso a base for A"{A}" sua área é:{areaA}:')
    areaB=(altura *B)/2
    print(f'Forma um triangulo, e caso a base for B"{B}" sua área é:{areaB}:')
    areaC=(altura *C)/2
    print(f'Forma um triangulo, e caso a base for C"{C}" sua área é:{areaC}:')
    
    


    
        
        
    

    
