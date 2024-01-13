import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px

file_path = "./jobs_in_data.csv"
data = pd.read_csv(file_path)

work_year = data["work_year"].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=work_year.index, y=work_year.values, hue=work_year.values, legend=False)
plt.title("Frequency of Each Work Year(First Recorded)")
plt.xlabel("Work Year")
plt.ylabel("Frequency")
plt.show()
# *Getting the frequency of each year that the data was recorded

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

average_salary = data.groupby("work_year")["salary"].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=average_salary, x="work_year", y="salary", hue="salary", legend=False)
plt.title("Average Salaries for Each Work Year")
plt.xlabel("Work Year")
plt.ylabel("Average Salary")
plt.show()
# *Showing the average of salaries over time, showing a rise in salaries

job_titles = data["job_title"].value_counts()

plt.figure(figsize=(14, 8))
sns.barplot(x=job_titles.values, y=job_titles.index, hue=job_titles.index, legend=False)
plt.title("Frequency of Each Job Title")
plt.xlabel("Frequency")
plt.ylabel("Job Title")
plt.show()
