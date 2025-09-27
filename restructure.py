from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Restructure Lightcast Data").getOrCreate()

# Read CSV data
df = spark.read.csv("data/lightcast_job_postings.csv", 
    header=True,
    inferSchema=True,
    sep=",",         
    quote='"',       
    multiLine=True,  
    escape="\""
   )   

# Job Postings table1.2.1
job_postings = df.select(
    "ID", "TITLE_RAW", "TITLE_CLEAN", 
    "POSTED", "EXPIRED",
    "SALARY_FROM", "SALARY_TO",
    "MIN_YEARS_EXPERIENCE", "MAX_YEARS_EXPERIENCE",
    "SKILLS", "SPECIALIZED_SKILLS", "SOFTWARE_SKILLS",
    "EMPLOYMENT_TYPE",
    df["COMPANY"].alias("COMPANY_ID")
)
job_postings.createOrReplaceTempView("Job_Postings")
print("\n✅ Job_Postings")
job_postings.show(5, truncate=False)

# Companies table1.2.2
companies = df.select(
    df["COMPANY"].alias("COMPANY_ID"),
    "COMPANY_NAME",
    "COMPANY_RAW",
    "COMPANY_IS_STAFFING"
).distinct()
companies.createOrReplaceTempView("Companies")
print("\n✅ Companies")
companies.show(5, truncate=False)

# Locations table1.2.3
job_location = df.select(
    "ID",
    "CITY", 
    "STATE", 
    "COUNTY",
)
job_location.createOrReplaceTempView("Job_Location")
print("\n✅ Job_Location")
job_location.show(5, truncate=False)

# 1.2.4 SOC_Details
soc_details = df.select(
    "ID",
    "SOC_2", "SOC_2_NAME",
    "SOC_3", "SOC_3_NAME",
    "SOC_4", "SOC_4_NAME",
    "SOC_5", "SOC_5_NAME"
)
soc_details.createOrReplaceTempView("SOC_Details")
print("\n✅ SOC_Details")
soc_details.show(5, truncate=False)

# 1.2.5 LOT_Details
lot_details = df.select(
    "ID","LOT_CAREER_AREA", "LOT_CAREER_AREA_NAME",
    "LOT_OCCUPATION", "LOT_OCCUPATION_NAME",
    "LOT_SPECIALIZED_OCCUPATION", "LOT_SPECIALIZED_OCCUPATION_NAME"
)
lot_details.createOrReplaceTempView("LOT_Details")
print("\n✅ LOT_Details")
lot_details.show(5, truncate=False)

#1.2.6 NAICS_Details
naics_details = df.select(
    "ID", "NAICS2", "NAICS2_NAME",
    "NAICS3", "NAICS3_NAME",
    "NAICS4", "NAICS4_NAME",
    "NAICS5", "NAICS5_NAME",
    "NAICS6", "NAICS6_NAME"
)
naics_details.createOrReplaceTempView("NAICS_Details")
print("\n✅ NAICS_Details")
naics_details.show(5, truncate=False)