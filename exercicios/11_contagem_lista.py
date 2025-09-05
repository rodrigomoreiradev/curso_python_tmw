# %%

numeros = [1,2,3,4,5,6,3,4,7,3,1,6,8,5,3,2,1]
cont = 0

num = input('Entre com um número: ')
num = int(num)

for n in numeros:
    if n == num:
        cont += 1

print(f'O número "{num}", apareceu {cont} vezes!')

# %%
