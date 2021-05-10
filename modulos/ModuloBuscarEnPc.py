import os
from playsound import playsound
import webbrowser


def buscar_musica(valor):
    buscar = str(valor)
    print(buscar)
    directorio = "Aqui va el directorio de la musica"  # os.getcwd()
    # total = 0
    print(directorio)

    for root, dir, ficheros in os.walk(directorio):
        for fichero in ficheros:
            if buscar in fichero.lower():
                ruta_fichero=root + "\\" + fichero
                print(ruta_fichero)
                webbrowser.open(ruta_fichero)
                return fichero
                # print(root + "\\" + fichero)
                # total += 1

    # print("En total hay", total, " archivos con", buscar)


