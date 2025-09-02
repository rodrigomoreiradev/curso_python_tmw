# %%
nome = 'Rodrigo Moreira'

for letra in nome:
    print(letra)
    
# %%

numero = 2

for i in range(1,101):
    print(f'{i} x {numero} = {i * numero}')

print('FIM!')
# %%

for i in range(4,101):
    if i % 4 == 0:
        print(i)