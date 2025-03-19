#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

medida = float(input('Uma distância em metros: '))
cm = medida * 100
km = medida * 1000
mm = medida * 1000
dm = medida * 1000000
dam = medida * 10000000000000
hm = medida * 100000000000
print( 'A medida de {}m corresponde a {}cm, {}km, {}mm, {}dm, {}dam, {}hm '.format(medida, cm, km, mm, dm, dam, hm))

