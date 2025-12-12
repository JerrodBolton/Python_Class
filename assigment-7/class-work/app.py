# ======================================================================================================================================
# Jerrod Bolton 
# Date Dec 10, 2024
# Assignment 7: MNIST Digit Classification with TensorFlow
# ======================================================================================================================================
# Import necessary libraries

import pandas as pd  # Import pandas for data manipulation and analysis

def load_dataset(the_file_name):  # Define a function to load data from a CSV file
    data = pd.read_csv(the_file_name)  # Read the CSV file into a pandas DataFrame it is called df in other places
    print(f"[INFO] Loaded dataset from '{the_file_name}'.")
    return data  # Return the DataFrame containing the loaded data it is called df in other places


# format the dataset so that is can stand out in the teminal
def format_dataset(df):  # Define a function to format the dataset
    df = df.rename(
        columns={
            "work_year": "WorkYear",
            "experience_level": "ExperienceLevel",
            "employment_type": "EmploymentType",
            "job_title": "JobTitle",
            "salary": "Salary",
            "salary_currency": "SalaryCurrency",
            "salary_in_usd": "SalaryInUSD",
            "employee_residence": "EmployeeResidence",
            "remote_ratio": "RemoteRatio",
            "company_location": "CompanyLocation",
            "company_size": "CompanySize",
        }
    )
    return df


def display_results(df):  # Define a function to display results from
    print("==============================================")  # Print a separator line for better readability
    print("First 10 rows of the formatted dataset:")  # Print a message indicating the first 5 rows will be displayed
    print(df.head(10))  # Print the first105 rows of the DataFrame
    print("==============================================")  # Print a separator line for better readability
# ======================================================================================================================================
# Jerrod Bolton
# Date Dec 10, 2024
# Assignment 7: MNIST Digit Classification with TensorFlow
# ======================================================================================================================================
if __name__ == "__main__":  # Check if this script is being run directly
    file_name = "salaries.csv"  # Specify the name of the CSV file to load
    df = load_dataset(file_name)  # Load the dataset from the specified CSV file
    df = format_dataset(df)  # Format the loaded dataset
    display_results(df)  # Display results from the formatted dataset
