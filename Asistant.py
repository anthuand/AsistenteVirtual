from modulos.ModuloHablar import decir
from modulos.ModuloEscuchar import escuchar
from modulos.ModuloWiki import wikiSearch
from modulos.ModuloTraduccion import traducir
from modulos.ModuloWit_ai import witai
from modulos.ModuloBuscarEnPc import buscar_musica
import time
import pywhatkit
from pynput import keyboard as kb

def saludo():
    decir("Hola mi nombre es Viernes , Soy tu asistente personal. Dime tu nombre: ")
    usuario = escuchar()
    decir("Hola" + str(usuario) + ". Venga pideme lo que quieras")


def llamar_comando(comand, valor):
    if comand == 'saludo':
        saludo()
    elif comand == 'hora':
        hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        decir(hora)
    elif comand == 'wikipedia_search':
        if valor:
            decir(wikiSearch(valor))
    elif comand == 'traducir':
        if valor:
            traducir(valor)
    elif comand == 'google_search':
        if valor:
            pywhatkit.search(valor)
    elif comand == 'buscar_musica':
        if valor:
            buscar_musica(valor)
    elif comand == 'mensaje':
        if valor:
            hora = time.strftime('%H', time.localtime())
            min = time.strftime('%M', time.localtime())
            seg = time.strftime('%S', time.localtime())
            m=int(min)+1
            decir("que quieres poner en el mensaje")
            texto=escuchar()
            pywhatkit.sendwhatmsg("+55555555555", texto,int(hora),m)
    elif comand == 'youtube_search':
        if valor:
            pywhatkit.playonyt(valor)



def main():
    text = 'as'
    while text != 'salir':
        x=input("presiona 'a' para empezar a grabar")
        if x == 'a':
            text = escuchar()
            com, val = witai(text)
            if com is None or val is None:
                print("no me llego nada de respuesta")
            else:
                try:
                    llamar_comando(com, val)
                except:
                    print('Algo sucedio cai en un error')


    decir('Bueno fue un placer ayudarte , nos vemos luego')


if __name__ == '__main__':
    main()
