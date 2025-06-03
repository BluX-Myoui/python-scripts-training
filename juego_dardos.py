#Creamos un diccionario para los nombres con las puntuaciones, y cramos una variable False para ronda_ganada.

juego_terminado = False
jugadores = {}
for i in range(3):
    nombre = input(f"Introduce el nombre del jugador {i+1}: ")
    jugadores[nombre] = 121
#Mostramos los nombres registrados con su puntuacion.
print("JUGADORES REGISTRADOS:")
for nombre in jugadores:
    print("-",nombre,":" ,jugadores[nombre])
#creamos varios bucels for dentro de cada uno paso a paso en cuanto a rondas turnos y puntuacion
for ronda in range(0, 3):
    print(f"\nRONDA {ronda + 1}")
    ganadores = [] #
    for jugador in jugadores:
        print(f"\nTURNO DE {jugador}:")
        puntos_total_ronda = 0

        for dardo in range(1, 4):
            while True:
                    try: #verificamos que meta un numero
                        puntos = int(input(f"Puntos del dardo {dardo}: "))
                        puntos_total_ronda += puntos #suma de puntos entr si
                        break
                    except ValueError:
                        print("Debes poner un numero entero")
        jugadores[jugador] -= puntos_total_ronda #121 menos los puntos acumulados en la ronda
        print(f"Puntuación restante de {jugador}: {jugadores[jugador]} puntos")

#si alguine llega a 0 o menos se acaba la partida y muestra en pantalla el ganador
        if jugadores[jugador] <= 0:
            ganadores.append(jugador)
    if ganadores:
        print(f"\nJUEGO TERMINADO EN LA RONDA {ronda + 1}")
        print("GANADOR/ES: ")
        for nombre in ganadores:
            print("-", nombre)
        juego_terminado = True
        break
#juego_terminado cambia a ser true y sale del bucle y si nadie gana porque no queda en 0 o menos termina el juego
    if juego_terminado:
        break
if not juego_terminado:
    print("\nNadie ha logrado ganar el juego")

