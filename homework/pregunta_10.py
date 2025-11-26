"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_10():
    """
    Retorne una lista de tuplas que contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    resultados = []

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            
            if len(columnas) >= 5:
                letra_columna_0 = columnas[0]
                
                elementos_columna_3 = columnas[3].split(',')
                cantidad_elementos_columna_3 = len(elementos_columna_3)
                if elementos_columna_3 == ['']:
                    cantidad_elementos_columna_3 = 0
                
                elementos_columna_4 = columnas[4].split(',')
                cantidad_elementos_columna_4 = len(elementos_columna_4)
                if elementos_columna_4 == ['']:
                    cantidad_elementos_columna_4 = 0
                
                resultados.append((letra_columna_0, cantidad_elementos_columna_3, cantidad_elementos_columna_4))
    
    return resultados