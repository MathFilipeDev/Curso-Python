N = int(input('Informe um número: '))
U = N // 1 % 10
D = N // 10 % 10
C = N // 100 % 10
M = N // 1000 % 10
print(f'Analisando o número {N}')
print(f'Unidade: {U}')
print(f'Dezena: {D}')
print(f'Centena: {C}')
print(f'Milhar: {M}')