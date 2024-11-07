contador = 0

while contador <= 100:
    contador += 1
    if contador == 6:
        print('Não vou mostrar o 6')
        continue # Interrompe a interação atual  volta para o início do loop
    elif contador  >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}')
        continue # Interrompe a interação atual  volta para o início do loop
    elif contador == 41:
        break # Interrompe o loop completamente quando o contador chega a 40
    print(contador)
print('Acabou')
