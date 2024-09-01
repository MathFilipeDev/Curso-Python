from random import choice
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
Lista = [a, b, c, d]
Escolhido = choice(Lista)
print(f'O aluno escolhido foi {Escolhido}')