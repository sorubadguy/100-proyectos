"""
5. Normalización de datos
**Descripción:** Crear una función que normalice una lista de valores entre 0 y 1.  
**Objetivo:** Introducción a preprocesamiento de datos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐
"""

from math import log10
from random import randint

# generar cadena de numeros al azar
numeros = [randint(1, 1000) for _ in range(50)]

# normalizador segun el numero mas alto
multiplicador = 10 ** (int(log10(max(numeros)))+1)

# normalizo los numeros
numeros_normalizados = []

for i in numeros:
    numeros_normalizados.append(i / multiplicador)
    
print(f"numeros originales: {numeros}")
print(f"numeros nmormalizados: {numeros_normalizados}")