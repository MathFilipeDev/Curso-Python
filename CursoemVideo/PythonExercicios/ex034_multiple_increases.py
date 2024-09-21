S = float(input('Qual é o sálario do funcionário? '))
if S <= 1250:
    print(f'Quem ganhava R${S} passa a ganhar R${S+(S*15)/100:.2f}')
else:
    print(f'Quem ganhava R${S} passa a ganhar R${S+(S*10)/100:.2f}')