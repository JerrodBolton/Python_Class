# ======================================================================================================================================
# Jerrod Bolton 
# Date Dec 10, 2024
# Assignment 7: MNIST Digit Classification with TensorFlow
# ======================================================================================================================================
# Import necessary libraries

import random  # Import the random module for generating random numbers
import csv  # Import the csv module for working with CSV files
import os  # Import the os module for interacting with the operating system
import pandas as pd  # Import pandas for data manipulation and analysis

# 2. define a function to create a large csv file
def create_large_csv(file_name, num_rows=1000):  # Define a function to create a large CSV file with a default of 1000 rows
    with open(file_name, mode='w', newline='') as file:  # Open the file in write mode, ensuring no extra newlines
        writer = csv.writer(file)  # Create a CSV writer object to write data to the file
        writer.writerow(['user_id', 'day_number', 'steps', 'mintes_action'])  # Write the header row to the CSV file
        for i in range(1, num_rows + 1):  # Loop through the specified number of rows (1 to num_rows inclusive)
            user_id = f"user_{(i % 50) + 1}"  # Generate a user ID cycling through 50 users (user_1 to user_50)
            day_number = i  # Assign the current row number as the day number
            steps = random.randint(1000, 200000)  # Generate a random number of steps between 1000 and 200000
            mintes_action = random.randint(0, 100)  # Generate a random number of minutes of action between 0 and 100
            writer.writerow([user_id, day_number, steps, mintes_action])  # Write the generated data to the CSV file

    # Now that we have exited the loop the file is saved and closed
    print(f"Large CSV file '{file_name}' created with {num_rows} rows.")  # Print a message indicating the file has been created

def load_dataset(the_file_name):  # Define a function to load data from a CSV file
        data = pd.read_csv(the_file_name)  # Read the CSV file into a pandas DataFrame it is called df in other places
        print(f"[INFO] Loaded dataset from '{the_file_name}'.")  # Print an error message if the file does not exist
        return data # Return the DataFrame containing the loaded data it is called df in other places
        
# Remember that this is for the formating and also the df means dataframe
def format_dataset(df):  # Define a function to format the dataset
    df = df.rename(columns={
            'user_id': 'UserID',
            'day_number': 'DayNumber',
            'steps': 'Steps',
            'mintes_action': 'MinutesAction'
        }
    )
    
    def categorize_steps(steps_value):
        if steps_value < 5000:
            return 'Low'
        elif steps_value < 10000:
            return 'Medium'
        else:
            return 'High'
    df['StepsCategory'] = df['Steps'].apply(categorize_steps)

    return df  # Return the formatted DataFrame


def display_results(df):  # Define a function to display results from the DataFrame

    print("==============================================") # Print a separator line for better readability
    print("First 10 rows of the formatted dataset:")  # Print a message indicating the first 5 rows will be displayed
    print(df.head(10))  # Print the first105 rows of the DataFrame
    print("==============================================") # Print a separator line for better readability
    
    
    print("\n==============================================") # Print a separator line for better readability
    print("Summary Statistics")  # Print a message indicating summary statistics will be displayed
    print("==============================================") # Print a separator line for better readability

    print(df.describe())  # Print summary statistics of the DataFrame



    print("\n==============================================") # Print a separator line for better readability
    print("Steps Category Counts:")  # Print a message indicating the counts of each steps category will be displayed
    print("==============================================") # Print a separator line for better readability

    print(df['StepsCategory'].value_counts())  # Print the counts of each category in the 'StepsCategory' column
    print("==============================================") # Print a separator line for better readability
    print("\n[INFO] Data display complete. For. the first time.")  # Print a message indicating that data display is complete


def main():  # Define the main function to orchestrate the workflow
    # This is point where the program starts executing
    # This is going to create the large csv file
    # format the dataset
    file_name = 'Big_daddy.csv'  # Specify the name of the CSV file to be created

    print("==============================================") # Print a separator line for better readability
    print("LARGE CSV FILE CREATION")  # Print a message indicating the start of the CSV file creation process
    print("==============================================") # Print a separator line for better readability

    if not os.path.exists(file_name):
        print(f"[INFO] Creating large CSV file '{file_name}'. Using existing dataset")  # Print a message indicating the start of the file creation process

        create_large_csv(file_name, num_rows=1000)  # Call the function to create a large CSV file with 1000 rows
    else:
        print(f"[INFO] Large CSV file '{file_name}' already exists. Using existing dataset.")
        print("==============================================") # Print a separator line for better readability

    df = load_dataset(file_name)  # Load the dataset from the CSV file

    df = format_dataset(df)  # Format the loaded dataset
    display_results(df)  # Display results from the formatted dataset
    print("==============================================") # Print a separator line for better readability
    print("\n[INFO] Program completed successfully.")  # Print a message indicating the program has completed successfully

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function to start the program