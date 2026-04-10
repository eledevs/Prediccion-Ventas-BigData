from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, dayofweek, when

# Configuro el entorno de Spark
spark = SparkSession.builder \
    .appName("Limpieza_Datos_SuperFresh") \
    .getOrCreate()

# Extraigo los datos automáticamente
# inferSchemaa divina si el dato es número o texto
df_ventas = spark.read.csv("datos_ventas.csv", header=True, inferSchema=True)

# Elimino las filas donde no haya nada vendido
df_sin_nulos = df_ventas.dropna(subset=["unidades_vendidas"])

# Extraigo el mes y el dia de la semana de la columna fecha. Para luego poder ver los dias que se vende más.
df_enriquecido = df_sin_nulos.withColumn("mes", month(col("fecha"))) \
                             .withColumn("dia_semana", dayofweek(col("fecha")))

# Convierto el clima a números
df_final = df_enriquecido.withColumn("clima_id", 
    when(col("clima") == "Soleado", 1)
    .when(col("clima") == "Lluvia", 2)
    .otherwise(3))

# Muestro el resultado pa verificar
df_final.show(10)

# Guardo los datos limpios en formato Parquet
df_final.write.mode("overwrite").parquet("datos_limpios_superfresh.parquet")