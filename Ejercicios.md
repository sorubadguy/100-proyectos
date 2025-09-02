# Guía de 100 Ejercicios de Python orientados a Data Science y Machine Learning

---

# 📅 Plan de Estudio – 100 Ejercicios de Python para Data Science y Machine Learning

Este plan está diseñado para completarse en **10 semanas**, con un enfoque progresivo: desde fundamentos de Python hasta un proyecto final integrador.  
Cada semana incluye:  
- **Ejercicios asignados** (referencia a la guía de 100 ejercicios)  
- **Objetivos de aprendizaje**  
- **Datasets sugeridos**  
- **Checkpoint de evaluación**  
- **Criterios de finalización**

---

## Semana 1 – Fundamentos I
**Ejercicios:** 1–10  
**Objetivos:**  
- Dominar sintaxis básica de Python.  
- Trabajar con estructuras de datos y funciones simples.  
- Introducir conceptos estadísticos básicos.  

**Datasets sugeridos:** Lista de números generada manualmente, textos cortos.  

**Checkpoint:**  
- Ejecutar todos los scripts sin errores.  
- Documentar cada ejercicio con comentarios claros.  

**Criterio de finalización:**  
- Comprender variables, tipos de datos, bucles y condicionales.

---

## Semana 2 – Fundamentos II
**Ejercicios:** 11–20  
**Objetivos:**  
- Programación orientada a objetos básica.  
- Lectura y escritura de archivos.  
- Introducción a JSON y manipulación de datos.  

**Datasets sugeridos:** Archivos CSV y JSON simples.  

**Checkpoint:**  
- Crear una clase funcional con métodos útiles.  
- Leer y guardar datos en diferentes formatos.  

**Criterio de finalización:**  
- Poder estructurar código en funciones y clases reutilizables.

---

## Semana 3 – Manipulación de datos I
**Ejercicios:** 21–30  
**Objetivos:**  
- Cargar y explorar datos con `pandas`.  
- Filtrar, ordenar y agrupar datos.  
- Manejar valores nulos y duplicados.  

**Datasets sugeridos:** Titanic, Iris.  

**Checkpoint:**  
- Generar un resumen estadístico de un dataset real.  
- Limpiar datos y dejar un DataFrame listo para análisis.  

**Criterio de finalización:**  
- Conocer las funciones básicas de `pandas` para limpieza.

---

## Semana 4 – Manipulación de datos II
**Ejercicios:** 31–40  
**Objetivos:**  
- Calcular correlaciones y percentiles.  
- Crear índices jerárquicos.  
- Exportar datos a diferentes formatos.  

**Datasets sugeridos:** Wine Quality, ventas ficticias.  

**Checkpoint:**  
- Detectar y eliminar outliers con IQR.  
- Exportar un DataFrame limpio a CSV y Excel.  

**Criterio de finalización:**  
- Manejar transformaciones intermedias en `pandas` y `numpy`.

---

## Semana 5 – Visualización I
**Ejercicios:** 41–50  
**Objetivos:**  
- Crear histogramas, scatter plots y boxplots.  
- Personalizar gráficos con títulos, etiquetas y colores.  

**Datasets sugeridos:** Titanic, Iris.  

**Checkpoint:**  
- Generar al menos 3 tipos de gráficos con datos reales.  

**Criterio de finalización:**  
- Poder representar visualmente distribuciones y relaciones.

---

## Semana 6 – Visualización II y EDA
**Ejercicios:** 51–60  
**Objetivos:**  
- Graficar mapas, heatmaps y pairplots.  
- Crear dashboards básicos con `streamlit`.  

**Datasets sugeridos:** Datos geográficos simples, Kaggle datasets.  

**Checkpoint:**  
- Presentar un mini-dashboard con al menos 2 visualizaciones.  

**Criterio de finalización:**  
- Integrar visualizaciones en un flujo de análisis exploratorio.

---

## Semana 7 – Machine Learning I
**Ejercicios:** 61–70  
**Objetivos:**  
- Dividir datos en train/test.  
- Entrenar modelos de regresión y clasificación básicos.  
- Introducir clustering y PCA.  

**Datasets sugeridos:** Iris, Boston Housing.  

**Checkpoint:**  
- Entrenar y evaluar al menos 2 modelos diferentes.  

**Criterio de finalización:**  
- Comprender el flujo básico de entrenamiento y evaluación.

---

## Semana 8 – Machine Learning II
**Ejercicios:** 71–80  
**Objetivos:**  
- Validación cruzada y optimización de hiperparámetros.  
- Uso de pipelines y escalado de datos.  

**Datasets sugeridos:** Wine Quality, datasets propios.  

**Checkpoint:**  
- Implementar un pipeline completo con preprocesamiento y modelo.  

**Criterio de finalización:**  
- Poder optimizar y automatizar el flujo de ML.

---

## Semana 9 – Proyectos temáticos
**Ejercicios:** 81–90  
**Objetivos:**  
- Aplicar ML a problemas reales: predicción, clasificación, clustering.  

**Datasets sugeridos:** Kaggle (Churn, Spam, MNIST).  

**Checkpoint:**  
- Completar al menos 2 proyectos con datasets reales.  

**Criterio de finalización:**  
- Tener proyectos listos para portafolio.

---

## Semana 10 – Proyecto final y revisión
**Ejercicios:** 91–100  
**Objetivos:**  
- Integrar todo el flujo: datos crudos → EDA → ML → despliegue.  
- Documentar y presentar resultados.  

**Datasets sugeridos:** A elección, según interés personal.  

**Checkpoint:**  
- Proyecto final funcional en `streamlit` o `fastapi`.  

**Criterio de finalización:**  
- Proyecto documentado, reproducible y listo para mostrar.

---

## Bloque 1 – Fundamentos de Python para Datos (1–20)

### 1. Hola Data Science
**Descripción:** Imprime en pantalla "Hola Data Science" y la versión de Python instalada.  
**Objetivo:** Familiarizarse con la sintaxis básica y el entorno.  
**Librerías sugeridas:** `sys`  
**Dificultad:** ⭐

### 2. Estadísticas básicas
**Descripción:** Calcular media, mediana y desviación estándar de una lista numérica.  
**Objetivo:** Practicar operaciones matemáticas y funciones integradas.  
**Librerías sugeridas:** `statistics`  
**Dificultad:** ⭐

### 3. Frecuencia de palabras
**Descripción:** Contar cuántas veces aparece cada palabra en un texto.  
**Objetivo:** Manejo de cadenas y diccionarios.  
**Librerías sugeridas:** `collections.Counter`  
**Dificultad:** ⭐⭐

### 4. Números primos
**Descripción:** Generar una lista de números primos hasta 100.  
**Objetivo:** Practicar bucles y condicionales.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 5. Normalización de datos
**Descripción:** Crear una función que normalice una lista de valores entre 0 y 1.  
**Objetivo:** Introducción a preprocesamiento de datos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 6. Leer CSV con open()
**Descripción:** Leer un archivo `.csv` simple y mostrar las primeras 5 líneas.  
**Objetivo:** Practicar lectura de archivos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 7. Lista de diccionarios a diccionario de listas
**Descripción:** Convertir una lista de diccionarios en un diccionario de listas.  
**Objetivo:** Manipulación de estructuras de datos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 8. Filtrar números pares
**Descripción:** Filtrar números pares de una lista usando *list comprehension*.  
**Objetivo:** Sintaxis concisa y filtrado.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐

### 9. Correlación de Pearson
**Descripción:** Calcular la correlación de Pearson entre dos listas.  
**Objetivo:** Introducción a estadística.  
**Librerías sugeridas:** `scipy.stats`  
**Dificultad:** ⭐⭐

### 10. Entropía de Shannon
**Descripción:** Implementar una función que calcule la entropía de Shannon de una lista.  
**Objetivo:** Conceptos de teoría de la información.  
**Librerías sugeridas:** `math`  
**Dificultad:** ⭐⭐⭐

### 11. Clase Dataset
**Descripción:** Crear una clase `Dataset` con métodos para cargar y describir datos.  
**Objetivo:** Programación orientada a objetos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 12. Enumerar elementos
**Descripción:** Usar `enumerate()` para indexar elementos de una lista.  
**Objetivo:** Iteración eficiente.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐

### 13. Decorador de tiempo
**Descripción:** Implementar un *decorator* que mida el tiempo de ejecución de una función.  
**Objetivo:** Decoradores y medición de rendimiento.  
**Librerías sugeridas:** `time`  
**Dificultad:** ⭐⭐

### 14. Simulación de dado
**Descripción:** Simular 1000 lanzamientos de un dado y calcular probabilidades.  
**Objetivo:** Simulación y aleatoriedad.  
**Librerías sugeridas:** `random`  
**Dificultad:** ⭐⭐

### 15. Generador Fibonacci
**Descripción:** Crear un generador que devuelva números de Fibonacci hasta un límite.  
**Objetivo:** Uso de `yield` y generadores.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 16. Búsqueda binaria
**Descripción:** Implementar búsqueda binaria en una lista ordenada.  
**Objetivo:** Algoritmos de búsqueda.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 17. Combinar listas con zip()
**Descripción:** Usar `zip()` para combinar dos listas en un diccionario.  
**Objetivo:** Empaquetado de datos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐

### 18. Matriz de confusión manual
**Descripción:** Calcular la matriz de confusión a partir de listas de etiquetas.  
**Objetivo:** Métricas de clasificación.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 19. Min-Max Scaling manual
**Descripción:** Implementar *min-max scaling* sin librerías externas.  
**Objetivo:** Preprocesamiento de datos.  
**Librerías sugeridas:** Ninguna  
**Dificultad:** ⭐⭐

### 20. Guardar y cargar JSON
**Descripción:** Guardar un diccionario en un archivo JSON y luego cargarlo.  
**Objetivo:** Persistencia de datos.  
**Librerías sugeridas:** `json`  
**Dificultad:** ⭐⭐

---

## Bloque 2 – Manipulación y análisis con pandas/numpy (21–40)

### 21. Leer CSV con pandas
**Descripción:** Cargar un archivo CSV y mostrar `head()` y `info()`.  
**Objetivo:** Familiarizarse con la carga y exploración inicial de datos.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐

### 22. Selección y filtrado
**Descripción:** Seleccionar columnas específicas y filtrar filas por una condición.  
**Objetivo:** Practicar indexado y filtrado en DataFrames.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 23. Estadísticas descriptivas
**Descripción:** Calcular estadísticas con `.describe()` y métricas personalizadas.  
**Objetivo:** Resumen rápido de datos numéricos.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐

### 24. Manejo de valores nulos
**Descripción:** Reemplazar valores nulos con la media de la columna.  
**Objetivo:** Limpieza de datos.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 25. Columna calculada
**Descripción:** Crear una nueva columna a partir de operaciones entre otras dos.  
**Objetivo:** Transformación de datos.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐

### 26. Agrupación y agregación
**Descripción:** Agrupar datos por categoría y calcular la media.  
**Objetivo:** Uso de `groupby()` y funciones de agregación.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 27. Ordenar DataFrame
**Descripción:** Ordenar por múltiples columnas en orden ascendente y descendente.  
**Objetivo:** Organización de datos.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐

### 28. Combinar DataFrames
**Descripción:** Unir dos DataFrames usando `merge()` con diferentes tipos de join.  
**Objetivo:** Integración de datasets.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 29. Pivotar datos
**Descripción:** Crear una tabla pivote con `pivot_table()`.  
**Objetivo:** Reestructuración de datos.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 30. Eliminar duplicados
**Descripción:** Detectar y eliminar filas duplicadas.  
**Objetivo:** Limpieza de datos redundantes.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐

### 31. Matriz de correlación
**Descripción:** Calcular la correlación entre columnas numéricas.  
**Objetivo:** Identificar relaciones entre variables.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 32. Matriz aleatoria y determinante
**Descripción:** Crear una matriz aleatoria y calcular su determinante.  
**Objetivo:** Operaciones matriciales.  
**Librerías sugeridas:** `numpy`  
**Dificultad:** ⭐⭐

### 33. Funciones personalizadas con apply()
**Descripción:** Aplicar una función definida por el usuario a una columna.  
**Objetivo:** Transformaciones personalizadas.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 34. Manejo de fechas
**Descripción:** Convertir una columna a `datetime` y extraer año, mes y día.  
**Objetivo:** Procesamiento de datos temporales.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 35. Diferencia porcentual
**Descripción:** Calcular la variación porcentual entre filas consecutivas.  
**Objetivo:** Análisis de cambios en series temporales.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 36. MultiIndex
**Descripción:** Crear un índice jerárquico en un DataFrame.  
**Objetivo:** Manejo de estructuras de datos complejas.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐⭐

### 37. Exportar datos
**Descripción:** Guardar un DataFrame en CSV y Excel.  
**Objetivo:** Exportación de resultados.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐

### 38. Filtrado con query()
**Descripción:** Usar `query()` para filtrar datos con expresiones.  
**Objetivo:** Filtrado más legible y flexible.  
**Librerías sugeridas:** `pandas`  
**Dificultad:** ⭐⭐

### 39. Calcular percentiles
**Descripción:** Calcular percentiles de una columna numérica.  
**Objetivo:** Análisis estadístico.  
**Librerías sugeridas:** `numpy`  
**Dificultad:** ⭐⭐

### 40. Detección de outliers con IQR
**Descripción:** Detectar valores atípicos usando el rango intercuartílico.  
**Objetivo:** Identificación de datos extremos.  
**Librerías sugeridas:** `pandas`, `numpy`  
**Dificultad:** ⭐⭐⭐

---

## Bloque 3 – Visualización y EDA (41–60)

### 41. Histograma básico
**Descripción:** Graficar un histograma de una variable numérica.  
**Objetivo:** Visualizar la distribución de datos.  
**Librerías sugeridas:** `matplotlib`  
**Dificultad:** ⭐

### 42. Gráfico de dispersión
**Descripción:** Crear un *scatter plot* para dos variables numéricas.  
**Objetivo:** Identificar relaciones y patrones.  
**Librerías sugeridas:** `matplotlib`, `seaborn`  
**Dificultad:** ⭐

### 43. Serie temporal
**Descripción:** Graficar la evolución de una variable en el tiempo.  
**Objetivo:** Analizar tendencias temporales.  
**Librerías sugeridas:** `matplotlib`, `pandas`  
**Dificultad:** ⭐⭐

### 44. Personalización de gráficos
**Descripción:** Añadir títulos, etiquetas y colores personalizados.  
**Objetivo:** Mejorar la legibilidad de gráficos.  
**Librerías sugeridas:** `matplotlib`  
**Dificultad:** ⭐

### 45. Boxplot para outliers
**Descripción:** Crear un diagrama de caja para detectar valores atípicos.  
**Objetivo:** Identificar outliers y rangos intercuartílicos.  
**Librerías sugeridas:** `seaborn`  
**Dificultad:** ⭐⭐

### 46. Heatmap de correlación
**Descripción:** Graficar una matriz de correlación con colores.  
**Objetivo:** Visualizar relaciones entre variables.  
**Librerías sugeridas:** `seaborn`, `pandas`  
**Dificultad:** ⭐⭐

### 47. Pairplot
**Descripción:** Usar `pairplot` para explorar relaciones entre múltiples variables.  
**Objetivo:** Análisis exploratorio multivariable.  
**Librerías sugeridas:** `seaborn`  
**Dificultad:** ⭐⭐

### 48. Distribución con histplot
**Descripción:** Graficar la distribución de una variable con `sns.histplot`.  
**Objetivo:** Comparar histogramas y densidades.  
**Librerías sugeridas:** `seaborn`  
**Dificultad:** ⭐

### 49. Barras agrupadas
**Descripción:** Crear un gráfico de barras agrupadas por categoría.  
**Objetivo:** Comparar valores entre grupos.  
**Librerías sugeridas:** `matplotlib`, `seaborn`  
**Dificultad:** ⭐⭐

### 50. Anotaciones en gráficos
**Descripción:** Añadir anotaciones y etiquetas a puntos clave.  
**Objetivo:** Resaltar información importante.  
**Librerías sugeridas:** `matplotlib`  
**Dificultad:** ⭐⭐

### 51. Mapa básico con geopandas
**Descripción:** Graficar datos geográficos simples.  
**Objetivo:** Introducción a visualización geoespacial.  
**Librerías sugeridas:** `geopandas`  
**Dificultad:** ⭐⭐⭐

### 52. Gráfico interactivo con plotly
**Descripción:** Crear un gráfico interactivo básico.  
**Objetivo:** Mejorar la exploración de datos.  
**Librerías sugeridas:** `plotly`  
**Dificultad:** ⭐⭐

### 53. Comparar distribuciones
**Descripción:** Graficar antes y después de normalizar datos.  
**Objetivo:** Visualizar el impacto del preprocesamiento.  
**Librerías sugeridas:** `matplotlib`, `seaborn`  
**Dificultad:** ⭐⭐

### 54. Importancia de variables
**Descripción:** Visualizar la importancia de variables en un modelo.  
**Objetivo:** Interpretar modelos de ML.  
**Librerías sugeridas:** `matplotlib`, `seaborn`  
**Dificultad:** ⭐⭐

### 55. Curvas ROC y PR
**Descripción:** Graficar curvas ROC y Precision-Recall.  
**Objetivo:** Evaluar modelos de clasificación.  
**Librerías sugeridas:** `matplotlib`, `scikit-learn`  
**Dificultad:** ⭐⭐⭐

### 56. Gráfico de violín
**Descripción:** Comparar distribuciones con un gráfico de violín.  
**Objetivo:** Analizar forma y dispersión de datos.  
**Librerías sugeridas:** `seaborn`  
**Dificultad:** ⭐⭐

### 57. Countplot
**Descripción:** Graficar frecuencias de categorías.  
**Objetivo:** Análisis de variables categóricas.  
**Librerías sugeridas:** `seaborn`  
**Dificultad:** ⭐

### 58. Dashboard básico con Streamlit
**Descripción:** Crear un dashboard simple para mostrar gráficos.  
**Objetivo:** Integrar visualizaciones en una app interactiva.  
**Librerías sugeridas:** `streamlit`  
**Dificultad:** ⭐⭐⭐

### 59. Visualizar clusters
**Descripción:** Graficar datos coloreados por clúster asignado.  
**Objetivo:** Interpretar resultados de clustering.  
**Librerías sugeridas:** `matplotlib`, `seaborn`  
**Dificultad:** ⭐⭐

### 60. Evolución de métricas de entrenamiento
**Descripción:** Graficar la evolución de métricas durante el entrenamiento de un modelo.  
**Objetivo:** Monitorear el rendimiento de modelos ML.  
**Librerías sugeridas:** `matplotlib`  
**Dificultad:** ⭐⭐## Bloque 3 – Visualización y EDA (41–60)

---

## Bloque 4 – Machine Learning (61–80)

### 61. División de datos en entrenamiento y prueba
**Descripción:** Separar un dataset en conjuntos de entrenamiento y prueba.  
**Objetivo:** Preparar datos para evaluar modelos de forma justa.  
**Librerías sugeridas:** `scikit-learn`, `pandas`  
**Dificultad:** ⭐

### 62. Regresión lineal
**Descripción:** Entrenar un modelo de regresión lineal simple y múltiple.  
**Objetivo:** Comprender la relación entre variables y predecir valores continuos.  
**Librerías sugeridas:** `scikit-learn`, `pandas`, `numpy`  
**Dificultad:** ⭐⭐

### 63. Evaluación de regresión
**Descripción:** Calcular métricas como RMSE, MAE y R² para un modelo de regresión.  
**Objetivo:** Medir el rendimiento de modelos de regresión.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐

### 64. Regresión logística
**Descripción:** Entrenar un modelo de clasificación binaria con regresión logística.  
**Objetivo:** Introducir un modelo lineal para clasificación.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐

### 65. Métricas de clasificación
**Descripción:** Calcular matriz de confusión, precisión, recall y F1-score.  
**Objetivo:** Evaluar modelos de clasificación.  
**Librerías sugeridas:** `scikit-learn`, `seaborn`  
**Dificultad:** ⭐⭐

### 66. Árbol de decisión
**Descripción:** Entrenar y visualizar un árbol de decisión para clasificación.  
**Objetivo:** Comprender modelos basados en reglas.  
**Librerías sugeridas:** `scikit-learn`, `matplotlib`  
**Dificultad:** ⭐⭐

### 67. Random Forest
**Descripción:** Entrenar un modelo de Random Forest y analizar importancia de variables.  
**Objetivo:** Aplicar un modelo de ensamble para mejorar predicciones.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐

### 68. K-Nearest Neighbors (KNN)
**Descripción:** Implementar KNN para clasificación y regresión.  
**Objetivo:** Explorar un algoritmo basado en proximidad.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐

### 69. Clustering con KMeans
**Descripción:** Agrupar datos en clústeres y visualizarlos.  
**Objetivo:** Introducir aprendizaje no supervisado.  
**Librerías sugeridas:** `scikit-learn`, `matplotlib`  
**Dificultad:** ⭐⭐

### 70. PCA – Reducción de dimensionalidad
**Descripción:** Aplicar Análisis de Componentes Principales para reducir dimensiones.  
**Objetivo:** Mejorar visualización y rendimiento de modelos.  
**Librerías sugeridas:** `scikit-learn`, `matplotlib`  
**Dificultad:** ⭐⭐

### 71. SVM – Clasificación
**Descripción:** Entrenar un modelo de Máquinas de Soporte Vectorial.  
**Objetivo:** Explorar un modelo robusto para clasificación.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐

### 72. Validación cruzada
**Descripción:** Evaluar un modelo usando k-fold cross-validation.  
**Objetivo:** Obtener métricas más estables y evitar overfitting.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐

### 73. GridSearchCV
**Descripción:** Optimizar hiperparámetros de un modelo con búsqueda en malla.  
**Objetivo:** Mejorar el rendimiento del modelo.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐⭐

### 74. Regresión polinómica
**Descripción:** Ajustar un modelo polinómico a datos no lineales.  
**Objetivo:** Modelar relaciones complejas.  
**Librerías sugeridas:** `scikit-learn`, `numpy`  
**Dificultad:** ⭐⭐

### 75. One-Hot Encoding
**Descripción:** Codificar variables categóricas para modelos ML.  
**Objetivo:** Preparar datos categóricos para algoritmos.  
**Librerías sugeridas:** `pandas`, `scikit-learn`  
**Dificultad:** ⭐

### 76. Escalado de datos
**Descripción:** Aplicar `StandardScaler` y `MinMaxScaler`.  
**Objetivo:** Normalizar datos para mejorar el rendimiento de modelos.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐

### 77. Gradient Boosting
**Descripción:** Entrenar un modelo de Gradient Boosting para clasificación.  
**Objetivo:** Usar boosting para mejorar predicciones.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐⭐

### 78. Guardar y cargar modelos
**Descripción:** Usar `joblib` o `pickle` para persistir modelos entrenados.  
**Objetivo:** Reutilizar modelos sin reentrenar.  
**Librerías sugeridas:** `joblib`, `pickle`  
**Dificultad:** ⭐

### 79. Pipeline de ML
**Descripción:** Crear un pipeline que incluya preprocesamiento y modelo.  
**Objetivo:** Automatizar el flujo de trabajo de ML.  
**Librerías sugeridas:** `scikit-learn`  
**Dificultad:** ⭐⭐

### 80. Comparación de modelos
**Descripción:** Entrenar varios modelos y comparar métricas.  
**Objetivo:** Seleccionar el mejor modelo para un problema.  
**Librerías sugeridas:** `scikit-learn`, `pandas`, `matplotlib`  
**Dificultad:** ⭐⭐