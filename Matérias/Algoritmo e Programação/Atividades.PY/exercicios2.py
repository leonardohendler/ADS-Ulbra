# 1. Uma pessoa foi a um restaurante que está com um prato do dia que custa R$ 35, mas no horário do
# almoço ele é vendido por R$ 25. Quantos reais uma pessoa economizaria pedindo o prato do dia no horário
# do almoço?
# prato_do_dia= int(35)
# horario_do_almoço= int(25)
# economia= prato_do_dia-horario_do_almoço
# print(f'Economia de: {economia}')

# 2. Calcule a área de um retângulo de base 8cm e altura 6cm.

# base= 8
# altura= 6
# area= base*altura
# print(f'A area do retangulo é: {area}')
# 3. Melhore seu algoritmo, possibilitando calcular a área de outros retângulos.

# base= int(input("Digite o valor da base do retangulo:\n"))
# altura= int(input("Digite o valor da altura do retangulo:\n"))
# area= base*altura
# print(f'O valor da area do retangulo é:{area}')
                
# 4. Uma pessoa pesa 65kg e mede 1,70m. Qual é o seu índice de massa corporal (IMC)? Considere a
# fórmula IMC = peso / altura2.

# peso=  80
# mede=  1.8
# imc= peso/(mede*mede)
# print(f'O indice de massa corporal é:{imc}')


# 5. Um ônibus saiu de uma cidade a 300km de distância e foi até outra cidade a uma velocidade média de
# 60km/h. Quanto tempo ele levou para chegar ao destino?

# distancia= 300
# velocidade= 60
# tempo=  distancia/velocidade
# print(f'O tempo levado foi:{tempo}')

# 6. Uma pessoa trabalha em uma empresa e recebe um salário base de R$ 2.500, mas também recebe um
# adicional de R$ 350 por mês por desempenho. Qual é o salário dessa pessoa em um ano?

# salario_base= 2500
# salario_adicional = 350
# salario_anual= (salario_base+salario_adicional)*12
# print(f'O salario anual é: R${salario_anual}')

# 7. Uma loja de roupas está com uma promoção de 20% de desconto em todos os produtos. Uma blusa
# custava R$ 80, quanto ela custará agora?
# blusa= 80
# desconto= 20
# valor_com_desconto= blusa - (desconto*blusa/100)
# print(f'O valor da blusa com desconto será: {valor_com_desconto}')

# 8. Um triângulo equilátero tem lado de medida 6cm. Calcule a sua área.

# lado_do_triangulo= int (input("Digite o valor do lado\n"))
# area_do_triangulo= ((lado_do_triangulo**2)*(0.5*3))/4
# print(f'A média do triangulo equilatero é: {area_do_triangulo}')

# 9. Um homem percorreu 10km em uma hora e meia. Qual é a sua velocidade média em km/h?

# distancia_percorrida= 10
# tempo= 1.5
# velocidade_média= distancia_percorrida/tempo
# print(f'A velocidade média foi:{velocidade_média}')

# 10. Um jardineiro está plantando uma cerca viva que tem 25 metros de comprimento. Se ele precisa
# plantar uma muda a cada 50 centímetros, quantas mudas ele precisará?

# cerca_viva= 25
# distancia_entre_as_mudas= 50
# mudas_necessarias= (cerca_viva*100)/50
# print(f'O jardineiro precisará de: {mudas_necessarias} mudas')

# 11. Uma escola de inglês oferece um curso de 6 meses que custa R$ 2.400. Qual é o valor mensal do
# curso?

# valor_total_curso=float (2400.00)
# quantidade_meses= float (6)
# valor_mensal_curso= valor_total_curso/quantidade_meses
# print(f'O valor mensal do curso é: R$ {valor_mensal_curso}')

# 12. Calcule a área de um círculo de raio 4cm. Considere a fórmula Área = π x raio2.

# raio_circulo= 4
# pi= 3.14
# area_circulo= pi*(raio_circulo**2)
# print(f'O valor da area do circulo é: {area_circulo}')

# 13. Uma loja de brinquedos está com uma promoção de 30% de desconto em um boneco que custa R$ 60.
# Qual é o preço do boneco com desconto?

# valor_boneco= 60
# desconto= 30
# boneco_com_desconto= valor_boneco - (desconto*valor_boneco)/100
# print(f'O valor do produto com desconto é: R$ {boneco_com_desconto} reais')

# 14. Um carro faz 12km por litro de gasolina. Se ele percorrer uma distância de 360km, quantos litros de
# gasolina ele gastará?

# média_carro= 12
# distancia_percorrida= 360
# litros_necessarios= distancia_percorrida/média_carro
# print(f'O carro gastará: {litros_necessarios} litros')


# 15. Uma pessoa está organizando uma festa e precisa de 1,5 litros de refrigerante para cada convidado. Se
# ela convidou 30 pessoas, quantos litros de refrigerante ela precisará?

# litro_por_convidado= 1.5
# numero_convidados= 30
# litros_refrigerante= litro_por_convidado*numero_convidados
# print(f'Essa pessoa precisará de {litros_refrigerante} litros de refrigerante ')

# 16. Calcule o perímetro de um quadrado de lado 5cm.

# lado_quadrado= 5
# perimetro_quadrado= lado_quadrado*4
# print(f' O perimetro do quadrado é: {perimetro_quadrado}')

# 17. Uma pessoa tem R$ 500 em sua conta corrente e precisa pagar uma conta de R$ 150 e
# outra de R$ 300. Qual é o saldo final da conta corrente?

# saldo_conta= 500
# conta1= 150
# conta2= 300
# saldo_final= saldo_conta -(conta1+conta2)
# print(f'O saldo em conta restante é: R$ {saldo_final} reais')


# exercicio extra:
# Faça um algoritmo que o usuario coloca o valor, e ele calcula quantas unidades de notas ou moedas.


# numero= float(input("Informo o valor em reais:\n"))
# nota_100= int(numero/100)
# numero= numero % 100
# nota_50= int(numero/50)
# numero=numero % 50
# nota_20=int(numero/20)
# numero= numero % 20
# nota_10= int(numero/10)
# numero= numero % 10
# nota_5= int(numero/5)
# numero= numero % 5
# nota_2= int(numero/2)
# numero= numero % 2

# print(f'A quantidade de notas de 100 necessarias são: {nota_100}')
# print(f'A quantidade de notas de 50 necessarias são: {nota_50}')
# print(f'A quantidade de notas de 20 necessarias são: {nota_20}')
# print(f'A quantidade de notas de 10 necessarias são: {nota_10}')
# print(f'A quantidade de notas de 5 necessarias são: {nota_5}')
# print(f'A quantidade de notas de 2 necessarias são: {nota_2}')

# # faça um algoritmo que recebe um numero inteiro e apresente a tabuada desse numero:

# numero= int(input("Digite um valor para saber a sua tabuada \n"))

# for i in range(1,11):
#         print(f'A tabudada do {numero} é:{i*numero}')


# _________________________________________________________________________________

# voce esta desenvolvendo um programa para calcular a distancia percorrida por um objeto em um movimento uniformemente acelerado. o Usuario deve informar a velocidade inicial, a aceleração e o tempo de deslocamento. Escreva um algoritmo que calcule e imprime a distancia percorrida pelo objeto.

# velocidade_inicial= float(input("Insira a velocidade inicial\n"))
# aceleracao= float(input("Insira a aceleração do objeto \n"))
# tempo= float(input("Insira o tempo de deslocamento em horas \n"))

# calculo = velocidade_inicial * tempo + (aceleracao* (tempo**2))/2
# print(f'A distancia percorrida é {calculo}km')


# _________________________________________________________________________________
# numero= int(input("Digite um valor"))

# if numero == 0:
#     print("O numero digitado é ZERO")
# elif numero % 2 == 0:
#     print("O numero digitado é par")
# else:
#     print ("O numero é impar")


# nome_paciente= (input("Insira o seu nome:\n"))
# peso= float(input("Insira o seu peso \n"))
# altura= float(input("Insira a sua altura \n"))
# calculo_imc= peso/(altura**2)

# if calculo_imc < 18.5:
#     print (f'O paciente {nome_paciente}está classificado como abaixo do peso.')

# elif calculo_imc >=18.5 and calculo_imc <24.9:
#     print(f'O paciente {nome_paciente} está classificado com peso normal.')

# elif calculo_imc >=25.00 and calculo_imc <29.9: 
#     print(f'O paciente {nome_paciente} está classificado com excesso de peso.')

# elif calculo_imc >=30 and calculo_imc <34.9:
#     print(f'Paciente {nome_paciente} está classificado com obesidade classe I.')

# elif calculo_imc >=35 and calculo_imc <39.9:
#     print(f'O paciente {nome_paciente} está classificado com obesidade classe II.')
    
# else:
#     print(f'O paciente {nome_paciente} está classificado com obesidade classe III.')