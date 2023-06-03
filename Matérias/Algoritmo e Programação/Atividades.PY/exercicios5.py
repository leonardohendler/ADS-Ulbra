# 1. Escreva um programa que receba uma lista de números do usuário e imprima a
# lista na tela.
# lista=[]
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)


# print(lista)    


# 2. Escreva um programa que receba uma lista de nomes do usuário e imprima cada
# nome em uma linha separada.

# lista=[]
# while True:
#     nom=(input("Digite um nome\n"))
#     if nom == "sair":
#         break
#     else:
#         lista.append(nom)

# for i in lista:
#     print(i)



# 3. Escreva um programa que receba uma lista de números do usuário e calcule a
# soma de todos os números presentes na lista.

# lista=[]
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

  
# print("Soma da lista:", sum(lista))


# 4. Escreva um programa que receba uma lista de números do usuário e calcule a
# média de todos os números presentes na lista.

# lista= []
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# # lista.sort(reverse=True)    
# # sort = ordem crescente
# # reverse = decrescente



# print("Resultado da média da lista:", sum(lista)/len(lista))

# 5. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números pares presentes na lista.

# lista=[]
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# for item in lista:
#     if item % 2 ==0:
#         print("Itens pares da lista: ", item)

                 

    
# 6. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números ímpares presentes na lista.

# lista=[]
# while True:
#     numero=int(input("Digite um numero\n"))
#     if numero == 0:
#         break
#     else:
#         lista.append(numero)

# for item in lista:
#     if item % 2 != 0:
#         print(f"Itens impares da lista: {item}")





# 7. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números que são múltiplos de 3 e 5 simultaneamente.

# lista= []
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# for item in lista:
#     if item % 3 == 0 and item % 5 == 0: 
#         print(f"Os numeros multiplos de 3 e 5 são: {item}")        




# 8. Escreva um programa que receba uma lista de números do usuário e imprima a
# lista em ordem crescente.


# lista= []
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)


# lista.sort()
# print(lista)   

# 9. Escreva um programa que receba uma lista de números do usuário e imprima a
# lista em ordem decrescente.

# lista=[]
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# lista.sort(reverse=True)
# print(lista)

# 10.Escreva um programa que receba uma lista de números do usuário e verifique se
# um número específico está presente na lista.

# lista= []
# while True:
#     num= int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# print(lista)

# verificar=int(input("Digite o numero a ser verificado!\n"))
# for i in lista:
#     if i == verificar:
#         print("O numero esta presente na lista!")
            




# 1.Escreva um programa que receba uma lista de números do usuário e retorne o maior número
# presente na lista.


# lista= []
# while True:
#     num= int(input("Digite um numero!\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# maior_numero = max(lista)
# print(f"O maior numero da lista é: {maior_numero}")



# 2. Escreva um programa que receba uma lista de números do usuário e retorne o menor número
# presente na lista.

# lista= []
# while True:
#     num=int(input("Digite um numero para preencher a lista!\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# menor_numero = min(lista)
# print(f"O menor numero presenta na lista é: {menor_numero}")


# 3. Escreva um programa que receba uma lista de números do usuário e retorne a soma de todos os
# números presentes na lista.

# lista= []
# while True:
#     num= int(input("Digite um numero!\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)
# soma_lista= sum(lista)
# print(f"A soma dos numeros da lista é: {soma_lista}")


# 4. Escreva um programa que receba uma lista de números do usuário e retorne a quantidade de
# números pares presentes na lista.

# lista= []
# while True:
#     num= int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else: 
#         lista.append(num)

# numeros_pares = 0
# for i in lista:
#     if i % 2 == 0:
#         numeros_pares += 1
# print(numeros_pares)
       
        

# 5. Escreva um programa que receba uma lista de números do usuário e retorne a quantidade de
# números ímpares presentes na lista.

# lista= []
# while True:
#     num= int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else: 
#         lista.append(num)

# numeros_impares = 0
# for i in lista:
#     if i % 2 != 0:
#         numeros_impares += 1
# print(numeros_impares)

# 6. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números pares presentes na lista.

# lista= []
# lista_par= []
# while True:
#     num = int(input("Digite um numero\n"))
#     if num == 0: 
#         break
#     else:
#         lista.append(num)

# for i in lista:
#     if i % 2 == 0:
#         lista_par.append(i)

# print(f"Lista de numeros pares! {lista_par}")


# 7. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números ímpares presentes na lista.

# lista= []
# lista_impares= []
# while True:
#     num = int(input("Digite um numero\n"))
#     if num == 0: 
#         break
#     else:
#         lista.append(num)

# for i in lista:
#     if i % 2 != 0:
#         lista_impares.append(i)

# print(f"Lista de numeros pares! {lista_impares}")

# 8. Escreva um programa que receba uma lista de nomes do usuário e retorne o nome mais longo
# presente na lista.


# lista= []
# while True:
#     nomes=(input("Digite um nome\n"))
#     if nomes == "sair":
#         break
#     else:
#         lista.append(nomes)
# nome_mais_longo=  max(lista, key=len)
# print(nome_mais_longo)

# 9. Escreva um programa que receba uma lista de números do usuário e retorne a média dos
# números presentes na lista.
# lista=[]
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# quantidade_numeros= len(lista)
# soma_da_lista= sum(lista)
# media= soma_da_lista/quantidade_numeros

# print(media)


# 10. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números que são múltiplos de 3 e 5 simultaneamente.

# lista = []
# while True:
#     num = int(input("Digite um numero!\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# for item in lista:
#     if item % 3 == 0 and item % 5 ==0:
#         print(f"O numeros multiplos de 3 e 5 na lista são: {item}")
#     else:
#         print("Não tem nenhum numero presente na lista!")  


# 11. Escreva um programa que receba uma lista de nomes do usuário e determine se todos os
# nomes possuem a mesma quantidade de caracteres.

# lista = []
# lista_nova = []
# while True:
#     nome= input("Digite um nome:\n")
#     if nome.lower() == "sair": #lower = defini tudo como minusculo
#         break
#     else:
#         lista.append(nome)

# for item in lista:
#     tamanho = len(item)
#     lista_nova.append(tamanho)
# if sum(lista_nova)/tamanho==len(lista):
#     print("Tamanhos iguais")
# else:
#     print("Tamanhos diferentes")    
    


# 12. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números ímpares presentes na lista, utilizando um loop while.


# lista=[]
# lista_impares=[]
# while True:
#     num= int(input("Digite um numero!\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# for item in lista:
#     if item % 2 != 0:
#         lista_impares.append(item)

# print(lista_impares)
        

# 13. Escreva um programa que receba uma lista de números do usuário e retorne a lista em ordem
# crescente.

# lista= []

# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)

# lista.sort()
# print(lista)
    
# 14. Escreva um programa que receba uma lista de números do usuário e retorne a lista em ordem
# decrescente.

# lista=[]

# while True:
#     num=int(input("Digite um numero\n"))
#     if num ==0:
#         break
#     else:
#         lista.append(num)

# lista.sort(reverse=True)
# print(lista)
            
# 15. Escreva um programa que receba uma lista de números do usuário e retorne uma lista sem
# duplicatas.

# lista=[]
# nova_lista=[]
# while True:
#     num=int(input("Digite um numero\n"))
#     if num == 0:
#         break
#     else:
#         lista.append(num)
# print(lista)
# for item in lista:
#     if item not in nova_lista:
#         nova_lista.append(item)
# print(nova_lista)


# ______________________________________________________________________________

# exercicios extras

# ______________________________________________________________________________

# lista=[]
# numero= input("Digite um numero ou 'sair' para encerrar:")
# while numero!= "sair":
#     lista.append(int(numero))
#     numero=input("Digite outro numero ou 'sair' para encerrar: ")

# total_itens = len(lista)
# itens_lista= ",".join(str(item) for item in lista)
# media= sum(lista)/total_itens

# print(f"total de itens: {total_itens}")
# print(f"Itens na lista: {itens_lista}")
# print(f"Média dos numeros da lista:{media}")


   
# import os

# pedido=[]
# descricao=[]
# while True:
        
#     print("TERMINAL DE VENDAS")
#     print("Menu de produtos")
#     print("1 - ÁGUA")
#     print("2 - REFRI")
#     print("3 - CAFÉ")
#     print("4 - PÃO DE QUEIJO")
#     print("5 - IMPRIMIR LISTA")
#     print("6 - ENCERRAR VENDA")
#     print("7 - SAIR")
#     print("____________________________________________________")



#     opc_menu= int(input("Digite o código:"))  
#     os.system('cls')
#     if opc_menu ==1:
#         pedido.append(3.00)
#         descricao.append("Água - R$ 3,00")
#     elif opc_menu == 2:
#         pedido.append(6.00)
#         descricao.append("Refri - R$ 6,00")
#     elif opc_menu == 3:
#         pedido.append(5.00)
#         descricao.append("Café - R$ 5,00")
#     elif opc_menu == 4:
#         pedido.append(10.00)
#         descricao.append("Pão de queijo - R$ 10,00")
#     elif opc_menu == 5:
#         print("------------------------")
#         print(f"|PRODUTOS SELECIONADOS:|")
#         print("------------------------")
#         for item in descricao:
#             print(item)
#         print("--------------------------")
#         print(f"Total do pedido: R$ {sum(pedido):.2f}")
#         print("--------------------------")
#     elif opc_menu == 6:
#         print("--------------------------")
#         print(f"Total do pedido: R$ {sum(pedido):.2f}")
#         print("Formas de pagamento:")
#         print("DINHEIRO")
#         print("CARTÃ0 DE CRÉDITO OU DÉBITO")
#         print("PIX")
#         print("--------------------------")
#     elif opc_menu == 7:    
#         break
#     else:
#         print("Digite uma opção válida!")
            
      
# # --------------------------------------------------------------        
        
# pares=[]
# impares=[]

# for i in range(10):
#     try:
#         numero=int(input("Digite um numero inteiro\n"))
#     except ValueError:
#         print("Digite um valor inteiro!")
#         continue
    
#     if numero % 2 ==0:
#         pares.append(numero)
#         print(f'O numero digitado é Par!')
#     else:
#         impares.append(numero)
#         print(f'O numero digitado é Impar!')
    

# print(f"Numeros pares digitados:{pares}" )
# print(f"Numeros impares digitados: {impares}" )




# ______________________________________________________________________________

# exercicios extras

# ______________________________________________________________________________
# lista=[]
# numero= input("Digite um numero ou 'sair' para encerrar:")
# while numero!= "sair":
#     lista.append(int(numero))
#     numero=input("Digite outro numero ou 'sair' para encerrar: ")

# total_itens = len(lista)
# itens_lista= ",".join(str(item) for item in lista)
# media= sum(lista)/total_itens

# print(f"total de itens: {total_itens}")
# print(f"Itens na lista: {itens_lista}")
# print(f"Média dos numeros da lista:{media}")



#--------------------------------------------------------------        
        
# pares=[]
# impares=[]

# for i in range(10):
#     try:
#         numero=int(input("Digite um numero inteiro\n"))
#     except ValueError:
#         print("Digite um valor inteiro!")
#         continue
    
#     if numero % 2 ==0:
#         pares.append(numero)
#         print(f'O numero digitado é Par!')
#     else:
#         impares.append(numero)
#         print(f'O numero digitado é Impar!')


# print(f"Numeros pares digitados:{pares}" )
# print(f"Numeros impares digitados: {impares}" )


# -------------------------------------------------------------- 

import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

print(requisicao)

dic_requisicao= requisicao.json()

cambio = dic_requisicao["USDBRL"] ["bid"]

dolar= float(cambio)

reais= float(input("Digite o valor em real"))

real = reais /dolar

print(real)

----------------------------------------------------

# import datetime as dt

# data_hora_atual= dt.datetime.now()

# print(f"A data e a hora atual é: {data_hora_atual}")


# import random

# numero_aleatorio = random.randint(1,10)

# print(f"O numero aleatório é: {numero_aleatorio}")

# import string

# caractere = 'a'

# if caractere in string.ascii.lowercase:
#     print(f"{caractere} é uma letra minúscula.")
# else:
#     print(f"{caractere} não é uma letra minúscula.")

    
# import io   

# with io.open("meu arquivo.txt", "w") as arquivo:
#     arquivo.write ("Ola, mundo!")   # joga essa frase la no arquivo


# with io.open("meu arquivo.txt", "r") as arquivo:
#     conteudo= arquivo.read()   # traz o conteudo do arquivo e joga no terminal


# print(conteudo)

# import matplotlib.pyplot as plt

# x= [1,2,3,4,5]

# y=[10,7,5,3,8]

# plt.plot(x,y)

# plt.xlabel ('Eixo X')

# plt.ylabel('Eixo Y')

# plt.title("Meu grafico")

# plt.show()


# import psutil

# disk = psutil.disk_usage("/")

# print(f"Uso de disco total: {disk.total}")
# print(f"Uso de disco usado: {disk.used}")
# print(f"Uso de disco livre: {disk.free}")
# print(f"Porcentagem de disco em uso: {disk.percent}%")

# print("--------------------------------")
# print("Digite uma das opções a seguir!")



# import psutil

# mem= psutil.virtual_memory()

# print(f"Uso de memória total: {mem.total}")
# print(f"Uso de memória disponivel:{mem.available}")
# print(f"Porcentagem de memória em uso: {mem.percent}%")


# Utilize o módulo psutil para criar um algoritmo que exiba algumas informações sobre o seu PC, crie um menu para facilitar o uso.
# Exemplo do módulo:


# import psutil
# print("------------------------------------------------------------------------------------------")
# print("-------------------------SISTEMA OPERACIONAL DO WINDOWS 10--------------------------------")
# print("Digite a opção desejavel para vizualizar uma informação do sistema operacional do Windows:")
# print("Digite [1] :Mémoria disponivel")
# print("Digite [2] :Porcentagem de memória em uso")
# print("Digite [3] :Disco livre")
# print("------------------------------------------------------------------------------------------")


# opcao= int(input("Digite a opção desejada:\n"))


# if opcao == 1:
#     mem= psutil.virtual_memory()
#     print(f"Uso de memória disponivel:{mem.available}")
# elif opcao == 2:
#     mem= psutil.virtual_memory()
#     print(f"Porcentagem de memória em uso: {mem.percent}%")
# elif opcao == 3:
#     disk = psutil.disk_usage("/")
#     print(f"Uso de disco livre: {disk.free}")

# elif opcao % 1 or opcao % 2 or opcao % 3:
#     print("Digite uma das opções que constam no menu!")
   



