n1 = int(input('\033[1;31mPrimeiro número: \033[m'))
n2 = int(input('\033[1;36mSegundo número: \033[m'))
if n1 > n2:
    print('O \033[1;32mPRIMEIRO\033[m valor é maior.')
elif n2 > n1:
    print('O \033[1;35mSEGUNDO\033[m valor é maior.')
elif n1 == n2:
    print('Os \033[1;33mdois valores\033[m são iguais.')