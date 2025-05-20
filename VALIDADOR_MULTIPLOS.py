# Pedir un número entero positivo y validarlo con isdigit()
while True:
    entrada1 = input("Dame un numero: ")

    if entrada1.isdigit():
        numero = int(entrada1)
        if numero > 0:
            print("Numero 1 valido y mayor que 0")
            break
    else:
        print("Por favor ingrese un numero positivo")

# Pedir segundo número y validar con try/except
while True:

    entrada2 = input("Dame otro numero: ")

    try:

        numero2 = int(entrada2)
        if numero2 > 0:
            print("NUMERO 2 entero y positivo\n")
            break
        else:
            print("NUMERO NEGATIVO VUELVA A SELECCIONAR UN NUMERO")

    except ValueError:
        print("Por favor ingrese numeros validos")

# Verificar si el segundo número es múltiplo del primero
print(f"{numero} y {numero2} son validos para la operacion")

if numero2 % numero == 0:
    print(f"El {numero2} es multiplo del {numero}")

else:
    print(f"El {numero2} no es multiplo del {numero}")

