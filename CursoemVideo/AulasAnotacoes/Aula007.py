#Espaçamento:
n = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(n))

n = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(n))

n = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(n))

#Operadores Aritméticos:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m , d))
print('Divisão inteira {} e potência {}'.format(di, e))

# \n = Quebra a linha
# end = Caso tenha quebrado a linha, com o "end" ele não vai quebrar
