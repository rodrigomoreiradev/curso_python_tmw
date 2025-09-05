# %%

# Dicionários são pares de chave:valor

dados_teo = {
    'nome':'Teo',
    'sobrenome':'Calvo',
    'filhos':True,
    'formacao':['estatistica', 'bigdata datascience'],
    'cargos':[
        {'nome':'estagiario','empresa':'taaps'},
        {'nome':'ds jr','empresa':'sas'},
        {'nome':'ds pl','empresa':'biticario'},
        {'nome':'ds sr','empresa':'via varejo'},
    ],
}

print(dados_teo)

# %%

dados_teo['estado civil'] = 'solteiro'

print(dados_teo['nome'])
print(dados_teo['formacao'][-1])

# %%
print(dados_teo['cargos'][-1]['empresa'])

# %%

# criando nova chave para o dicionário

dados_teo['estado civil'] = 'casado'

print(dados_teo)

# %%

# decobrindo chaves do dicionário

chave = dados_teo.keys()
print(f'Chaves -> {chave}')

print('---'* 30)

# descobrindo os valores
valores = dados_teo.values()
print(f'Valores -> {valores}')

print('---'* 30)

# trazer chave e valor <- retorna uma tupla com chave e valor.
itens = dados_teo.items()
print(f'Itens -> {itens}')
# %%

# percorrendo dicionários

for i in dados_teo:
    print(i,'->',dados_teo[i])

# %%
for chave,valor in dados_teo.items():
    print(chave,'->',valor)
    