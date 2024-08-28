soma = 0
N = int(input('Informe quantas médias você quer calcular '))
for i in range(1, N + 1):
    print(f'\nMédia do aluno {i}')
    nome = input("Informe o nome: ")
    p1 = float(input("Informe p1: "))
    p2 = float(input("Informe p2: "))
    m = (p1 + p2) / 2
    soma = soma + m
    print(f'Média: {m}')
mturma = soma / N
print(f'\nMédia da turma: {mturma}')