# %%

texto = '''
Escolha a sua água:
[1] - Água Mineral R$1,50
[2] - Água Mineral com Gás R$2,50
'''

opt = input(texto)

valor_item = 0

if opt == '1':
    valor_item = 1.5 

elif opt == '2':
      valor_item = 2.5 

if valor_item == 0:
    print('Entre com a opção correta!')

else:
    qtd = input('Quantas Garrafas? ')
    qtd = int(qtd)
    conta = valor_item * qtd
    print(f'Sua conta foi R${conta:.2f}')
    
# %%
