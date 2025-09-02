"""
4. Números primos
**Descripción:** Generar una lista de números primos hasta 100.  
**Objetivo:** Practicar bucles y condicionales.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐
"""

numeros = []

for i in range(1, 101):
    numeros.append(i)
    
primos = []

for i in numeros:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 1 or i == 2 or i == 3 or i == 5 or i == 7:
        primos.append(i)

print(primos)