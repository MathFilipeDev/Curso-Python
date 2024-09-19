F = str(input('Digite uma frase: ')).upper().strip()
#.strip não conta os espaços
print(f'A letra A aparece {F.count('A')} vezes.')
print(f'A primeira letra A apareceu na posição {F.find('A')+1}')
print(f'A última letra A apareceu na posição {F.rfind('A')+1}')
