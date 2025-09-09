# %%

from random import randint

numeroSorteio = randint(1,15)

# Verifica se o usuário entreou com um valor válido
def get_input():
        while True:
            try:
                numeroUsuario = int(input('Entre com um número: '))
            
            except ValueError as err:
                print('Valor inválido!')
                continue

            if 1 <= numeroUsuario <=15:
                return numeroUsuario

            print('O valor deve ser entre 1 e 15')

# verifica se o usuario acertou o numero
def check_numbers(numeroSorteio,numeroUsuario):
    if numeroUsuario == numeroSorteio:
        print('Parabéns!')
        return True

    elif numeroUsuario > numeroSorteio:
        print('Número muito alto, tente um númenro menor!')
        return False

    elif numeroUsuario < numeroSorteio:
        print('Número muito baixo, tente um número maior!')
        return False

    else:
        print('Digite um valor válido!')
        return False


for i in range(3):

    numeroUsuario = get_input()

    if check_numbers(numeroSorteio=numeroSorteio,numeroUsuario=numeroUsuario):
        break

else:
    print('Suas tentativas acabaram!')


# %%
