# %%
arquivo = 'historia.txt'


#  abre arquivo em formato de leitura
open_file = open(arquivo)

# le os dados do arquivo
conteudo = open_file.read()

print(conteudo)

#  fecha o arquivo
open_file.close()
# %%

# melhor forma de abrir arquivos

arquivo = 'historia.txt'

with open(arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)
# %%
