#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar- considere U$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem na carteira?: R$ '))
dolar = real / 5.77
euro = real / 5.99
print('Com R${:.2f} você pode comprar, US${:.2f}, EUR{:.2f}'.format(real, dolar, euro))
