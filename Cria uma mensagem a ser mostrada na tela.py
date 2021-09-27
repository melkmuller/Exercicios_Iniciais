#Cria uma mensagem a ser mostrada na tela
mensagem1 = "Programa 1 - exibiçao básica de dados"
mensagem2 = "Informe se nome: "
mensagem3 = "Informe seu sobrenome: "
mensagem4 = "Informe sua altura: "

#Mostra mensagem na tela
print(mensagem1)
nome = input(mensagem2)
sobrenome = input(mensagem3)
altura = input(mensagem4)

#mostra dados na tela
nome_completo = nome + " " + sobrenome
print("Seu nome é:" + nome_completo.title())
print("Sua altura é: " + altura + " metros")