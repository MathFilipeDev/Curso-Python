print(f'{" LOJA FICTÍCIA ":=^40}')
P = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
option = int(input('Qual é a opção? '))
if option == 1:
    print(f'\033[1;32mSua compra de R${P} vai custar {P-(P*0.1):.2f} no final.\033[m')
elif option == 2:
    print(f'\033[1;32mSua compra de R${P} vai custar {P-(P*0.05):.2f} no final.\033[m')
elif option == 3:
    print(f'Sua compra será parcelada em \033[1;34m2x de R${P / 2:.2f}\033[m')
    print(f'\033[1;32mSua compra de R${P:.2f} vai custar R${P:.2f} no final.\033[m')
elif option == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em \033[1;33m{parcelas}x de {(P / parcelas) * 0.2 + (P / parcelas):.2f} COM JUROS\033[m')
    print(f'\033[1;32mSua compra de R${P:.2f} vai custar R${P+(P*0.2)} no final.\033[m')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')

