#Escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma mensagem

numero01 = input('Digite o primeiro número: ')
numero02 = input('Digite o segundo número: ')

if(numero01 > numero02):
    print(" O número {} é maior que o número {}".format(numero01,numero02))

elif(numero01 < numero02):
    print("O número {} é menor que o número {}".format(numero01,numero02))

else:
    print("Os números digitados são iguais")