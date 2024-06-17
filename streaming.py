from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.types import *

#Define schema from streamlit
schema = StructType([
    StructField("emp_id", IntegerType(), True),
    StructField("drug_id", IntegerType(), True),
    StructField("doc_id", IntegerType(), True),
    StructField("pharmacy_name", StringType(), True),
    StructField("pharmacy_region", StringType(), True),
    StructField("quantity_sold", IntegerType(), True),
    StructField("date_sold", DateType(), True)
])

spark = SparkSession.builder.appName("StreamlitStreaming").getOrCreate()

#Define input sources
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 8000).load()

#Define the data and use the explode function to flatten it
data = lines.select(explode(split(col("value"), ",").alias("values")))

#Define columns
sales_df = data.select(
    col("values").getItem(0).cast(IntegerType()).alias("emp_id"),
    col("values").getItem(1).cast(IntegerType()).alias("drug_id"),
    col("values").getItem(2).cast(IntegerType()).alias("doc_id"),
    col("values").getItem(3).alias("pharmacy_name"),
    col("values").getItem(4).alias("pharmacy_region"),
    col("values").getItem(5).cast(IntegerType()).alias("quantity_sold"),
    col("values").getItem(6).cast(DateType()).alias("date_sold")
)

#Define groupby function
grouped_df = sales_df.groupBy("drug_id").agg(
    count("quantity_sold").alias("total_sales")
)
#Define output stream
query = grouped_df.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()

