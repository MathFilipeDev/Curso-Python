#ESTRUTURA DE REPETIÇÃO FOR

#Repetições de oi
for c in range (0, 6):
    print('Oi') #Dentro do laço
print('FIM') #Fora do laço 

#Contagem crescente de 1 a 6
for c in range (0, 6):
    print(c) 
print('FIM') 

#Contagem regressiva de 6 a 1
for c in range (6, 0, -1):
    print(c) 
print('FIM') 

#Contagem crescente de 2 em 2
for c in range (0, 7, 2):
    print(c) 
print('FIM')

#---------------------------------#

#Contagem crescente até o valor da variável
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

#Estabelecendo o início e o fim de uma contagem e demarcando a quantidade de cada passo até chegar ao fim
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

#Repetições de comandos e o somatório deles!
s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')