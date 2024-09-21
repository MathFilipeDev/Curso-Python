V = float(input('Valor da casa: R$'))
S = float(input('Salário do comprador: R$'))
A = int(input('Anos de financiamento? '))
divisao = (V / A) / 12
if divisao > S * 0.3:
    print(f'Para pegar uma casa de R${V:.2f} em {A} anos a prestação será de {divisao:.2f}')
    print(f'Empréstimo NEGADO!')
else:
    print(f'Para pegar uma casa de R${V:.2f} em {A} anos a prestação será de {divisao:.2f}')
    print(f'Empréstimo APROVADO!')