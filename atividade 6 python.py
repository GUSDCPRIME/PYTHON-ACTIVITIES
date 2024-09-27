print("Algoritmo do voto Obrigatório")
idade = int(input("Digite sua Idade: "))
if (idade >= 18 and idade < 65):
        print("Voto Obrigatório")
elif (16 <= idade < 18 or idade >= 65):
        print("Voto Opcional !!!")
else: print("Voto não permitido !!!")