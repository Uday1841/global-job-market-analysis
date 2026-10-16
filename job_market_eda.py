import pandas as pd
import matplotlib.pyplot as plt    

#  pandas loads and analyzes your CSV data.
# read_csv() reads your dataset.
# df.head() displays the first five records.
# df.shape shows the number of rows and columns.
# df.columns displays all column names.
# encoding="utf-8-sig" handles a possible BOM at the beginning of the CSV.
# Load the dataset

file_path = r"E:\Uday Kumar\Power BI\job_market_dataset.csv"

df = pd.read_csv(file_path, encoding="utf-8-sig")

# Display dataset information
print("First 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Average salary by occupation
occupation_salary = (
    df.groupby("occupation")["salary"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Salary by Occupation:")
print(occupation_salary)

# Average salary by country
country_salary = (
    df.groupby("country")["salary"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 Countries by Average Salary:")
print(country_salary.head(10))

# Visualize average salary by occupation

occupation_salary = occupation_salary.sort_values()

plt.figure(figsize=(10, 6))

plt.barh(
    occupation_salary.index,
    occupation_salary.values
)

plt.title("Average Salary by Occupation")
plt.xlabel("Average Salary")
plt.ylabel("Occupation")

plt.tight_layout()
plt.show()


# Average salary by years of experience

experience_salary = (
    df.groupby("years_of_experience")["salary"]
    .mean()
)

print("\nAverage Salary by Years of Experience:")
print(experience_salary)

# Create a line chart
plt.figure(figsize=(10, 6))

plt.plot(
    experience_salary.index,
    experience_salary.values,
    marker="o"
)

plt.title("Average Salary by Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Average Salary")

plt.grid(True)
plt.tight_layout()
plt.show()

############################################33333
# Count job records by year

jobs_by_year = df.groupby("year").size()

print("\nJob Records by Year:")
print(jobs_by_year)

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    jobs_by_year.index.astype(str),
    jobs_by_year.values
)

plt.title("Job Records by Year")
plt.xlabel("Year")
plt.ylabel("Number of Job Records")

plt.tight_layout()
plt.show()

#############################################################333333333333
# Average salary by education level

education_salary = (
    df.groupby("education_level")["salary"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Salary by Education Level:")
print(education_salary)

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    education_salary.index,
    education_salary.values
)

plt.title("Average Salary by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()

################################################################
# Save analysis results
occupation_salary.to_csv("E:/Global_Job_Market_Analysis/salary_by_occupation.csv")
country_salary.to_csv("E:/Global_Job_Market_Analysis/salary_by_country.csv")
experience_salary.to_csv("E:/Global_Job_Market_Analysis/salary_by_experience.csv")
jobs_by_year.to_csv("E:/Global_Job_Market_Analysis/job_records_by_year.csv")
education_salary.to_csv("E:/Global_Job_Market_Analysis/salary_by_education.csv")

print("Analysis results saved successfully!")