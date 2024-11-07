numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m')
        total += 1
    else:
        print('\033[31m')
    print(f'{c}', end='')
print(f'\n\033[mO número {numero} foi divisível {total} vez')
if total == 2:
    print('Por isso ele é Primo!')
else:
    print('Por isso ele NÃO é Primo!')