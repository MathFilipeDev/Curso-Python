import math #Importacão de toda a biblioteca de math // "from math import sqrt" (é importar algo especifico)
N = int(input('Digite um número: '))
R = math.sqrt(N)
print(f'A raiz de {N} é igual a {R}') #Resultado exato
print(f'A raiz de {N} é igual a {math.ceil(R)}') #Arredonda para cima
print(f'A raiz de {N} é igual a {math.floor(R)}') #Arredonda para baixo