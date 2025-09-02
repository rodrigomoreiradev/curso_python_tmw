count = 1
soma = 0

while count <= 4:
    altura = input(f'Digite a altura da {count}ª pessoa: ').replace(',','.')
    altura = float(altura)

    soma += altura

    count +=1

print(f'A soma das alturas é {soma}m')