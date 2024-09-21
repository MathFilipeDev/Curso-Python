A = int(input('Ano de nascimento: '))
idade = 2024 - A
resta = 18 - idade
ano_alist = 2024 + resta
atraso = idade - 18
print(f'Quem nasceu em {A} tem {idade} anos em 2024.')
if A > 2006:
    print(f'Ainda faltam {resta} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_alist}.')
elif A < 2006:
    print(f'Você já deveria ter se alistado há {atraso} anos.')
    print(f'Seu alistamento foi em {2024 - atraso}')
else: # Nesse caso é a mesma coisa que elif A == 2006
    print(f'Você tem que se alistar IMEDUATAMENTE!')
    