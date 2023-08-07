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
   









