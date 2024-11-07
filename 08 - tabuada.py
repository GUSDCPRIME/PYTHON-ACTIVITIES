#Esse código tem como função selecionar um número digitado e retornar a sua tabuada

valor = int(input("Digite um número para a tabuada: "))
contador = 0

print("\nTabuada de ", valor, '\n')
while contador <= 10:
    print(valor," x ",contador, " = ", valor*contador )
    contador += 1

print("\nFim do Código :)\n")