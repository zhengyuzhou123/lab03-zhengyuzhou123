from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Lightcast").getOrCreate()

# Read CSV data
df = spark.read.csv("data/lightcast_job_postings.csv", 
    header=True,
    inferSchema=True,
    sep=",",         
    quote='"',       
    multiLine=True,  
    escape="\""
   )   

df.show(5)