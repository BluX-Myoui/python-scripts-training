numero = None
numero2 = None
#Solicitamos un numero, validamos que sea un numero y miramos si es par o impar
while True:
    entrada = input("Dame el numero [1] o si prefieres salir escribe 'salir': ")
    if entrada.lower() == "salir":
        break
    if entrada.isdigit():
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"Numero [1] valido y par: ({numero})")
            break
        else:
            print(f"Numero [1] valido e impar: ({numero})")
            break
    else:
        print("se acabo")

#Solicitamos otro numero pero en este caso lo validamos con "try/except" y comprobamos que se apar o impar
while True:
    entrada2 = input("Dame el numero [2] o si prefieres salir escribe 'salir': ")
    if entrada2.lower() == "salir":
        break
    try:
        numero2 = int(entrada2)
        if numero2 % 2 == 0:
            print(f"Numero [2] valido y par: ({numero2})")
            break
        else:
            print(f"Numero [2] valido e impar: ({numero2})")
            break
    except ValueError:
        print("se acabo")

#Comprobamos si se ingresaron los dos numeros y si se acabó el programa
if entrada.lower() == "salir" and entrada2.lower() == "salir":
    print("EL PROGRAMA SE TERMINO CORRECTAMENTE")
elif entrada.lower() == "salir":
    print(f"EL PROGRAMA DETECTO SOLO EL NUMERO [2]: {numero2}")
elif entrada2.lower() == "salir":
    print(f"EL PROGRAMA DETECTO SOLO EL NUMERO [1]: {numero}")
else:
    print(f"\nTUS NUMEROS SON EL {numero} y {numero2}")