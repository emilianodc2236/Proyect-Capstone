#AUTOR: Emiliano Delgado 


#***PROYECTO: CAPSTONE. JUEGO BATTLESHIP***
#Bibliotecas (estilos y numeros aleatorios)
import copy
import random
from colorama import init, Fore, Back, Style
init()

#abrir un archivo
def leer_archivo(archivo):
    
    contenido = []
    
    archivo = open("manual.txt", 'r')
    for linea in archivo:
        contenido.append(linea.strip())
    archivo.close()    
    for linea in contenido:
        print(linea)


#Funciones generales (reutilizadas)

#Para construir un tablero:
def filaLinea(x):
    columna = ""
    for c in range(x):
        columna += "- "
    return columna

def construirTablero(numF,numC):
    tablero = []
    c = "  "
    for columna in range(numC):
        c += str(columna+1) + " "
    tablero.append(c)
    for fila in range(numF):
        f = str(fila+1) + " "
        f += filaLinea(numC)
        tablero.append(f)
    return tablero

def mostrarTablero(tablero, tipo):
    if tipo == True:
        color_fondo = Back.BLACK + Fore.CYAN
    else:
        color_fondo = Back.BLACK + Fore.RED
    for row in tablero:
        print(color_fondo + row + Style.RESET_ALL)

#Para duplicar el tablero:
def duplicarTablero(tablero):
    return copy.deepcopy(tablero)

#Para moificar los tableros
def modificarVertical(tablero,fila,columna):
    elementos = list(tablero[fila])
    for c in elementos:
        if c == " ":
            elementos.remove(c)
    elementos[columna] = "B"
    resultado = ""
    for x in elementos:
        resultado += x + " "
    return resultado

def modificarHorizontal(tablero,fila,columna,tamaño):
    elementos = list(tablero[fila])
    for c in elementos:
        if c == " ":
            elementos.remove(c)
    if columna > tamaño:
        for x in range(tamaño,columna+1):
            colision = barcosChocan(tablero,fila,x)
            if colision == True:
                return True
            elementos[x] = "B"
    else:
        for x in range(columna,tamaño):
            colision = barcosChocan(tablero,fila,x)
            if colision == True:
                return True
            elementos[x] = "B"
    resultado = ""
    for x in elementos:
        resultado += x + " "
    return resultado

#Para verificar la posición de barcos
def barcosChocan(tablero,fila,columna):
    elementos = list(tablero[fila])
    for c in elementos:
        if c == " ":
            elementos.remove(c)
    y = elementos[columna]
    if y == "B" or y == "O" or y.isdigit():
        return True
    return False

#Para colocar los barcos
def colocarBarcos(tablero, tamaño):
    print("\n" + Style.BRIGHT + f"Posiciona el barco de tamaño: {tamaño}." + Style.RESET_ALL)
    filasTotales = (len(tablero)) - 1
    columnasDisponibles = list(tablero[1])
    for c in columnasDisponibles:
        if c == " ":
            columnasDisponibles.remove(c)
    columnasTotales = (len(columnasDisponibles)) - 1
    fila = int(input("¿En qué fila te gustaría colocar el barco?: "))
    columna = int(input("¿En qué columna te gustaría colocarlo?: "))
    
    while fila > (filasTotales) or columna > (columnasTotales) or fila < 1 or columna < 1:
        print("\n" + Style.BRIGHT + "Por favor, introduce valores dentro del tablero." + Style.RESET_ALL)
        fila = int(input("¿En qué fila te gustaría colocar el barco?: "))
        columna = int(input("¿En qué columna te gustaría colocarlo?: "))
        
    orientacion = input("¿Quieres que esté en vertical(v) u horizontal(h)? (escribe v / h): ")
    while orientacion.lower() != "v" and orientacion != "h":
        print("\n" + Style.BRIGHT + "Por favor, elige una de las letras indicadas." + Style.RESET_ALL)
        orientacion = input("¿Quieres que esté en vertical(v) u horizontal(h)? (escribe v / h): ")
    if orientacion.lower() == "v":
        direccion = input("¿Quieres que vaya hacia arriba(a) o hacia abajo(b)? (escribe a / b): ")
        while direccion.lower() != "a" and direccion != "b":
            print("\n" + Style.BRIGHT + "Por favor, elige una de las letras indicadas." + Style.RESET_ALL)
            direccion = input("¿Quieres que vaya hacia arriba(a) o hacia abajo(b)? (escribe a / b): ")
        if direccion.lower() == "a":
            tamaño = fila - tamaño
            for x in range(fila, tamaño, -1):
                colision = barcosChocan(tablero, x, columna)
                if colision == True or x == 0:
                    return False
                resultado = modificarVertical(tablero, x, columna)
                tablero[x] = resultado
            return tablero
        elif direccion.lower() == "b":
            tamaño = tamaño + (fila - 1)
            if tamaño > filasTotales:
                return False
            for x in range(fila, tamaño + 1):
                colision = barcosChocan(tablero, x, columna)
                if colision == True:
                    return False
                resultado = modificarVertical(tablero, x, columna)
                tablero[x] = resultado
            return tablero
    if orientacion.lower() == "h":
        direccionHorizontal = input("¿Quieres que vaya hacia la izquierda(i) o hacia la derecha(d)? (escribe i / d): ")
        while direccionHorizontal.lower() != "i" and direccionHorizontal != "d":
            print("\n" + Style.BRIGHT + "Por favor, elige uno de los números indicados." + Style.RESET_ALL)
            direccionHorizontal = input("¿Quieres que vaya hacia la izquierda(i) o hacia la derecha(d)? (escribe i / d): ")
        if direccionHorizontal.lower() == "i":
            tamaño = (columna + 1) - tamaño
            resultado = modificarHorizontal(tablero, fila, columna, tamaño)
            if resultado == True:
                return False
            tablero[fila] = resultado
            return tablero
        elif direccionHorizontal.lower() == "d":
            tamaño = (tamaño - 1) + columna
            if tamaño > columnasTotales:
                return False
            resultado = modificarHorizontal(tablero, fila, columna, tamaño + 1)
            if resultado == True:
                return False
            tablero[fila] = resultado
            return tablero

#Para crear el barco
def barcosCpu(tablero, tamaño):
    filasTotales = (len(tablero)) - 1
    columnasDisponibles = list(tablero[1])
    for c in columnasDisponibles:
        if c == " ":
            columnasDisponibles.remove(c)
    columnasTotales = (len(columnasDisponibles)) - 1
    fila = random.randint(1, filasTotales)
    columna = random.randint(1, columnasTotales)
    orientacion = random.randint(1, 2)
    if orientacion == 1:
        direccion = random.randint(1, 2)
        if direccion == 1:
            tamaño = fila - tamaño
            for x in range(fila, tamaño, -1):
                colision = barcosChocan(tablero, x, columna)
                if colision == True or x == 0:
                    return False
                resultado = modificarVertical(tablero, x, columna)
                tablero[x] = resultado
            return tablero
        
        elif direccion == 2:
            tamaño = tamaño + (fila - 1)
            if tamaño > filasTotales:
                return False
            for x in range(fila, tamaño + 1):
                colision = barcosChocan(tablero, x, columna)
                if colision == True:
                    return False
                resultado = modificarVertical(tablero, x, columna)
                tablero[x] = resultado
            return tablero

    if orientacion == 2:
        direccionHorizontal = random.randint(1, 2)
        if direccionHorizontal == 1:
            tamaño = (columna + 1) - tamaño
            resultado = modificarHorizontal(tablero, fila, columna, tamaño)
            if resultado == True:
                return False
            tablero[fila] = resultado
            return tablero
        elif direccionHorizontal == 2:
            tamaño = (tamaño - 1) + columna
            if tamaño > columnasTotales:
                return False
            resultado = modificarHorizontal(tablero, fila, columna, tamaño)
            if resultado == True:
                return False
            tablero[fila] = resultado
            return tablero

#Para disparar
def disparosBarcos(tableroCpu, tableroDisparo):
    filasTotales = (len(tableroDisparo)) - 1
    columnasDisponibles = list(tableroDisparo[1])
    for c in columnasDisponibles:
        if c == " ":
            columnasDisponibles.remove(c)
    columnasTotales = (len(columnasDisponibles)) - 1
    fila  = int(input("¿En qué fila deseas lanzar el disparo?: "))
    columna = int(input("¿En qué columna deseas lanzar el disparo?: "))
    
    while fila < 1 or fila > filasTotales or columna < 1 or columna > columnasTotales:
        print("\n" + Style.BRIGHT + "Error: Por favor, introduce valores dentro del tablero." + Style.RESET_ALL)
        fila = int(input("¿En qué fila deseas lanzar el disparo?: "))
        columna = int(input("¿En qué columna deseas lanzar el disparo?: "))

    impacto = barcosChocan(tableroCpu, fila, columna)
    filaDisparo = list(tableroDisparo[fila])
    filaCpu = list(tableroCpu[fila])
    if impacto == True:
        for c in filaDisparo:
            if c == " ":
                filaDisparo.remove(c)
        filaDisparo[columna] = "O"
        for c in filaCpu:
            if c == " ":
                filaCpu.remove(c)
        filaCpu[columna] = "O"
    else:
        for c in filaDisparo:
            if c == " ":
                filaDisparo.remove(c)
        filaDisparo[columna] = "X"
        
        for c in filaCpu:
            if c == " ":
                filaCpu.remove(c)
        filaCpu[columna] = "X"
    resultado = ""
    
    for x in filaDisparo:
        resultado += x + " "
    tableroDisparo[fila] = resultado
    resultado = ""
    for x in filaCpu:
        resultado += x + " "
    tableroCpu[fila] = resultado
    return tableroDisparo

#Disparos CPU
def disparoBarcosCpu(tableroUsuario):
    filasTotales = (len(tableroUsuario)) - 1
    columnasDisponibles = list(tableroUsuario[1])
    for c in columnasDisponibles:
        if c == " ":
            columnasDisponibles.remove(c)
    columnasTotales = (len(columnasDisponibles)) - 1
    fila = random.randint(1, filasTotales)
    columna = random.randint(1, columnasTotales)
    impacto = barcosChocan(tableroUsuario, fila, columna)
    filaUsuario = list(tableroUsuario[fila])
    if impacto == True:
        for c in filaUsuario:
            if c == " ":
                filaUsuario.remove(c)
        filaUsuario[columna] = "O"
    else:
        for c in filaUsuario:
            if c == " ":
                filaUsuario.remove(c)
        filaUsuario[columna] = "X"
    resultado = ""
    for x in filaUsuario:
        resultado += x + " "

    tableroUsuario[fila] = resultado
    return tableroUsuario

#Para verificar quien gana
def verificarGanador(tablero):
    barcosRestantes = 0
    for fila in tablero:
        for elemento in fila:
            if elemento == "B":
                barcosRestantes += 1
    if barcosRestantes == 0:
        return True
    return False

def principal():
    manualDeUsuario = "manual.txt"
    #leer_archivo("manual.txt")
    start = input(Style.BRIGHT + "¿Te gustaría jugar una partida de BattleShip? (si/no): " + Style.RESET_ALL)
    while start.lower() != "si" and start.lower() != "no":
        print('Escribe "si" o "no", por favor.')
        start = input(Style.BRIGHT + "¿Te gustaría jugar una partida de BattleShip? (si/no): " + Style.RESET_ALL)
    while start.lower() == "si":
        print(Style.BRIGHT + "¡GENIAL! ¡Vamos a comenzar!" + Style.RESET_ALL)
        print("\n" + Style.BRIGHT + "Debes crear un tablero de mínimo 5x5." + Style.RESET_ALL)
        filas = int(input("¿Cuántas filas deseas que tenga el tablero?: "))
        columnas = int(input("¿Cuántas columnas deseas que tenga el tablero?: "))
        
        while filas < 5 or columnas < 5:
            print("\n" + Style.BRIGHT + "El tamaño mínimo del tablero es de 5x5." + Style.RESET_ALL)
            filas = int(input("¿Cuántas filas deseas que tenga el tablero?: "))
            columnas = int(input("¿Cuántas columnas deseas que tenga el tablero?: "))
            
        tablero = construirTablero(filas, columnas)
        mostrarTablero(tablero, True)
        copiaTableroUsuario = duplicarTablero(tablero)
        for tamañoBarco in range(2, 5):
            tableroTemporal = duplicarTablero(copiaTableroUsuario)
            copiaTableroUsuario = colocarBarcos(copiaTableroUsuario, tamañoBarco)
            while copiaTableroUsuario == False:
                print("\n" + Style.BRIGHT + "La posición del barco no es válida, inténtalo de nuevo." + Style.RESET_ALL)
                copiaTableroUsuario = colocarBarcos(duplicarTablero(tableroTemporal), tamañoBarco)
            else:
                mostrarTablero(copiaTableroUsuario, True)
        print("\n")
        copiaTableroCpu = duplicarTablero(tablero)
        for tamañoBarco in range(2, 5):
            tableroTemporalCpu = duplicarTablero(copiaTableroCpu)
            copiaTableroCpu = barcosCpu(copiaTableroCpu, tamañoBarco)
            while copiaTableroCpu == False:
                copiaTableroCpu = barcosCpu(duplicarTablero(tableroTemporalCpu), tamañoBarco)
        #mostrarTablero(copiaTableroCpu, False)
        tableroDisparo = duplicarTablero(tablero)
        #print("\n")
        mostrarTablero(tableroDisparo, False)
        print("\n" + Style.BRIGHT + "¡Comienza la partida!" + Style.RESET_ALL)
        disparoUsuario = disparosBarcos(copiaTableroCpu, tableroDisparo)
        juegoUsuario = verificarGanador(copiaTableroCpu)
        disparoCpu = disparoBarcosCpu(copiaTableroUsuario)
        juegoCpu = verificarGanador(disparoCpu)
        print("\n")
        mostrarTablero(disparoCpu, True)
        print("\n")
        mostrarTablero(disparoUsuario, False)
        
        while juegoUsuario == False and juegoCpu == False:
            disparoUsuario = disparosBarcos(copiaTableroCpu, tableroDisparo)
            juegoUsuario = verificarGanador(copiaTableroCpu)
            disparoCpu = disparoBarcosCpu(copiaTableroUsuario)
            juegoCpu = verificarGanador(disparoCpu)
            print("\n")
            mostrarTablero(disparoCpu,True)
            print("\n")
            mostrarTablero(disparoUsuario,False)
            
            #mostrarTablero(disparoCpu, True)
        if juegoUsuario == True:
            print("\n" + Style.BRIGHT + "¡FELICIDADES, GANASTE!" + Style.RESET_ALL)
        elif juegoCpu == True:
            print("\n" + Style.BRIGHT + "¡Vaya, perdiste!" + Style.RESET_ALL)
            print(Style.BRIGHT + "¡Mejor suerte la próxima vez!" + Style.RESET_ALL)
        
        start = input("\n" + Style.BRIGHT + "¿Te gustaría jugar otra vez? (si/no): " + Style.RESET_ALL)
        while start.lower() != "si" and start.lower() != "no":
            print('Escribe "si" o "no", por favor.')
            start = input(Style.BRIGHT + "¿Te gustaría jugar otra vez? (si/no): " + Style.RESET_ALL)
    else:
        print("\n" + Style.BRIGHT + "¡Hasta la próxima!" + Style.RESET_ALL)
        print("¡Adiós! ;)" + Style.RESET_ALL)

principal()



