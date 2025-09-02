saldo_total = 0

while True:
    saldo = input('Digite o saldo: R$').replace(',','.')

    if saldo == '':
        break

    saldo_total += float(saldo)


print(f'Saldo total: R${saldo_total:.2f}')
