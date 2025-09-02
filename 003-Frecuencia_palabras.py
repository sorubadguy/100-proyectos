"""
3. Frecuencia de palabras
**Descripción:** Contar cuántas veces aparece cada palabra en un texto.  
**Objetivo:** Manejo de cadenas y diccionarios.  
**Librerías sugeridas:** `collections.Counter`  
**Dificultad:** ⭐⭐
"""

from collections import Counter

texto = "Le quedan los últimos dos partidos de unas Eliminatorias que ya ganó (es decir, ya nadie puede alcanzarlo en la cima de la tabla de posiciones). Primero contra Venezuela este jueves 4 de septiembre en el Estadio Monumental de Buenos Aires y después contra Ecuador en el Estadio Monumental de Guayaquil el martes 9 del mismo mes. Luego, antes del brindis, vendrán una serie de amistosos en las 2 fechas FIFA que le restan al 2025. En octubre, en los Estados Unidos, será el turno de Puerto Rico y nuevamente de Venezuela. En tanto que en noviembre, el combinado comandado por Lionel Scaloni visitará Angola e India. Sin embargo, hay una estadística que puede lograr que los futbolistas se motiven, si es que les falta algo de incentivo (rasgo que no se notó desde que Scaloni está al mando, ni siquiera, tras Qatar 2022). Se trata del Ranking FIFA, clasificación que la Selección Argentina lidera desde el 6 de abril del 2023, cuando se le computaron los puntos que cosechó en el último campeonato mundial."

# Quitar signos de puntuacion

texto2 = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "")

# Convertir a minusculas

texto2 = texto.lower()

# Contar frecuencia de palabras

palabras = texto2.split()
frecuencia = Counter(palabras)

print(f"texto original:\n{texto}\ntexto modificado:\n{texto2}\nFrecuencia de palabras: {frecuencia}")