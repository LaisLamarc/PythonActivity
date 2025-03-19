#desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a sua media

nota1 = float(input('Qual foi a sua nota da AV1?:'))
nota2 = float(input('Qual foi a sua nota da AV2?:'))
media = (nota1 + nota2) / 2
print('A sua média é {:.1f}'.format(media))


