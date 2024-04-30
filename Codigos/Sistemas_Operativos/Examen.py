#---------------------------------------------------
# Dante Alejandro Alegria Romero
# Examen segundo parcial
#---------------------------------------------------
#LIBRERIAS NECESARIAS
#Es necesrio instalar estas librerias
#Para hacerlo solo es pip install "nombre de la libreria"
# o en su defecto pip3 install "nombre de la libreria"
import numpy as np
import pyfiglet
import os

#---------------------------------------------------
#Funcion para encontrar la ultima aparicion de un elemento en una lista
def ultima_aparicion(lista, palabra):
    try:
        ultima_posicion = lista[::-1].index(palabra)
        return len(lista) - 1 - ultima_posicion
    except ValueError:
        return None
#---------------------------------------------------
#Funcion para pedir al usuario la informacion de los procesos
def PedirValores():
    NumeroP = int(input("Ingrese el numero de procesos: "))
    Informacion = []
    for i in range(NumeroP):
        print("Proceso ", i+1)
        Nombre = input("Nombre del proceso: ")
        Tiempo = int(input("Tiempo del proceso: "))
        Prioridad = int(input("Prioridad del proceso: "))
        Llegada = int(input("Tiempo de llegada del proceso: "))
        Informacion.append([Nombre, Tiempo, Prioridad, Llegada])
    return Informacion
#---------------------------------------------------
#Funcion para mostrar el menu
def Menu():
    print("Seleccione el algoritmo a utilizar: ")
    print("1.- Round Robin")
    print("2.- FIFO")
    print("3.- Salir")
    opcion = int(input("Opcion: "))
    if(opcion == 3):
        exit()
    while opcion < 1 or opcion > 2:
        print("Opcion no valida")
        opcion = int(input("Opcion: "))
    return opcion
#---------------------------------------------------
#Funcion para el algoritmo de Round Robin
def RoundRobin(Informacion):
    Organizada = []
    Quantum = int(input("Ingrese el quantum: "))
    TiempoActual = 0
    procesados = [] 
    for i in range(len(Informacion)):
        procesados.append([Informacion[i][0], Informacion[i][3], Informacion[i][1]])

    while Informacion:
        for i in range(len(Informacion)):
            if Informacion[i][3] <= TiempoActual:
                for j in range(Quantum):
                    if Informacion[i][1] == 0:
                        Informacion.remove(Informacion[i])
                        break
                    Organizada.append(Informacion[i][0])
                    Informacion[i][1] -= 1
                    TiempoActual += 1
                    if j == Quantum - 1:
                        Informacion.append(Informacion.pop(i))
                        break
                break
            if i == len(Informacion) - 1:
                TiempoActual += 1
                Organizada.append("Vacio")

    print("Procesos Organizados:", Organizada)
    print("Proceso/ Tiempo de llegada/ Tiempo de Salida")
    for i in range(len(procesados)):
        print(procesados[i][0], procesados[i][1], ultima_aparicion(Organizada, procesados[i][0])) 

#---------------------------------------------------
#Funcion para el algoritmo de FIFO
def FIFO(Informacion):
    Organizada = []
    TiempoActual = 0
    procesados = [] 
    for i in range(len(Informacion)):
        procesados.append([Informacion[i][0], Informacion[i][3], Informacion[i][1]])

    while Informacion:
        for i in range(len(Informacion)):
            if Informacion[i][3] <= TiempoActual:
                for j in range(Informacion[i][1]):
                    Organizada.append(Informacion[i][0])
                    TiempoActual += 1
                    Informacion[i][1] -= 1
                Informacion.remove(Informacion[i])
                break
            else:
                TiempoActual += 1
                Organizada.append("Vacio")
    print("Procesos Organizados:", Organizada)
    print("Proceso/ Tiempo de llegada/ Tiempo de Salida")
    for i in range(len(procesados)):
        print(procesados[i][0], procesados[i][1], ultima_aparicion(Organizada, procesados[i][0])) 

def LLenadoAutomatico():
    n = int(input("Ingrese el numero de procesos: "))
    Informacion = []
    for i in range(n):
        Informacion.append(["P" + str(i), np.random.randint(1, 10), np.random.randint(1, 10), np.random.randint(0, 10)])
    return Informacion
#---------------------------------------------------
def main():
    os.system('cls')
    print(pyfiglet.figlet_format("Administrador de Procesos", font="larry3d", justify="center", width=100))
    opcion = Menu()
    opcion2 = int(input("Desea ingresar los valores de los procesos? (1.- Si, 2.- No): "))
    if opcion == 1:
        os.system('cls')
        print(pyfiglet.figlet_format("Round Robin", font="larry3d", justify="center", width=100))
        print("-----------------------------------")
        if opcion2 == 1:
            Informacion = PedirValores()

        else:
            Informacion = LLenadoAutomatico()
        print("-----------------------------------")
        print("Nombre | Tiempo | Prioridad | Llegada")
        print("Procesos: ", Informacion)
        print("-----------------------------------")
        RoundRobin(Informacion)
        print("-----------------------------------")
        input("Presione enter para continuar..." + '\n')
        main()
    elif opcion == 2:
        os.system('cls')
        print(pyfiglet.figlet_format("FIFO", font="larry3d", justify="center", width=100))
        print("-----------------------------------")
        if opcion2 == 1:
            Informacion = PedirValores()
        else:
            Informacion = LLenadoAutomatico()
            #Imprimo la informacion
        print("-----------------------------------")
        print("Nombre | Tiempo | Prioridad | Llegada")
        print("Procesos: ", Informacion)
        print("-----------------------------------")
        FIFO(Informacion)
        print("-----------------------------------")
        input("Presione enter para continuar..." + '\n')
        main()
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    main()
