numero = None
def es_impar(numero):
    if numero % 2 == 1:
        return True
    else:
        return False

while True:
    entrada = input("DAME UN NUMERO: ")
    if entrada.lower() == "salir":
        print("PROGRAMA CERRADO CON ÉXITO")
        break
    try:
        numero = int(entrada)
        print("NUMERO VALIDO")
    except ValueError:
        print("NO ES UN NUMERO VALIDO")
        continue

    if es_impar(numero):
        print("ES IMPAR")
    else:
        print("ES PAR")