idade = int(input('Informe sua idade em dias: '))

anos = int(idade / 365)
meses = int(idade %365)/30
dias = (idade % 365)%30

print(f'Anos:{anos}\nMeses:{meses}\nDias:{dias}')
