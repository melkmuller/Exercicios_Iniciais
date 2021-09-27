#Desenvolver um programa que receba o nome,
# idade e salário de uma pessoa e aplique um desconto de 20% 
# no salário dessa pessoa.

#Entrada de dados
nome = input("Insira o nome: ")
idade = int(input("Insira a idade: "))
salario = float(input("Insira o salário: "))

#Processamento dos dados
descontado = salario * 0.8

#Saída de dados
print("Olá " + nome.title() + ", " + str(idade) + " anos," + " seu salário descontado é" + " R$ " + str(descontado))
#O comando .title() depois da variável nome, faz com que a primeira letra fique em maiúsculo
#O comando .upper() depois da variável nome, faz com que todas as letras fiquem em maiúsculo