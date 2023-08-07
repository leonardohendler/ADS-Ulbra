# 1. Você está desenvolvendo um programa para calcular a corrente elétrica em um circuito elétrico. O
# usuário deve informar a resistência elétrica e a tensão elétrica do circuito. Escreva um algoritmo que
# calcule e imprima a corrente elétrica do circuito, de acordo com a lei de Ohm.

# resistencia_eletrica= int(input("Digite a resistencia elétrica\n"))
# tensao_eletrica= int(input("Digite a tensão elétrica\n"))
# corrente_eletrica= tensao_eletrica/resistencia_eletrica
# print(f"A corrente elétrica através da Lei de Ohm é {corrente_eletrica}")





# 2. Você está desenvolvendo um programa que verifica se uma pessoa pode dirigir ou não. Para isso,
# você precisa solicitar a idade da pessoa e verificar se ela é maior ou igual a 18 anos. Se a idade for
# menor que 18, o programa deve informar que a pessoa não pode dirigir, caso contrário, o programa
# deve informar que a pessoa pode dirigir.
# nome= (input("Informe seu nome:\n"))
# idade= int(input("Informe sua idade:\n"))


# if idade <= 18:
#     print(f'{nome}, não tem idade para dirigir')

# elif idade > 18:    
#     print(f'{nome}, está liberado para dirigir')

# else:
#     print(f'A pessoa não quer dirigir')




# 3. Você está desenvolvendo um programa que verifica se um número é par ou ímpar. Para isso, você
# precisa solicitar o número e verificar se ele é divisível por 2. Se o número for divisível por 2, o
# programa deve informar que o número é par, caso contrário, o programa deve informar que o número
# é ímpar.

# num1= int(input("Informe um valor inteiro:\n"))

# if num1 == 0:
#     print("O numero é 0")
# elif num1 % 2 == 0:
#     print("O numero digitado é par")
# else:
#     print("O numero é impar")    



# 4. Você está desenvolvendo um programa para calcular a altura máxima e o tempo de queda de um
# objeto em um lançamento vertical. O usuário deve informar a altura inicial do objeto. Assuma que a
# aceleração da gravidade é igual a 9,81 m/s2. Escreva um algoritmo que calcule e imprima a altura
# máxima e o tempo de queda do objeto.

# altura_inicial_objeto= float(input("Digite a altura inicial do objeto\n"))
# aceleracao_gravidade=  9.81
# tempo_queda= (2*altura_inicial_objeto)/(aceleracao_gravidade)**0.5
# altura_maxima= (aceleracao_gravidade* (tempo_queda**2))/2

# print(f'O tempo de queda do objeto é: {tempo_queda}, e a altura máxima obtida foi: {altura_maxima}')


# 5. Você está desenvolvendo um programa para calcular a distância percorrida por um objeto em um
# movimento uniformemente acelerado. O usuário deve informar a velocidade inicial, a aceleração e o
# tempo de deslocamento. Escreva um algoritmo que calcule e imprima a distância percorrida pelo
# objeto.

# velocidade_inicial= int(input("Informe a velocidade inicial \n"))
# aceleracao= int(input("Informe a aceleração \n"))
# tempo_deslocamento= int(input("Informe o tempo de deslocamento \n"))
# distancia_percorrida= (velocidade_inicial*tempo_deslocamento) + (1/2) * aceleracao * tempo_deslocamento ** 2

# print(f'A distancia percorrida foi: {distancia_percorrida}')





# 6. Você está desenvolvendo um programa para classificar triângulos de acordo com as medidas de
# seus lados. O usuário deve informar as medidas dos três lados do triângulo. Escreva um algoritmo
# que determine e imprima se o triângulo é equilátero, isósceles ou escaleno.
# lado1= int(input("Informe a medida do lado do triangulo \n"))
# lado2= int(input("Informe a medida do lado do triangulo \n"))
# lado3= int(input("Informe a medida do lado do triangulo \n"))



# if lado1 == lado2 == lado3:
#     print("O triangulo é equilátero")
# elif lado1 == lado2 or lado1 == lado3 or lado2== lado3 :
#     print("O triangulo é isósceles")
# else:
#     print ("O triangulo é escaleno")    




# 7. João é um médico que trabalha em uma clínica especializada em saúde preventiva. Ele está
# desenvolvendo um programa para calcular o IMC (Índice de Massa Corporal) de seus pacientes. O
# IMC é uma medida que relaciona o peso e a altura de uma pessoa e é utilizada para verificar se ela
# está com o peso ideal. João sabe que, para calcular o IMC, ele precisa da altura e do peso do
# paciente. Escreva um algoritmo em Python que ajude João a calcular o IMC de seus pacientes.

# peso= float(input("Digite o peso do paciente \n"))
# altura= float(input("Digite a altura do paciente \n"))
# imc= peso/altura**2
# print(f'O Imc do paciente é: {imc}')



# 8. Maria é uma estudante de física que está desenvolvendo um programa para converter uma
# temperatura de Celsius para Fahrenheit. Ela sabe que muitas vezes precisa realizar essa conversão
# em seus estudos, mas a fórmula matemática pode ser confusa. Por isso, ela está desenvolvendo um
# programa em Python que simplifica esse processo. Escreva um algoritmo que ajude Maria a
# converter uma temperatura de Celsius para Fahrenheit.

# celcius= float(input("Informe a temperatura em Celsius \n"))
# fahrenheit= (celcius*1.8)+32
# print(f'A conversão fica: {fahrenheit} graus Fahrenheit.')


# 9. Pedro é um estudante de matemática que está desenvolvendo um programa para calcular o volume
# de uma esfera. Ele sabe que o cálculo pode ser um pouco complicado, mas também é muito
# importante em diversas áreas da matemática e da física. Pedro está animado em desenvolver esse
# programa em Python para ajudar outros estudantes a entenderem melhor a fórmula. Escreva um
# algoritmo que ajude Pedro a calcular o volume de uma esfera.

# raio= float(input("Informe o raio da esfera \n"))
# pi= 3.14
# volume_esfera= (4/3)*pi*(raio**3)
# print(f'O volume da esfera é {volume_esfera}')





# 10. Ana é uma professora de matemática que está desenvolvendo um programa para calcular a média
# aritmética de uma lista de números. Ela sabe que, para calcular a média, é necessário somar todos
# os números da lista e dividir pelo total de números. Ana quer desenvolver um programa em Python
# que possa ser utilizado por seus alunos para facilitar esse processo. Escreva um algoritmo que ajude
# Ana a calcular a média aritmética de uma lista de números.


# numeros= [10,20,30,40,50]
# soma= sum(numeros)
# media= soma/len(numeros)
# print(f'A média é {media}')




