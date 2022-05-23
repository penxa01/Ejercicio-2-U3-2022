from ClaseRamo import ramo
from ManejadorFlores import flores
import os

class ramos:
    __ramosVendidos = None

    def __init__(self):
        self.__ramosVendidos = []
    
    def agregarRamo(self,ListaFlores):
        tamaño = input("Ingrese tamaño del ramo\n")
        NuevoRamo = ramo(tamaño)
        listadoFlores = ListaFlores.getLista()

        dato = int(input("Ingrese nro de flor que desea(0 para finalizar)"))
        os.system("cls")
        contadorFlores = 0

        while (dato != 0) and (contadorFlores < 4):
            indice = ListaFlores.buscarFlor(dato)
            if (indice != -1):
                contadorFlores +=1
                NuevaFlor = listadoFlores[indice]
                NuevoRamo.agregarFlor(NuevaFlor)
            else:
                print("Flor no encontrada")
            dato = int(input("Ingrese siguiente flor a agregar(0 para finaliar)"))
            os.system("cls")

        if (contadorFlores == 4):
            print("Ya se alcanzaron las 4 flores")

        input("ENTER PARA CONTINUAR")
        os.system("cls")
        
        if isinstance(NuevoRamo,ramo):
            NuevoRamo.mostrar()
            input("ENTER PARA CONTINUAR")
            os.system("cls")
            self.__ramosVendidos.append(NuevoRamo)
        else:
            print("{} no es un ramo".format(NuevoRamo))
        
        

