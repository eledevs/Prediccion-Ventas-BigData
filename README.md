# 🍎 Sistema de Predicción de Ventas - SuperFresh

Este proyecto desarrolla un sistema de **Big Data** e **Inteligencia Artificial** diseñado para optimizar el inventario de una cadena de supermercados. Utiliza un modelo predictivo para estimar las unidades vendidas basándose en factores temporales (mes, día de la semana) y condiciones climáticas.

## 🚀 Tecnologías Utilizadas
* **Lenguaje:** Python 3.14.
* **Procesamiento:** Apache Spark (PySpark).
* **Machine Learning:** Spark MLlib (Random Forest Regressor).
* **Visualización:** Tableau Public.

## 📂 Estructura del Proyecto
* `preprocesamiento.py`: Script para la limpieza de datos, gestión de nulos y enriquecimiento del dataset.
* `modelo_ia.py`: Implementación del modelo de Machine Learning, entrenamiento y generación de predicciones.
* `datos_ventas.csv`: Dataset histórico original con registros de ventas.
* `csv_powerbi/`: Directorio que contiene los resultados procesados (`datos_finales.csv`) listos para el Dashboard.

## 🛠️ Cómo Usarlo

### 1. Requisitos Previos
Es necesario contar con **Java JRE** configurado en el sistema y la librería **NumPy** para los cálculos matriciales de Spark.

```bash
# Instalación de dependencias necesarias
/usr/local/bin/python3.14 -m pip install numpy
```

### 2. Ejecución
Primero, ejecuta el preprocesamiento para limpiar y transformar los datos:
```Bash
python3 preprocesamiento.py
```
Después, entrena el modelo para generar las predicciones finales:
```Bash
python3 modelo_ia.py
```
### 📊 Visualización de Resultados
Los resultados se integran en un Dashboard de Tableau. En el gráfico se observa la comparativa entre las Unidades Vendidas (realidad) y la Prediction (modelo IA), permitiendo identificar picos de demanda y ajustar el stock de forma proactiva.
