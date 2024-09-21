v = int(input('Qual é a velocidade atual do carro? '))
m = (v-80) * 7
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print(f'MULTADO! Você execedeu o limite permitido que é de 80Km/h. Você deve pagar uma multa de R${m}.00!')
    print('Tenha um bom dia! Dirija com segurança')