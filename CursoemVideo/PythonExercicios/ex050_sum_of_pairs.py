soma = 0
count = 0
for c in range(1,7):
    N = int(input(f'Digite o {c} valor: '))
    if N % 2 == 0:
        soma = soma + N
        count = count + 1
print(f'Você informou {count} números e a soma foi {soma}')

