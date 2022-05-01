espessura = int(input('Informe a espessura da parte radiografada: '))
K = int(input('Informe a constante do aparelho: '))
kv = (espessura * 2) + K
print(f'Devem ser usados {kv}, Kv no exame radiográfico. ')
