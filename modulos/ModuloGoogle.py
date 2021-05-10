# importar la funcion de busqueda
from googlesearch import search
import webbrowser



def googleSearch(query):
    tld = "com"
    lang = "en"
    num = 2
    start = 0
    stop = num
    pause = 2.0
    # ahora ejecutamos la busqueda con la funcion search y pasamos como parametro la consulta
    # asignamos cada parametro de variable local con los parametros correspondiente de la funcion search
    results = search(query, tld=tld, lang=lang, num=num, start=start, stop=stop, pause=pause)
    # hacemos un recorrido de los resultados, cada resultado es una URL
    for r in results:
        print(r)  # la variable "r" contiene la url resultados
        webbrowser.open(r)


googleSearch("pasto")






"""
query: Consulta de búsqueda
ltd: dominio de búsqueda
lang: lenguaje de búsqueda
num: numero de resultados para obtener
start: resultado inicial, podemos saltar por ejemplo los primeros 10 o 100 resultados
stop: Parar, si el valor es None la busqueda seria infinita / infinite loop o hasta que se terminen los resultados
pause: Lapso entre peticiones HTTP, una pausa muy corta puede hacer que google nos banee por IP y una pausa muy larga hace que el script vaya lento.
"""