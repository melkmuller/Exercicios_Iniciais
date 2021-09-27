#Programa que calcula o gasto em combustível previsto em uma viagem

#Entrada de dados
print("Vamos calcular quantos Reais serão gastos com combustível na sua viagem?")
dist = int(input("Informe a distância a ser percorrida em Km: "))
consumo = float(input("Informe o consumo em kilômetros por litro do carro: "))
preco = float(input("Informe o preço do combustível: "))

#Processamento dos dados
valor = (dist / consumo) * preco

#Saída de dados
print("Você precisará abastecer R$" + str(valor) + " para fazer esta viagem!")