"""
Estadísticas básicas
**Descripción:** Calcular media, mediana y desviación estándar de una lista numérica.  
**Objetivo:** Practicar operaciones matemáticas y funciones integradas.  
**Librerías sugeridas:** `statistics`  
**Dificultad:** ⭐
"""

import statistics

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

media = statistics.mean(data)
mediana = statistics.median(data)
desviacion_estandar = statistics.stdev(data)

print(f"Data = {data}\nMedia = {media}\nMeiana = {mediana}\nDesviacion Estandar = {desviacion_estandar}")