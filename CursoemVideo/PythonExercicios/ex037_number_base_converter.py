N = int(input('Digite um número inteiro: '))
B = print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{N} convertido para BINÁRIO é igual a {bin(N) [2:]}')
elif opção == 2:
    print(f'{N} convertido para OCTAL é igual a {oct(N) [2:]}')
elif opção == 3:
    print(f'{N} convertido para HEXADECIMAL é igual a {hex(N) [2:]}')
else:
    print('Opção inválida. Tente novamente.')