# %%

a = 1 
b = 5

print(a)
print(b)
# %%

c = a
a = b
b = c

print(a)
print(b)

# %%

a,b = b,a

print(a)
print(b)
# %%

b,a ,*_= 1,2,3,4121,454545,454,545445545
print(a,b,_)


a,*_,b = 1,2,3,4121,454545,454,545445545
print(a,b,_)
# %%

dados = {'nome':'teo','sobrenome':'calvo'}
for i,j in dados.items():
    print(i,j)
# %%
def soma(a, *args):
    total = a + sum(args)
    return  total

soma(1,2,3,4)

# %%
def soma_quatro(a,b,c,d):
    return a + b + c + d

valores = [1,2,3,4]

soma_quatro(*valores)

