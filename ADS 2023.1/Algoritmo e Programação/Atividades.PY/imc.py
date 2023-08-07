import datetime as dt
lista = []
def calcula_imc(parametro_peso, parametro_altura):
    retorno_imc = parametro_peso / pow(parametro_altura,2)
    return retorno_imc

def classifica(parametro_imc):
    if parametro_imc < 18.5:
        return "Seu IMC é classificado como Muito Magro"
    if ((parametro_imc > 18.5) and (parametro_imc < 24.9)):
        return "Seu IMC é classificado como Normal"
    if ((parametro_imc > 24.9) and (parametro_imc < 29.9)):
        return "Seu IMC é classificado como Sobrepeso"    
    if ((parametro_imc > 29.9) and (parametro_imc < 34.9)):
        return "Seu IMC é classificado como Obesidade I"
    if ((parametro_imc > 34.9) and (parametro_imc < 39.9)):
        return "Seu IMC é classificado como Obesidade II"
    if (parametro_imc > 39.9):
        return "Seu IMC é classificado como Obesidade III"

while True:


    print("--------------------------------")
    print("Opção 0 : SAIR || Opção 1 : Calcular IMC || Opção 2 : LISTA DE CONSULTA")
    print("--------------------------------")
    opc=int(input("Digite a opção desejada:"))

    if opc == 0:
        break
    elif opc == 1:
        nome = input("Digite seu nome: ")
        peso = float(input("Digite o seu peso:"))
        altura = float(input("Digite a sua altura:"))
        data_avalia = dt.datetime.now()
        imc = calcula_imc(peso,altura)
        classificacao = classifica(imc)
        lista.append([nome, peso, altura, imc, classificacao, data_avalia])
        
        print('Olá :' + nome)
        print(f"Seu IMC é : {imc:.2f}")
        print(f"{classificacao}")
        print(f"Esta avaliação foi realizada em: {data_avalia}")
    elif opc == 2:  
        for item in lista:
            print("--------------------------------")
            print("--------------------------------")
            print("--------------------------------")
            print(f"Avaliado: {item[0]} | Peso: {item[1]}kg | Altura: {item[2]}m | IMC:{(item[3]):.2f}")
            print(f"Classificado:{item[4]} ")
            print(f"Avaliado em:{item[5]}")
            print("--------------------------------")
            print("--------------------------------")
            print("--------------------------------")
    else:
        print("Digite uma opção valida!!")