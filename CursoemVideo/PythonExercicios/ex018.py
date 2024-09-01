import math
A = float(input('Digite o angulo que você deseja: '))
S = math.sin(math.radians(A))
C = math.cos(math.radians(A))
T = math.tan(math.radians(A))
print(f'O angulo de {A} tem o SENO de {S:.2f}')
print(f'O angulo de {A} tem o COSSENO de {C:.2f}')
print(f'O angulo de {A} tem a TANGENTE de {T:.2f}')