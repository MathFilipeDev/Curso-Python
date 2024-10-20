P = float(input('Qual é o seu peso? (Kg) '))
A = float(input('Qual é a sua altura? (m) '))
IMC = P / A ** 2
print(f'O IMC dessa pessoa é de {IMC:.1f}')
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif IMC >= 18.5 and IMC < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif IMC >= 25 and IMC < 30:
    print('Você está em SOBREPESO')
elif IMC >= 30 and IMC < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
