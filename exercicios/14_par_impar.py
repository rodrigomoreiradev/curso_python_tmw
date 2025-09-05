# %%

def par_impar(numero:int ):
    if numero % 2 == 0:
        return 'Par'

    else:
        return 'Impar'


numero = input('Entre com um número: ')
numero = int(numero)

resultado = par_impar(numero= numero)

print(f'O {numero} é {resultado}')