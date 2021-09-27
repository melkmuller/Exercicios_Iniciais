#Programa para transformar Fahrenheit em Celsius

#Entrada de dados e introdução
print("Vamos transformar uma temperatura de Fahrenheit para Celsius, digite abaixo o valor da temperatura:")
temperatura = float(input("Temperatura em Fahrenheit: "))

#Processamento de dado
celsius = (temperatura - 32) / 1.8

#Saída do dado
print(" A tempertura de " + str(temperatura) + "°F, equivale a " + str(celsius) + "°C" )