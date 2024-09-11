# Fatiamento de String
frase = 'Curso em Vídeo Python'
print(frase[9])       # 'V'
print(frase[9:13])    # 'Víde'
print(frase[9:21:2])  # 'VdoPto'

#Funções de Análise
frase = 'Curso em Vídeo Python'
print(len(frase))         # 21
print(frase.count('o'))   # 3
print(frase.find('Vídeo')) # 9

#Transformações
frase = '   Aprendendo Python   '
print(frase.replace('Python', 'Java'))  # '   Aprendendo Java   '
print(frase.upper())                    # '   APRENDENDO PYTHON   '
print(frase.lower())                    # '   aprendendo python   '
print(frase.capitalize())               # '   aprendendo python   '
print(frase.title())                    # '   Aprendendo Python   '
print(frase.strip())                    # 'Aprendendo Python'

