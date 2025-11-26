"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    sumas_por_letra_col1 = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            
            if len(columnas) >= 5:
                letra_columna_0 = columnas[0]
                pares_clave_valor_str = columnas[4]
                
                suma_valores_col5 = 0
                if pares_clave_valor_str:
                    pares = pares_clave_valor_str.split(',')
                    for par in pares:
                        _, valor_str = par.split(':')
                        suma_valores_col5 += int(valor_str)
                
                if letra_columna_0 in sumas_por_letra_col1:
                    sumas_por_letra_col1[letra_columna_0] += suma_valores_col5
                else:
                    sumas_por_letra_col1[letra_columna_0] = suma_valores_col5
    
    resultado_ordenado = {k: sumas_por_letra_col1[k] for k in sorted(sumas_por_letra_col1)}
    
    return resultado_ordenado