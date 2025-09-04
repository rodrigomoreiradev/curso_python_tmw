# %%

# uma maneira de definir listas.
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)
# %%

rodrigo = ['Rodrigo','Moreira',35,False,'casado',2345.98]
print(rodrigo)
print(type(rodrigo))
print(len(rodrigo))

# %%

# acessar elementos.
print(rodrigo[2])

# renda
print(rodrigo[5])

# primerio indice
print(rodrigo[0])
# %%

# criando lista de idades
idades = [28, 42, 43, 35, 39, 28, 38, 42, 32]

# soma das idades
print(f'Soma das idades: {sum(idades)}')

# tamnho da lista
print(f'Tamanho da lista: {len(idades)}')

# média das idades 
print(f'Média das idades: {sum(idades) / len(idades):.2f}')

# menor idade
print(f'Menor idade: {min(idades)}')

# maior idade
print(f'Maior idade: {max(idades)}')

# %%

teo = [
    'Teo Calvo', 35, False, 'casado',
       ['estagiario','ds jr','ds pl','ds sr','head'],
       [4000,4500,6500,1000],
       ['Ana','Maria','Claudia']
    ]

print(teo[-1][-2])

# %%

# fatiamento (start: stop: step) <- onde começa, onde terminae número de passos.
# 4 primeiros elementos
print(teo[:4])

# 2 ultimas posições
print(teo[-3][-2:])
# %%

teo[-2][::-1]