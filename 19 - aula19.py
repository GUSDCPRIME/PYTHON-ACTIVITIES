nome = input("Digite o seu nome: ")
print(f"Bem vindo(a) {nome}, escolha a sua conversão de temperatura:\n")

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

while True:
        print("Conversor de Temperaturas:")
        print("1. Converter de Fahrenheit para Kelvin")
        print("2. Converter de Fahrenheit para Celsius")
        print("3. Converter de Kelvin Fahrenheit")
        print("4. Converter de Kelvin para Celsius")
        print("5. Converter de Celsius para Fahrenheit")
        print("6. Converter de Celsius para Kelvin")
        print("7. Sair")

        opção = int(input("Digite a sua opção: "))

        if opção == 1:
            temperatura = float(input("Digite a sua temperatura: "))
            resultado = fahrenheit_para_kelvin(temperatura)
            print(f"{temperatura}°F é igual a: {resultado}K")

        elif opção == 2:
            temperatura = float(input("Digite a sua temperatura: "))
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura}°F é igual a: {resultado}°C")

        elif opção == 3:
            temperatura = float(input("Digite a sua temperatura: "))
            resultado = kelvin_para_fahrenheit(temperatura)
            print(f"{temperatura}K é igual a: {resultado}°F")

        elif opção == 4:
            temperatura = float(input("Digite a sua temperatura: "))
            resultado = kelvin_para_celsius(temperatura)
            print(f"{temperatura}K é igual a: {resultado}°C")
        elif opção == 5:
            temperatura = float(input("Digite a sua temperatura: "))
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura}°C é igual a: {resultado}°F")
        elif opção == 6:
            temperatura = float(input("Digite a sua temperatura: "))
            resultado = celsius_para_kelvin(temperatura)
            print(f"{temperatura}°C é igual a: {resultado}K")
        elif opção == 7:
            print("Saindo...")
            break
        else:
            print("OPÇÃO INVÁLIDA!!!")

print("\nCódigo finalizado :)")