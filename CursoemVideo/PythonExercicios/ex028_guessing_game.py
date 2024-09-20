from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if player == pc:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {pc} e não no {player}')
