total = int(input('Informe o número total de eleitores: '))
brancos = int(input('Informe a quantidade de votos brancos: '))
nulos = int(input('Informe a quantidade de votos nulos: '))

perc_brancos = brancos * 100 / total
perc_nulos = nulos * 100 / total
perc_validos = (brancos + nulos) * 100 / total

print(f'Votos brancos representam: {perc_brancos} %, votos nulos representam: {perc_nulos} %, votos válidos representam: {perc_validos} %')
