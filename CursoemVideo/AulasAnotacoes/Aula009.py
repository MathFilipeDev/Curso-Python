#1. Fatiamento de String
frase = 'Curso em Vídeo Python'
print(frase[9])       # 'V'
print(frase[9:13])    # 'Víde'
print(frase[9:21:2])  # 'VdoPto'

#2. Funções de Análise
frase = 'Curso em Vídeo Python'
print(len(frase))         # 21
print(frase.count('o'))   # 3
print(frase.find('Vídeo')) # 9

#2.1 Eliminar espaços
N = str(input('Digite seu nome completo: ')).strip() # o .strip elimina o espaço do inicio e do fim

separa = N.split() #separa cada palavra da frase
print(f'Seu nome tem ao todo {len(N) - N.count(' ')} letras') #Nesse caso ele Lê a frase e elimina os espaços entre as palavras

print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras') #Dessa forma ele identifica qual é a primeira palavra e depois conta quantas letras tem essa palavra

#3. Transformações
frase = '   Aprendendo Python   '
print(frase.replace('Python', 'Java'))  # '   Aprendendo Java   '
print(frase.upper())                    # '   APRENDENDO PYTHON   '
print(frase.lower())                    # '   aprendendo python   '
print(frase.capitalize())               # '   aprendendo python   '
print(frase.title())                    # '   Aprendendo Python   '
print(frase.strip())                    # 'Aprendendo Python'

#4. Junção de Strings
lista = ['Curso', 'em', 'Vídeo', 'Python']
print(' '.join(lista))  # 'Curso em Vídeo Python'

#5. Verificação de presença e posições
frase = 'Curso em Vídeo Python'
print('Curso' in frase)   # True
print(frase.find('Python'))  # 15
print(frase.rfind('o'))    # 17 (rfind busca da direita para a esquerda)

#6. ivisão de Strings
frase = 'Curso em Vídeo Python'
print(frase.split())  # ['Curso', 'em', 'Vídeo', 'Python']

#7. Uso de Strings Multilinha
mensagem = '''Olá, 
tudo bem? 
Esse é um exemplo de string multilinha.'''
print(mensagem)

#8. Justificando Textos
nome = 'Guanabara'
print(nome.ljust(20, '-'))  # 'Guanabara-----------'
print(nome.rjust(20, '-'))  # '-----------Guanabara'
print(nome.center(20, '-')) # '-----Guanabara------'

#9. Remoção de Espaços com strip(), rstrip(), e lstrip()
frase = '   Aprendendo Python   '
print(frase.rstrip())  # '   Aprendendo Python'
print(frase.lstrip())  # 'Aprendendo Python   '

#10. Uso de Variáveis em Strings
nome = 'Guanabara'
idade = 40
print(f'O professor {nome} tem {idade} anos.')