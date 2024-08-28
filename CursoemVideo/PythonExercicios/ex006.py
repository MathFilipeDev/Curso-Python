# no .format é necessário escrever as variantes depois, facilitando o erro de ordem em caso de muita quantidade.

n = float(input('Digite um valor: '))
print('O dobro de {} vale {}.'.format(n, n*2))
print('O triplo de {} vale {}.'.format(n, n*3))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, n**(1/2)))

# já fstring é só colocar um "f" antes das aspas e colocar as variantes e caso tenha suas alterações dentro das chaves.

n = float(input('Digite um valor: '))
print(f'O dobro de {n} vale {n*2}.')
print(f'O triplo de {n} vale {n*3}.')
print(f'A raiz quadrada de {n} é igual a { n**(1/2):.2f}.')