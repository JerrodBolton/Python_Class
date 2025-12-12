# Assignment 7 Overview
In this assignment, we will be learning how to write and read large data sets. You also need to use at least 1 Python package in this program.

## Guidelines
- Use an existing large dataset or create a large dataset or file.
- Read that large dataset and apply some formatting to the data.

## Expectations
1. Find/create a large file.
2. Read that large file.
3. Format the data in some way and display the data, perhaps using the package you included in this project.
4. Over-comment your source code file (.py) well.
5. Each program should have a great user experience.

## Deliverables / Submission
- Source code `.py` file for your application.
- Screenshot(s) or a YouTube link to a video of your app running.
- Do not zip this submission!

# About Dataset

The salaries are from ai-jobs. Ai-jobs collects salary information anonymously from professionals all over the world in the AI/ML and Big Data space and makes it publicly available for anyone to use, share and play around with. The data is being updated regularly with new data coming in, usually on a weekly basis.

The primary goal is to have data that can provide better guidance in regards to what's being paid globally.

## Dataset FieldsThe dataset contains one table structured as follow:

work_year: The year the salary was paid.
experience_level: The experience level in the job during the year with the following possible values:
EN: Entry-level / Junior
MI: Mid-level / Intermediate
SE: Senior-level / Expert
EX: Executive-level / Director
employment_type: The type of employement for the role:
PT: Part-time
FT: Full-time
CT: Contract
FL: Freelance
job_title: The role worked in during the year.
salary: The total gross salary amount paid.
salary_currency: The currency of the salary paid as an ISO 4217 currency code.
salary_in_usd: The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com).
employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
remote_ratio: The overall amount of work done remotely, possible values are as follows:
0: No remote work (less than 20%)
50: Partially remote
100: Fully remote (more than 80%)
company_location: The country of the employer's main office or contracting branch as an ISO 3166 country code.
company_size: The average number of people that worked for the company during the year:
S: less than 50 employees (small)
M: 50 to 250 employees (medium)
L: more than 250 employees (large)

- **work_year**: The year the salary was paid.

- **experience_level**: The experience level in the job during the year.
    - EN: Entry-level / Junior
    - MI: Mid-level / Intermediate
    - SE: Senior-level / Expert
    - EX: Executive-level / Director

- **employment_type**: The type of employment for the role.
    - PT: Part-time
    - FT: Full-time
    - CT: Contract
    - FL: Freelance

- **job_title**: The role worked in during the year.

- **salary**: The total gross salary amount paid.

- **salary_currency**: The currency of the salary paid (ISO 4217 code).

- **salary_in_usd**: The salary in USD (FX rate divided by avg. USD rate for the respective year).

- **employee_residence**: Employee's primary country of residence (ISO 3166 code).

- **remote_ratio**: The overall amount of work done remotely.
    - 0: No remote work (less than 20%)
    - 50: Partially remote
    - 100: Fully remote (more than 80%)

- **company_location**: The employer's main office country (ISO 3166 code).

- **company_size**: Average number of company employees.
    - S: less than 50 employees
    - M: 50 to 250 employees
    - L: more than 250 employees

