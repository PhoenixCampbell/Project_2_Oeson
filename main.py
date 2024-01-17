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
plt.figure(figsize=(14, 14))
sns.barplot(x=job_titles.values, y=job_titles.index, hue=job_titles.index, legend=False)
plt.title("Frequency of Each Job Title")
plt.subplots_adjust(bottom=0.040, top=0.95)
plt.xlabel("Frequency")
plt.ylabel("Job Title", labelpad=10)
plt.show()

# *Showing how often Job Titles are used

common_data_jobs = data["job_title"].value_counts()
top_10 = common_data_jobs.head(10)

plt.figure(figsize=(14, 8))
sns.barplot(x=top_10.values, y=top_10.index, hue=top_10.index, legend=False)
plt.title("Top 10 Most Common Data Jobs")
plt.xlabel("Frequency")
plt.ylabel("Job Title")
plt.subplots_adjust(left=0.202)
plt.show()

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

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

job_title = data["job_title"].value_counts()

top_common_job_titles = job_title.head(5).index

top_common_jobs = data[data["job_title"].isin(top_common_job_titles)]

average_salary = top_common_jobs.groupby("job_title")["salary"].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(
    x="salary", y="job_title", data=average_salary, hue="job_title", legend=False
)
plt.title("Average Salaries for the Most Common Job Titles")
plt.xlabel("Average Salary")
plt.ylabel("Job Title")
plt.show()
# * average salaries for most common jobs

job_category = data["job_category"].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(
    x=job_category.index, y=job_category.values, hue=job_category.values, legend=False
)
plt.title("Distribution of Job Categories")
plt.xlabel("Job Category")
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha="right")
plt.show()
# *distribution of job categories

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

average_by_category = data.groupby("job_category")["salary"].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(
    x="salary",
    y="job_category",
    data=average_by_category.sort_values(by="salary", ascending=False),
    hue="job_category",
    legend=False,
)
plt.title("Average Salaries by Job Category")
plt.xlabel("Average Salary")
plt.ylabel("Job Category")
plt.show()
# *average salary through job category

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

data["salary_in_usd"] = data["salary_in_usd"].apply(
    lambda x: float(x.replace(",", "")) if isinstance(x, str) else x
)

average_by_currency = (
    data.groupby("salary_currency")["salary_in_usd"].mean().reset_index()
)

plt.figure(figsize=(12, 6))
sns.barplot(
    x="salary_in_usd",
    y="salary_currency",
    data=average_by_currency.sort_values(by="salary_in_usd", ascending=False),
    hue="salary_currency",
    legend=False,
)
plt.title("Average Salary in USD by Currency")
plt.xlabel("Average Salary in USD")
plt.ylabel("Currency")
plt.show()
# *average salary based on USD, with USD obviously being the largest bar on the plot

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

average_by_location = (
    data.groupby(["employee_residence", "company_location"])["salary"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(16, 8))
sns.barplot(
    x="salary",
    y="employee_residence",
    hue="company_location",
    data=average_by_location.sort_values(by="salary", ascending=False),
    palette="viridis",
)
plt.title("Average Salary by Employee Residence and Company Location")
plt.subplots_adjust(bottom=0.040, top=0.95, right=0.75)
plt.xlabel("Average Salary")
plt.ylabel("Employee Residence")
plt.legend(title="Company Location", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()
# *average salary based on employee residence and company location

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

average_by_experience = data.groupby("experience_level")["salary"].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(
    x="experience_level",
    y="salary",
    data=average_by_experience.sort_values(by="salary", ascending=False),
    hue="salary",
    legend=False,
)
plt.title("Average Salary by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Average Salary")
plt.show()
# * Salaries based on experience levels

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

average_by_category = (
    data.groupby(["employment_type", "work_setting", "company_size"])["salary"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(16, 8))
sns.barplot(
    x="salary",
    y="employment_type",
    hue="work_setting",
    data=average_by_category.sort_values(by="salary", ascending=False),
    palette="viridis",  #!using palette as hue is being used previously
    ci=None,
)
plt.title("Average Salary by Employment Type, Work Setting, and Company Size")
plt.subplots_adjust(right=0.86)
plt.xlabel("Average Salary")
plt.ylabel("Employment Type")
plt.legend(title="Work Setting", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()
# *average salary based on employment type, work setting, and "company_size"
