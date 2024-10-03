13-Funções
# Declaração da função exibirmensagem(nome)
def exibirmensagem(nome,idade):
    print(f"Olá, {nome} com {idade}!")

def somar(a,b):
    return a + b

def calculadoraAreaCirculo(raio):
    area = 3.1415 * raio ** 2
    return area
# início do meu algoritmo
nome = input("Digite o seu nome: ")
idade =input("Digire sua idade: ")
exibirmensagem(nome,idade) # Exibe a mensagem com nome do usuário.

# chamando funções com retorno
valorA = int(input("Digite o primeiro numero: "))
valorB = int(input("Digite o segunto numero: "))
resultado = somar(valorA, valorB)
print(f"O resultado da som = {resultado}")

# calcular area do circulo
print("Área do circulo")
raio = float(input("digite o valor do raio: "))
area = calculadoraAreaCirculo(raio)
print(f"Área do circulo: {area:.2f}") # Exibe a mensagem com nome do