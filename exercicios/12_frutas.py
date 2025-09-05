# %%

frutas = {
    'Maçã': 1.50,
    'Banana': 2.75,
    'Uva': 1.90,
    'Pera': 1.25,
    'Laranja': 0.65,
    'Limão': 1.25,
    'Goiaba': 2.15,
    'Abacaxi': 3.20,
    'Jaca': 5.80,
}

fruta = input('Entre com o nome da fruta: ').capitalize().strip()

# verifica se a fruta está na lista e exibe o valor se verdadeiro

if fruta in frutas:
    print(f'{fruta} -> R${frutas[fruta]:.2f}')

else:
    print(f'{fruta} não está na lista!')

