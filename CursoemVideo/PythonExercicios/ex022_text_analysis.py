N = str(input('Digite seu nome completo: ')).strip()
separa = N.split()
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é: {N.upper()}')
print(f'Seu nome em letras minúsculas é: {N.lower()}')
print(f'Seu nome tem ao todo {len(N) - N.count(' ')} letras')
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')