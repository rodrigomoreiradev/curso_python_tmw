# %%

texto = '''
Escolha a sua água:
[1] - Água Mineral R$1,50
[2] - Água Mineral com Gás R$2,50
'''

opt = input(texto)
conta = 0

if opt == '1':
    conta = 1.5

elif opt == '2':
      conta = 2.5
      

if conta == 0:
    print('Entre com a opção correta!')

else:
     print(f'Sua conta foi R${conta:.2f}')
# %%
