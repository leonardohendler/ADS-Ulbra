"""Problema:

Faça um algoritmo que verifique a aprovação de alunos com base em suas notas e presenças. O algoritmo deve receber três notas (AP1, AP2 e AS) e o número de presenças de um aluno (valor entre 1 e 24). A partir desses dados, o algoritmo deve calcular a nota final (PS) do aluno (soma das três notas) e verificar se o número de faltas é inferior ou igual a 5. O aluno poderá ser aprovado, realizar a Avaliação Final (AF) ou ser reprovado, conforme as regras a seguir.

Regras:

Se a nota final (PS) for igual ou superior a 6 e o número de faltas for igual ou inferior a 5, o aluno está aprovado.
Se a nota final (PS) for inferior a 6, mas o número de faltas for igual ou inferior a 5, o aluno deverá fazer a Avaliação Final (AF).
Se o número de faltas for superior a 5, o aluno estará reprovado, independentemente da nota.
O algoritmo deve ser capaz de receber e testar as notas de diversos alunos usando a estrutura WHILE. Após cada verificação, o algoritmo deve voltar para o menu inicial.

Menu de entrada:

1- VERIFICAR APROVAÇÃO

0- SAIR

Observações:

Não é obrigatório o uso de listas ou funções.
Exemplo de saída para o aluno:

"Parabéns, [NOME DO ALUNO], você foi aprovado!"

"Infelizmente, [NOME DO ALUNO], você foi reprovado por faltas..."
"[NOME DO ALUNO], você deverá fazer a Avaliação Final (AF)."""




print("--------------------------------------")
print("---MENU DE APROVAÇÃO - ULBRA TORRES---")
print("--1 - VERIFICAR APROVAÇÃO || 0 - SAIR--")

while True:

    opc = int(input("Digite a opção desejada!\n"))

    if opc == 0:
        break
    elif opc == 1:
        nome= input("Digite seu nome:\n")
        ap1 = float(input("Digite o valor da AP1:\n"))
        ap2 = float(input("Digite o valor da AP2:\n"))
        a_s = float(input("Digite o valor da AS:\n"))
        num_faltas= int(input("Digite o numero de faltas\n"))


        ps= ap1+ap2+a_s

        if ps >= 6 and num_faltas <=5:
            print(f"Parabéns,{nome}, você foi aprovado!")
        elif ps <6 and num_faltas <=5:
            print(f"{nome}, você deverá fazer a Avaliação Final (AF).")
        elif ps >= 6 and num_faltas > 5:
            print(f"Infelizmente, {nome}, você foi reprovado por faltas...")

    else: 
        print("Digite uma opção valida!")


# Você está desenvolvendo um algoritmo para um programa de conversão de unidades de medida. O programa deve exibir um menu de opções para que o usuário escolha a conversão desejada e, em seguida, solicitar os valores necessários para realizar a conversão correta. O programa deve repetir esse processo até que o usuário escolha a opção "SAIR".

# Menu de Opções:

# Quilômetros para Milhas
# Milhas para Quilômetros
# Metros para Pés
# Pés para Metros
# Centímetros para Polegadas
# Polegadas para Centímetros
# SAIR
# Regras de conversão:

# Quilômetros para Milhas: M = K * 0.621371
# Milhas para Quilômetros: K = M * 1.60934
# Metros para Pés: P = M * 3.28084
# Pés para Metros: M = P * 0.3048
# Centímetros para Polegadas: I = C * 0.393701
# Polegadas para Centímetros: C = I * 2.54
# Implemente o algoritmo que permita ao usuário escolher a conversão desejada e realizar a conversão correta da unidade de medida fornecida. Após exibir o resultado da conversão, o algoritmo deve retornar ao menu inicial para nova utilização.

# Lembre-se de tratar possíveis erros de entrada do usuário e fornecer mensagens claras para orientar o processo de conversão.

print("---------------------------------------")
print("----------MENU DE OPÇÕES:--------------")
print("---------------------------------------")
print(" DIGITE 1 : Quilômetros para Milhas")
print(" DIGITE 2 : Milhas para Quilômetros")
print(" DIGITE 3 : Metros para Pés")
print(" DIGITE 4 : Pés para Metros")
print(" DIGITE 5 :  Centímetros para Polegadas")
print(" DIGITE 6 : Polegadas para Centímetros")
print(" DIGITE 0 : SAIR")
print("---------------------------------------")
print("---------------------------------------")
    
while True:
    opc= int(input("Digite a opção desejada!\n"))
    if opc == 0:
        break
    elif opc == 1:
        k= float(input("Digite o km!\n"))
        milhas = k * 0.621371
        print(f"A conversão de km para milhas fica: {milhas} milhas")
    elif opc == 2: 
        milhas=float(input("Digite o valor em milhas!\n"))
        km = milhas * 1.60934
        print(f"A conversão de milhas para km é: {km} km")
    elif opc == 3:
        metros= float(input("Digite um valor em metros!\n")) 
        pes = metros * 3.28084
        print(f"A conversão de metros para pés é: {pes} pes")
    elif opc == 4: 
         pes1= float(input("Digite um valor em pes!\n"))
         m = pes1 * 0.3048
         print(f"A conversão de pes para metros é: {m} metros")
    elif opc == 5: 
        cm= float(input("Digite o valor em cm!\n"))
        polegadas = cm * 0.393701
        print(f"A conversão de cm para polegadas é: {polegadas} polegadas")
    elif opc == 6:
        p = float(input("Digite um valor em polegadas!\n"))
        c = p * 2.54
        print(f"A conversão de polegadas para cm é: {c} cm")
    else:
        print("Digite uma da opções do MENU!")     









 

    


