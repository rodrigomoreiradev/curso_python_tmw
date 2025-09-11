# %%

lista = []
for i in range(1,101):
    lista.append(i)

lista
# %%

# list comprehension

lista2 = [i for i in range(1,101)]
lista2
# %%

# lista aninhada

def eh_par(x):
    return x % 2 == 0

z = [eh_par(i) for i in range(1,101)]
z
# %%

w = [i for i in range(1,101) if eh_par(i)]
w
# %%
