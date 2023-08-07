# 1. Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a
# média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba
# "Reprovado".

# nota1= float(input("Informe o valor da nota\n"))
# nota2= float(input("Informe o valor da nota\n"))
# nota3= float(input("Informe o valor da nota\n"))
# media= (nota1) + (nota2) + (nota3)/3      

# if media >=7:
#      print("Aprovado")
# else:
#      print("Reprovado")

    
# 2. Verificação de idade: Escreva um programa que peça a idade do usuário e verifique se ele é
# maior de idade ou não. Se for maior de idade, exiba a mensagem "Você é maior de idade".
# Caso contrário, exiba "Você é menor de idade".

# idade= int(input("Informe sua idade\n"))

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")    

# 3. Verificação de números pares: Escreva um programa que leia um número inteiro e verifique
# se ele é par ou ímpar. Se for par, exiba a mensagem "O número é par". Caso contrário, exiba
# "O número é ímpar".

# numero= int(input("Informe um numero inteiro\n"))

# if numero % 2 ==0:
#     print("Par")
# else:
#     print("impar")


# 4. Cálculo de desconto: Escreva um programa que leia o valor de um produto e calcule o valor
# com desconto de 10%. Se o valor do produto for maior que R$ 50,00, aplique um desconto
# adicional de 5%. Exiba o valor final com desconto.

# valor_produto= float(input("Informe o valor do produto R$ \n"))
# desconto= 10
# desconto2=5

# calculo= valor_produto-(desconto*valor_produto/100)
# calculo2=valor_produto-((desconto2*valor_produto/100)+(desconto*valor_produto/100))

# if valor_produto <50:
#     print(f'O valor do produto é R$ {calculo:.2f} reais')
# else:
#     print(f'O valor do produto é R$ {calculo2:.2f} reais')    

# :.2f = usado para printar duas casas decimais.
 


# 5. Verificação de número positivo: Escreva um programa que leia um número e verifique se ele
# é positivo ou negativo. Se for positivo, exiba a mensagem "O número é positivo". Caso
# contrário, exiba "O número é negativo".

# numero= float(input("Digite um numero"))

# if numero > 0:
#     print("O número é positivo")
# else:
#     print("O numero é negativo")

    

# 6. Verificação de idade para votação: Escreva um programa que peça a idade do usuário e
# verifique se ele pode votar ou não. Se a idade for igual ou superior a 16 anos, exiba a
# mensagem "Você pode votar". Caso contrário, exiba "Você ainda não pode votar".

# idade= int(input("informe sua idade:\n"))

# if idade >=16:
#     print("Você pode votar")
# else:
#     print("Você não pode votar")

# 7. Verificação de senha: Escreva um programa que peça ao usuário uma senha e verifique se
# ela é válida ou não. Considere uma senha válida aquela que possui pelo menos 8
# caracteres, contendo pelo menos uma letra maiúscula e um número. Se a senha for válida,
# exiba a mensagem "Senha válida". Caso contrário, exiba "Senha inválida".

# senha=input("Digite uma senha")

# if len(senha) >= 8 and any(char.isupper() for char in senha) and any(char.isdigit() for char in senha):

            # char.isupper()= contem uma letra maiscula
            # char.isdigit()= contem um digito
            # for char in senha= informa que os dados estao dentro da senha.

#     print("Senha valida")
# else:
#     print("Senha invalida")    




# 8. Cálculo de imposto: Escreva um programa que leia o salário de um funcionário e calcule o
# valor do imposto a ser pago, considerando as seguintes faixas salariais: até R$ 1.000,00,
# isento de imposto; de R$ 1.000,00 a R$ 2.000,00, 10% de imposto; acima de R$ 2.000,00,
# 20% de imposto.

# salario= float(input("Informe seu salario \n"))
# desconto1= 10
# desconto2=20

# imposto_10= salario -(desconto1*salario/100)
# imposto_20=salario - (desconto2*salario/100)


# if salario <1000:
#     print(f'Com seu salario de {salario}, fica isento de imposto de renda.')
# elif salario >1000 and salario <2000:
#     print(f'Com seu salario de {salario}, voce deve pagar um imposto de 10%, assim o seu salario fica: {imposto_10}') 
# else:
#     print(f'Com seu salario de {salario}, voce deve pagar um imposto de 20%, assim o seu salario fica: {imposto_20}')






# 9. Verificação de ano bissexto: Escreva um programa que peça ao usuário um ano e verifique
# se ele é bissexto ou não. Um ano é bissexto se for divisível por 4 e não for divisível por 100,
# exceto quando é divisível por 400. Se o ano for bissexto, exiba a mensagem "O ano é
# bissexto". Caso contrário, exiba "O ano não é bissexto".

# while True:
#     ano= int(input("Informe um ano\n"))

#     if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#         print("O ano é bisexto")
#     else:
#         print("O ano não é Bisexto")    




# 10.Verificação de vogal: Escreva um programa que leia uma letra e verifique se ela é uma vogal
# ou não. Se for uma vogal, exiba a mensagem "A letra é uma vogal". Caso contrário, exiba "A
# letra é uma consoante".

# letra= input("Informe uma letra\n").lower()   
# vogais= ['a','e','i','o','u']
# # .lower() é usado para transformar tudo que vem antes em minusculo.
# # .upper() é usado para transformar tudo que vem antes em maiusculo.

# if letra in vogais:
#     print("A letra é uma vogal")
# else:
#     print("A letra é uma consoante")



# exercicio EXTRA
# ---------------------------------------------------------------------------------

# import random
# numero_correto = random.randint(1, 100)
# tentativas_restantes = 10

# print("Tente adivinhar o número escolhido pelo programa (entre 1 e 100):")

# while tentativas_restantes > 0:
#     try:
#         palpite = int(input("Digite seu palpite: "))
#     except ValueError:
#         print("Digite apenas números!")
#         continue
#     if palpite == numero_correto:
#         print("Parabéns, você acertou!")
#         break
#     elif palpite < numero_correto:
#         print("Seu palpite é menor do que o número correto.")
#     else:
#         print("Seu palpite é maior do que o número correto.")
#     tentativas_restantes -= 1

# if tentativas_restantes == 0:
#     print(f"Suas tentativas acabaram. O número correto era {numero_correto}.")

# -----------------------------------------------------------------------------------



# while True:
#     num= float(input("Digite um numero:\n"))
#     if num> 0:
#         print("O numero é positivo")
#     elif num <0:
#         print("O numero é negativo")
#     else:
#         print("O numero é zero")    






# letra= input("Digite uma letra:\n")
# letras_maisculas= ['a','e','i','o','u']

# if letra in letras_maisculas:
#     print("A letra é vogal")
# else:
#     print("A letra é consoante")






# Crie um algoritmo capaz de ler dois valores e imprimir uma das três mensagens a seguir:
# ‘Números iguais’, caso os números sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.

# numero1= float(input("Digite um numero:\n"))
# numero2= float(input("Digite um numero:\n"))

# if numero1 == numero2:
#     print("Numeros iguais")
# elif numero1 > numero2:
#     print("Primeiro é maior")    
# else:
#     print("Segundo maior")


"""Crie um algoritmo que receba o nome, sexo, idade e tempo de trabalho (contribuição).
Com base nos seguintes requisitos para aposentadoria: 
Mulheres - 30 anos de contribuição e 55 anos de idade
Homens - 35 anos de contribuição e 60 anos
Diga se as pessoas consultadas podem ou não requerer a aposentadoria.
Armazene as informações de quantas pessoas foram consultadas, por exemplo: esta é a consulta número XX.
Necessário MENU com interface para usuário (no terminal, não é tela gráfica!)."""

while True:

    print("__________________________________________________")
    print("Digite a opção deseja: 1 - FEMININO | 2- MASCULINO")

    sexo= (input("Informe seu sexo\n"))
    nome= (input("Informe seu nome\n"))
    idade= (input("Informe sua idade\n"))
    tempo_trabalho= (input("Informe seu tempo de trabalho\n"))
    

    idade_desejada1= '55'
    tempo_trabalho_desejado1= '30'

    idade_desejada2= '60'
    tempo_trabalho_desejado2= '35'

    if sexo == '1' and (idade >= idade_desejada1) and (tempo_trabalho >= tempo_trabalho_desejado1):
        print(f"Aposentadoria disponivel Sr(a) {nome}")
    elif sexo == '2'and (idade >= idade_desejada2) and (tempo_trabalho >= tempo_trabalho_desejado2):
        print(f"Aposentadoria disponivel Sr(a) {nome}")
    else:
        print("Aposentadoria não disponivel no momento")
        
