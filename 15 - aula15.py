valor = 0

while valor != 6:
    print("~~~~~~CALCULADORA DAS OPERAÇÕES BÁSICAS~~~~~~\n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da divisão")
    print("6. sair\n")
    valor = int(input("Digite uma opção: "))

    if valor == 1:
        número1 = float(input("Digite um valor: "))
        número2 = float(input("Digite outro valor: "))
        resultado = número1 + número2
        print(f"O resultado da soma é: {resultado}")
    elif valor == 2:
        número1 = float(input("Digite um valor: "))
        número2 = float(input("Digite outro valor: "))
        resultado = número1 - número2
        print(f"O resultado da subtração é: {resultado}")
    elif valor == 3:
        número1 = float(input("Digite um valor: "))
        número2 = float(input("Digite outro valor: "))
        resultado = número1 * número2
        print(f"O resultado da multiplicação é: {resultado}")
    elif valor == 4:
        número1 = float(input("Digite um valor: "))
        número2 = float(input("Digite outro valor: ")) 
        if número2 == 0:
           print("Erro: Divisão por zero não é permitida.\n")
        else:
            resultado = número1 / número2
            print(f"O resultado da divisão é: {resultado}")
    elif valor == 5:
        número1 = float(input("Digite um valor: "))
        número2 = float(input("Digite outro valor: "))
        if número2 == 0:
           print("Erro: Divisão por zero não é permitida.\n")
        else:
            resultado = número1 % número2
            print(f"O resto da divisão é: {resultado}")

    elif valor == 6:
        print("Código finalizando...\n")
    else:
        print("Valor inválido")

print("Código finalizado!!!")
