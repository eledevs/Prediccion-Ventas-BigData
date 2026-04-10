from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession

# 1. Iniciamos la sesión de Spark
spark = SparkSession.builder.appName("Entrenamiento_SuperFresh").getOrCreate()

# 2. Cargo los datos
df = spark.read.csv("datos_ventas.csv", header=True, inferSchema=True)

# 3. Preparamos las Features para la IA
ensamblador = VectorAssembler(inputCols=["unidades_vendidas"], outputCol="features") 
df_preparado = ensamblador.transform(df)

# 4. Entreno el modelo Random Forest
rf = RandomForestRegressor(featuresCol="features", labelCol="unidades_vendidas")
modelo = rf.fit(df_preparado)

# 5. Muestro las predicciones
predicciones = modelo.transform(df_preparado)
predicciones.select("unidades_vendidas", "prediction").show()

# Guardo los resultados en una carpeta llamada 'csv_powerbi'
predicciones.select("fecha", "unidades_vendidas", "prediction") \
    .coalesce(1) \
    .write.mode("overwrite") \
    .csv("csv_powerbi", header=True)