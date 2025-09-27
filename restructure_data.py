import pandas as pd
import os

# 确保输出目录存在
os.makedirs("_output", exist_ok=True)
# Load the dataset
data = pd.read_csv('data/lightcast_job_postings.csv')

# Extract Job_Postings table
job_postings = data[['ID', 'TITLE_RAW', 'TITLE_CLEAN', 'POSTED', 'EXPIRED',
                     'SALARY_FROM', 'SALARY_TO', 'MIN_YEARS_EXPERIENCE',
                     'MAX_YEARS_EXPERIENCE', 'SKILLS', 'SPECIALIZED_SKILLS',
                     'SOFTWARE_SKILLS', 'EMPLOYMENT_TYPE', 'COMPANY']]
print("✅ Job_Postings saved")
job_postings.to_csv('_output/job_postings.csv', index=False)
print(job_postings.head(), "\n")

# Extract Company table
company = data[['COMPANY', 'COMPANY_NAME', 'COMPANY_RAW', 'COMPANY_IS_STAFFING']]
company.to_csv('_output/company.csv', index=False)
print("✅ Company saved")
print(company.head(), "\n")

# Extract Job_Location table
job_location = data[['ID', 'CITY', 'STATE', 'COUNTY']]
job_location.to_csv('_output/job_location.csv', index=False)
print("✅ Job_Location saved")
print(job_location.head(), "\n")

# Extract SOC_Details table
soc_details = data[['ID', 'SOC_2', 'SOC_2_NAME', 'SOC_3', 'SOC_3_NAME',
                    'SOC_4', 'SOC_4_NAME', 'SOC_5', 'SOC_5_NAME']]
soc_details.to_csv('_output/soc_details.csv', index=False)
print("✅ SOC_Details saved")
print(soc_details.head(), "\n")

# Extract LOT_Details table
lot_details = data[['ID', 'LOT_CAREER_AREA', 'LOT_CAREER_AREA_NAME',
                    'LOT_OCCUPATION', 'LOT_OCCUPATION_NAME',
                    'LOT_SPECIALIZED_OCCUPATION', 'LOT_SPECIALIZED_OCCUPATION_NAME']]
lot_details.to_csv('_output/lot_details.csv', index=False)
print("✅ LOT_Details saved")
print(lot_details.head(), "\n")

# Extract NAICS_Details table
naics_details = data[['ID', 'NAICS2', 'NAICS2_NAME', 
                    'NAICS3', 'NAICS3_NAME',
                    'NAICS4', 'NAICS4_NAME', 
                    'NAICS5', 'NAICS5_NAME',
                    'NAICS6', 'NAICS6_NAME']]
naics_details.to_csv('_output/naics_details.csv', index=False)
print("✅ NAICS_Details saved")
print(naics_details.head(), "\n")

print("All tables have been extracted and saved to _output/")

