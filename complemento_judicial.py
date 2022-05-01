print("Olá, esse programa objetiva, exclusivamente, calcular o valor correto de complemento de piso salarial dos técnicos em radiologia do município de Fortaleza \nque foram contemplados pelos efeitos da sentença do processo judicial número 0805265.59.2016.4.05.8100. ")

vencimento = float(input('Digite o valor atual de seu vencimento: '))
grat_rx = float(input('Digite o valor atual de sua gratificação de raiox - x: '))
complemento_atual = 2377.90 - (vencimento + grat_rx)
vencimento_2020 = float(input('Digite o valor de seu vencimento em setembro de 2020: '))
gratrx_2020 = float(input('Digite o valor de sua gratificação de raios-x em setembro de 2020: '))
complemento_2020 = 2377.90 - (vencimento_2020 + gratrx_2020)
pisosalarial_atual = (2377.90 + (2377.90 * 0.1458))
complemento_corrigido = pisosalarial_atual - (vencimento + grat_rx)
diferença = complemento_corrigido - complemento_atual

print(f'Seu complemento de piso salarial em 2020 era {complemento_2020:.2f} R$. \n'
      f'Seu complemento de piso salarial atualmente é: {complemento_atual:.2f} R$. \n'
      f'Seu complemento de piso salarial deveria ser: {complemento_corrigido:.2f} R$. \n'
      f'Seu complemento de piso salarial está defasado em: {diferença:.2f} R$.')

