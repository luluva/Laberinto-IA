from BRsin import *
from BRcon import *
import random
import os

print ("///////////////    LABERINTO    /////////////// \n")

num = int(input("Ingrese el Tamanio del laberinto: "))
obs = int(input("Ingrese la Cantidad de Obstaculos: "))

def gLaberinto(n = num): 
    laberinto = []
    for i in range(n):
        laberinto.append([' ' for j in range(n)])

    for i in range(obs):
        laberinto[random.randint(0, obs - 1)][random.randint(0, obs - 1)] = '|'
    return laberinto

def imprimir(laberinto):
    for i in range(len(laberinto)):
        print(laberinto[i])
        
def solA(ruta, laberinto):
    for i in  range(len(ruta)):
        laberinto[ruta[i][0]][ruta[i][1]] = '-'
        if i >=  len(ruta)-1:
            laberinto[ruta[i][0]][ruta[i][1]] = 'F'

def menu():

    os.system('clear')
    print ("Seleccione una opcion")
    print ("\t1 - Laberinto Resuelto con Razonamiento")
    print ("\t2 - Laberinto Resuelto sin Razonamiento")
    print ("\t3 - Laberinto Resuelto sin&con Razonamiento")
    print ("\t4 - Salir")

while True:
    menu()
    opcionMenu = input("")
    if opcionMenu=="1":
        print ("///////////////    LABERINTO con Razonamiento /////////////// \n")

        laberinto = gLaberinto()
        inicio = (0, 0)    
        final = (num - 1 , random.randint ( 0 , num -  1 ))
        ruta = aEstrella(laberinto, inicio, final)
        solA(ruta, laberinto)
        imprimir(laberinto)
        input("Para Continuar pulse cualquier tecla, Ingrese una opcion")
    elif opcionMenu=="2":
         print ("///////////////    LABERINTO sin Razonamiento   /////////////// \n")

         laberinto = gLaberinto()
         inicio = (0, 0)   
         final = (num - 1 , random.randint ( 0 , num -  1 ))
         ruta = aEstrella(laberinto, inicio, final)
         busqueda(laberinto, inicio, final)
         imprimir(laberinto)
         input("Para Continuar pulse cualquier tecla, Ingrese una opcion")
    elif opcionMenu=="3":   
         print ("///////////////    LABERINTO    /////////////// \n")

         laberinto = gLaberinto()
         inicio = (0, 0)    
         final = (num - 1 , random.randint ( 0 , num -  1 ))
         ruta = aEstrella(laberinto, inicio, final)
         busqueda(laberinto, inicio, final)
         solA(ruta, laberinto)
         imprimir(laberinto)
         input("Para Continuar pulse cualquier tecla, Ingrese una opcion")
    elif opcionMenu=="4":
         break
    else:
        print("")
        input("Ingrese un digito del 1 al 4, Ingrese una opcion")


	


