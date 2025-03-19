#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input(' Largura da parede: '))
altura = float(input(' Altura da parede: '))
area = largura * altura
print(' Sua parede tem a dimensão de {}X{} e sua área é de {}m² '.format(largura, altura, area))
tinta = area / 2
print(' Para pintar essa parede voce precisará de {}L de tinta' .format(tinta))

#
distancia = float(input( 'Quantos Km voce irá percorrer?: '))
consumo = float(input ('Quantos km por litro seu carro faz?: '))
preçoCombustivel = float(input(' Qual o preço do combustivel?: R$ '))
litrosNecessarios = distancia / consumo
gastoTotal = litrosNecessarios * preçoCombustivel
print('Para percorrer {}Km voce precisará de {}L de combustivel e gastará R${} para percorrer esse trajeto' .format(distancia, litrosNecessarios, gastoTotal))
