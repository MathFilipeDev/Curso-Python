from random import randint 
Jogador1 = randint(1,10)
print('Qual número entre 1 e 10 eu estou pensando?')
acertou = False
tentativa = 0
while not acertou:
    Jogador2 = int(input('O número foi: '))
    tentativa += 1
    if Jogador2 == Jogador1:
        acertou = True
    else: 
        if Jogador2 != Jogador1:
            print('Errou... Tente novamente!')
print('Parabéns! Acertou com {} tentativas.' .format(tentativa))