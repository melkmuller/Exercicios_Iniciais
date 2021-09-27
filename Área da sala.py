#Programa para calcular a área de uma sala

#Entrada de dados
print("Olá, vou ajudar você a calcular a área de uma sala...")
print("Digite abaixo as informações requeridas")

#Variáveis
comprimento = float(input("Digite aqui o comprimento da sala em metros: "))
largura = float(input("Digite aqui a largura da sala em metros: "))

#Processamento dos dados
area = comprimento * largura

#Saída dos dados
print("A área da sala é de " + str(area) + "m²")