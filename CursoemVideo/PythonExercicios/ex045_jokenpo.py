from random import randint
from time import sleep
itens = ('Tesoura', 'Papel', 'Pedra')
pc = randint(0, 2)

print('''Suas opções:
[ 0 ] TESOURA
[ 1 ] PAPEL     
[ 2 ] PEDRA''')

player = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 10)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[player]}')
print('-=' * 10)

if pc == 0:
    if player  == 0:
        print('EMPATE')
    elif player == 1:
        print('COMPUTADOR VENCEU')
    elif player ==2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida!')
elif pc == 1:
    if player  == 0:
        print('JOGADOR VENCEU')
    elif player == 1:
        print('EMPATE')
    elif player ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada inválida!')
elif pc == 2:
    if player  == 0:
        print('COMPUTADOR VENCEU')
    elif player == 1:
        print('JOGADOR VENCEU')
    elif player ==2:
        print('EMPATE')
    else:
        print('Jogada inválida!')


