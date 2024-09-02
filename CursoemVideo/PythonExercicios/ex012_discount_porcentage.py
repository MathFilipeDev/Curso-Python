P = float(input('Qual é o preço do produto? R$ '))
D = (P*0.05)
promo = (P-D)
print(f'O produto que custava {P:.2f}, na promoção com desconto de 5% vai custar R${promo:.2f}')