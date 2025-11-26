"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    sumas_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            
            if len(columnas) >= 4:
                valor_columna_1 = int(columnas[1])
                letras_columna_3 = columnas[3].split(',')
                
                for letra in letras_columna_3:
                    if letra in sumas_por_letra:
                        sumas_por_letra[letra] += valor_columna_1
                    else:
                        sumas_por_letra[letra] = valor_columna_1
    
    resultado_ordenado = {k: sumas_por_letra[k] for k in sorted(sumas_por_letra)}
    
    return resultado_ordenado