# %%

def calc_imposto(preco:float, tx_base:float, **kwargs) -> float:
    imposto = preco * tx_base

    for chave, valor in kwargs.items():
        print(chave, valor)
        imposto += preco * valor

    return imposto

impostos_gerais = {
    'municipio' : 0.01,
    'estadual': 0.005,
    'nacional': 0.001
    }

calc_imposto(100,0.03,**impostos_gerais)
calc_imposto(100,0.03,municipio = 0.01, estadual = 0.005, nacional= 0.001)
