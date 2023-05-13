# 1. Escreva um programa que receba uma lista de números do usuário e imprima a
# lista na tela.

# lista= [int(input("Digite um numero\n"))] + [int(input("Digite outro numero\n")) for i in range(4)]
# print(f'Lista desejada: {lista}')

# 2. Escreva um programa que receba uma lista de nomes do usuário e imprima cada
# nome em uma linha separada.



# 3. Escreva um programa que receba uma lista de números do usuário e calcule a
# soma de todos os números presentes na lista.

# lista=[]
# numero= input("Digite um numero ou 'sair' para encerrar:\n ")
# while numero!= "sair":
#     lista.append(int(numero))
#     numero=input("Digite outro numero ou 'sair' para encerrar:\n ")

# total_itens = len(lista)
# itens_lista= ",".join(str(item) for item in lista)
# soma= sum(lista)

# print(f"total de itens: {total_itens}")
# print(f"Itens na lista: {itens_lista}")
# print(f"A soma dos numeros da lista é:{soma}")

# 4. Escreva um programa que receba uma lista de números do usuário e calcule a
# média de todos os números presentes na lista.

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

# 5. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números pares presentes na lista.

# lista=[int(input("Digite um numero\n"))] + [int(input("Digite outro numero\n")) for i in range(3)]

# print("Numeros pares da lista:")

# for numero in lista:
#     if numero % 2 ==0:
#         print(f"{numero}")
    
# 6. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números ímpares presentes na lista.
# 7. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números que são múltiplos de 3 e 5 simultaneamente.
# 8. Escreva um programa que receba uma lista de números do usuário e imprima a
# lista em ordem crescente.
# 9. Escreva um programa que receba uma lista de números do usuário e imprima a
# lista em ordem decrescente.
# 10.Escreva um programa que receba uma lista de números do usuário e verifique se
# um número específico está presente na lista.





# 1.Escreva um programa que receba uma lista de números do usuário e retorne o maior número
# presente na lista.
# 2. Escreva um programa que receba uma lista de números do usuário e retorne o menor número
# presente na lista.
# 3. Escreva um programa que receba uma lista de números do usuário e retorne a soma de todos os
# números presentes na lista.
# 4. Escreva um programa que receba uma lista de números do usuário e retorne a quantidade de
# números pares presentes na lista.
# 5. Escreva um programa que receba uma lista de números do usuário e retorne a quantidade de
# números ímpares presentes na lista.
# 6. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números pares presentes na lista.
# 7. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números ímpares presentes na lista.
# 8. Escreva um programa que receba uma lista de nomes do usuário e retorne o nome mais longo
# presente na lista.
# 9. Escreva um programa que receba uma lista de números do usuário e retorne a média dos
# números presentes na lista.
# 10. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números que são múltiplos de 3 e 5 simultaneamente.
# 11. Escreva um programa que receba uma lista de nomes do usuário e determine se todos os
# nomes possuem a mesma quantidade de caracteres.
# 12. Escreva um programa que receba uma lista de números do usuário e retorne uma lista com
# apenas os números ímpares presentes na lista, utilizando um loop while.
# 13. Escreva um programa que receba uma lista de números do usuário e retorne a lista em ordem
# crescente.
# 14. Escreva um programa que receba uma lista de números do usuário e retorne a lista em ordem
# decrescente.
# 15. Escreva um programa que receba uma lista de números do usuário e retorne uma lista sem
# duplicatas.



print("TERMINAL DE VENDAS")
print("Menu de produtos")
print("1 - ÁGUA")
print("2 - REFRI")
print("3 - CAFÉ")
print("4 - PÃO DE QUEIJO")
print("5 - IMPRIMIR LISTA")
print("6 - ENCERRAR VENDA")
print("7 - SAIR")
print("____________________________________________________")


pedido=[]
descricao=[]
while True:

    opc_menu= int(input("Digite o código:"))  
    
    if opc_menu ==1:
        pedido.append(3.00)
        descricao.append("Água - R$ 3,00")
    elif opc_menu == 2:
        pedido.append(6.00)
        descricao.append("Refri - R$ 6,00")
    elif opc_menu == 3:
        pedido.append(5.00)
        descricao.append("Café - R$ 5,00")
    elif opc_menu == 4:
        pedido.append(10.00)
        descricao.append("Pão de queijo - R$ 10,00")
    elif opc_menu == 5:
        print("------------------------")
        print(f"|PRODUTOS SELECIONADOS:|")
        print("------------------------")
        for item in descricao:
            print(item)
        print("--------------------------")
        print(f"Total do pedido: R$ {sum(pedido):.2f}")
        print("--------------------------")
    elif opc_menu == 6:
        print("--------------------------")
        print(f"Total do pedido: R$ {sum(pedido):.2f}")
        print("Formas de pagamento:")
        print("DINHEIRO")
        print("CARTÃ0 DE CRÉDITO OU DÉBITO")
        print("PIX")
        print("--------------------------")
    elif opc_menu == 7:    
        break
    else:
        print("Digite uma opção válida!")
        
#         colocar um try, e um except valueerror
--------------------------------------------------------------        
        
        pares=[]
impares=[]

for i in range(10):
    try:
        numero=int(input("Digite um numero inteiro\n"))
    except ValueError:
        print("Digite um valor inteiro!")
        continue
    
    if numero % 2 ==0:
        pares.append(numero)
        print(f'O numero digitado é Par!')
    else:
        impares.append(numero)
        print(f'O numero digitado é Impar!')
    

print(f"Numeros pares digitados:{pares}" )
print(f"Numeros impares digitados: {impares}" )


