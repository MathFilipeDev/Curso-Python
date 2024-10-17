A = int(input('Ano de Nascimento: '))
I = (2024 - A)
if I <= 9:
    print(f'O atleta tem {I} anos.\nClassificação: JUNIOR')
elif I > 9 and I <= 14:
    print(f'O atleta tem {I} anos.\nClassificação: INFANTIL')
elif I > 14 and I <= 19:
    print(f'O atleta tem {I} anos.\nClassificação: JUNIOR')
elif I > 19 and I <= 25:
    print(f'O atleta tem {I} anos.\nClassificação: SÊNIOR')
else:
    print(f'O atleta tem {I} anos.\nClassificação: MASTER')

# LEMBRE-SE: Você pode importar a biblioteca da data do computador: from datetime import date. 
# Depois, crie uma variavel para remeter essa data, ex: atual = date.today().year