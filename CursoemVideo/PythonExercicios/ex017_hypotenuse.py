#PRIMEIRA MANEIRA (básica)

#b = float(input('Comprimento do cateto oposto: '))
#c = float(input('Comprimento do cateto adjacente: '))
#print(f'A hipotenusa vai medir {((b**2)+(c**2))**0.5:.2f}')

#SEGUNDA MANEIRA (Importar toda biblioteca de Math)

#import math
#b = float(input('Comprimento do cateto oposto: '))
#c = float(input('Comprimento do cateto adjacente: '))
#print(f'A hipotenusa vai medir {math.sqrt(math.pow(b, 2) + math.pow(c, 2)):.2f}')

#TERCEIRA MANEIRA (Importar apenas a potencia e a raiz quadrada)

#from math import pow, sqrt
#b = float(input('Comprimento do cateto oposto: '))
#c = float(input('Comprimento do cateto adjacente: '))
#print(f'A hipotenusa vai medir {sqrt(pow(b, 2) + pow(c, 2)):.2f}')

#QUARTA MANEIRA (Importar o calculo da hipotenusa)

from math import hypot
b = float(input('Comprimento do cateto oposto: '))
c = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(b, c):.2f}')