# PRIMEIRA MANEIRA

#import math
#v = float(input('Digite um valor: '))
#print(f'O valor digitado foi {v} e a sua porção inteira é {math.trunc(v)}')

# SEGUNDA MANEIRA

from math import trunc
v = float(input('Digite um valor: '))
print(f'O valor digitado foi {v} e a sua porção inteira é {trunc(v)}')