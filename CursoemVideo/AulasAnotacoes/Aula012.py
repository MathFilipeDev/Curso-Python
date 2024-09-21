#Condições Aninhadas

#Esse tema se refere à utilização de estruturas condicionais dentro de outras estruturas condicionais, ou seja, colocar um bloco if, elif ou else dentro de outro bloco if

nome = str(input('Qual é o seu nome? '))
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Maite Chaves Ramos':
    print('Belo nome feminino')
else:
    print('Seu nome é bem comum.')
print(f'Tenha um bom dia {nome}')