#
import pandas as pd

data = pd.read_csv("data/lightcast_job_postings.csv", nrows=5)
print(list(data.columns))