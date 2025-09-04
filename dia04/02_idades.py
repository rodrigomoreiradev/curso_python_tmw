# %%
idades = []

while True:
    idade = input('Entre com a idade: ')
    
    if idade == '':
        break

    else:
        idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print('MEDIA',media)
print('MINIMO',minimo)
print('MAXIMO',maximo)
print('QTDE',qtde)

# %%
