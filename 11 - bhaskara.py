print("---EQUAÇÃO DO 2 GRAU---\n")

vA = int(input("Digite o valor A: "))
vB = int(input("Digite o valor B: "))
vC = int(input("Digite o valor C: "))

Delta = ((vB)**2)-4*vA*vC

x0 = int(-vB)/2*vA
x1 = int(-vB + (Delta ** 0.5))/2*vA
x2 = int(-vB - (Delta ** 0.5))/2*vA

if Delta > 0:
    print((f"\nO valor de x1 é: {x1}"))
    print((f"O valor de x2 é: {x2}"))
elif Delta < 0:
    print("A equação não possui raízes reais")
else:
    print(f"O valor único é: {x0}")