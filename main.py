import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np

file_path = "./jobs_in_data.csv"
data = pd.read_csv(file_path)

# work_year = data["work_year"].value_counts()

# plt.figure(figsize=(10, 6))
# sns.barplot(x=work_year.index, y=work_year.values, hue=work_year.values, legend=False)
# plt.title("Frequency of Each Work Year(First Recorded)")
# plt.xlabel("Work Year")
# plt.ylabel("Frequency")
# plt.show()
# *Getting the frequency of each year that the data was recorded

# data["salary"] = pd.to_numeric(data["salary"], errors="coerce")
# average_salary = data.groupby("work_year")["salary"].mean().reset_index()

# plt.figure(figsize=(10, 6))
# sns.barplot(data=average_salary, x="work_year", y="salary", hue="salary", legend=False)
# plt.title("Average Salaries for Each Work Year")
# plt.xlabel("Work Year")
# plt.ylabel("Average Salary")
# plt.show()
# *Showing the average of salaries over time, showing a rise in salaries

# job_titles = data["job_title"].value_counts()
# plt.figure(figsize=(14, 14))
# sns.barplot(x=job_titles.values, y=job_titles.index, hue=job_titles.index, legend=False)
# plt.title("Frequency of Each Job Title")
# plt.subplots_adjust(bottom=0.040, top=0.95)
# plt.xlabel("Frequency")
# plt.ylabel("Job Title", labelpad=10)
# plt.show()

# *Showing how often Job Titles are used
# !Having issues with how close y labels are together, will ask for help on Monday

# common_data_jobs = data["job_title"].value_counts()
# top_10 = common_data_jobs.head(10)

# plt.figure(figsize=(14, 8))
# sns.barplot(x=top_10.values, y=top_10.index, hue=top_10.index, legend=False)
# plt.title("Top 10 Most Common Data Jobs")
# plt.xlabel("Frequency")
# plt.ylabel("Job Title")
# plt.subplots_adjust(left=0.202)
# plt.show()

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")
average_salary_by_title = data.groupby("job_title")["salary"].mean().reset_index()

plt.figure(figsize=(16, 8))
sns.barplot(
    x="salary",
    y="job_title",
    data=average_salary_by_title.sort_values(by="salary", ascending=False),
    hue="job_title",
    legend=False,
)
plt.title("Average Salaries by Job Titles")
plt.subplots_adjust(bottom=0.040, top=0.95)
plt.xlabel("Average Salary")
plt.ylabel("Job Title")
plt.show()
# *General average salaries

top_highest = average_salary_by_title.nlargest(5, "salary")
print("\nTop Job Titles w/ Highest Average Salaries: ")
print(top_highest)
top_lowest = average_salary_by_title.nsmallest(5, "salary")
print("\nTop Job Titles w/ Least Average Salaries: ")
print(top_lowest)
# *Printing out top and lower ends of the spectrum
