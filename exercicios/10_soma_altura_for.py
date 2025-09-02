# %%
soma = 0

for i in range(4):
    altura = input(f'Digite a altura da {i + 1}ª pessoa: ').replace(',','.')
    altura = float(altura)

    soma += altura
print(f'A soma das alturas é {soma:.2f}m')