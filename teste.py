#             # TRABALHANDO COM FLOAT
# prova1 = float(input("Qual foi sua nota na prova de Portugues? "))
# prova2 = float(input("Qual foi sua nota na prova de Matemática? "))
# prova3 = float(input("Qual foi sua nota na prova de Inglês? "))

# media = (prova1 + prova2 + prova3) / 3.0

# print(f"Sua média é: {media:.1f}") #f{} formata o tipo de dado dentro das chaves | :.xf formata o tanto de casas decimais que esse número terá.

# if media > 6.0:
#     print("Parabéns, você passou!")
# elif media == 6.0:
#     print("Eita, passou raspando")
# else:
#     print("Infelizmente você rodou, pegue um lenço na saída")

#         Converter celsius pra fahrenheit
# tempC = int(input("Qual a temperatura em Celsius que queria converter para fahrenheit? "))

# tempF = float(tempC * (9/5)) + 32

# print(f"{tempC} em fahrenheit equivalem a: {tempF}")


#         Matemática com código
# import math

# exponencial = math.exp(3)

# print(exponencial)

#         funções em python
# # meu_nome = input("Seu nome: ")

# # def hello(meu_nome):
# #     print('Olá, ' + meu_nome)

# # print(hello(meu_nome))
                
#                 Calculadora de salário por horas trabalhadas
# horas = float(input("Quantas horas trabalhou nessa semana? "))
# dinheiro = float(input("Quanto vale a sua hora trabalhada? "))

# def calcular_pagamento(qtd_horas, valor_hora):
#     salario = horas * dinheiro
#     if horas >= 40:
#         return salario
#     else:
#         print('você não trabalhou o suficiente')

# salario = calcular_pagamento(horas, dinheiro)

# if horas > 40:
#     print(f"Você vai receber R$: {salario}")



#                     Jogo do detetive
# print('Detetive')
# print('Responda as perguntas abaixo com S(sim) ou N(não)')

# perguntas = ('Você telefonou para a vitima? ', 'Você esteve no local do crime? ', 'Você era vizinha da vítima? ', 'Você tinha crush na vítima? ', 'Você devia dinheiro para a vítima? ')

# respostas = []

# for pergunta in perguntas:
#     respostas.append(input(pergunta).upper()) #pra cada pergunta na lista de perguntas, insira a resposta que o jogador deu na lista Respostas 

# tipo = 0

# for resposta in respostas:
#     if resposta == "S": # pra cada resposta na lista respostas, se tiver uma resposta com o valor S, some +1 no tipo
#         tipo += 1

# if tipo < 2: #Classificação do jogador com base no valor da variavel tipo
#     print("Você é inocente")
# elif tipo <= 4:
#     print("Você é uma testemunha")
# else:
#     print("Você é o culpado")


qntPessoas = int(input("Quantas pessoas tem na sua turma? "))

pessoas = []

while pessoa <= qntPessoas:    
    pessoas.append(int(input("Qual a idade mental dessa pessoa? "))

def soma(a, b)
    resultado = a + b
    a += 2
    b += 2
    return resultado

while 