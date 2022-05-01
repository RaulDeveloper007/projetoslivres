custoFabrica = float(input('Qual o custo de fábrica do produto?'))
impostos = custoFabrica * 0.45
distribuidor = custoFabrica * 0.28
custoFinal = custoFabrica + impostos + distribuidor

print(f'O custo final a ser pago pelo consumidor é: {custoFinal:.2f}', end = ' R$')
