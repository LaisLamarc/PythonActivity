salario = float(input('Qual o seu salário atual?: R$ '))
novoSalario =  salario + (salario*15/100)
print( 'Seu novo salário com reajuste de 15%, ficou R${:.2f} .' .format(novoSalario))
