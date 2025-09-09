# %%

valor = 0
sorvete = ''
sabor = ''
cobertura = ''
while True:
    textoSorvete = '''
    Escolha o seu sorvete:
    [1] -> Casquinha: R$1.00
    [2] -> Cascão: R$2.50
    [3] -> Cestinha: R$4.00
    '''

    sorvete = int(input(textoSorvete))

    if sorvete == 1:
        valor = 1.00
        sorvete = 'Casquinha'
        break

    elif sorvete == 2:
        valor = 2.50
        sorvete = 'Cascão'
        break

    elif sorvete == 3:
        valor = 4.00
        sorvete = 'Cestinha'
        break

    else:
        print('Escolha a opção correta!')

    print()

while True:
    textoSabor = '''
    Escolha o sabor:
    [1] -> Morango
    [2] -> Creme
    [3] -> Chocolate
    '''

    sabor = int(input(textoSabor))

    if sabor == 1:
        sabor = 'Morango'
        break

    elif sabor == 2:
        sabor = 'Creme'
        break

    elif sabor == 3:
        sabor = 'Chocolate'
        break

    else:
        print('Escolha um sabor!')

    print()

while True:
    textoCobertura = '''
    [1] -> Caramelo: R$1.50
    [2] -> Morango: R$1.50
    [3] -> Chocolate: R$1.50
    [4] -> Sem cobertura R$0.00
    '''

    cobertura = int(input(textoCobertura))

    if cobertura == 1:
        valor += 1.50
        cobertura = 'Caramelo'
        break

    elif cobertura == 2:
        valor += 1.50
        cobertura = 'Morango'
        break
    
    elif cobertura == 3:
        valor += 1.50
        cobertura = 'Chocolate'
        break

    elif cobertura == 4:
        break

    else:
        print('Escolha uma opção válida!')

    print()

print(f'Sorvete: {sorvete}')
print(f'Sabor: {sabor}')
print(f'Cobertura: {cobertura}')
print(f'Valor a pagar: R${valor:.2f}')


# %%
