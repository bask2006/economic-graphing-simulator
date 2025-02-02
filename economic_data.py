import sqlite3
import pandas as pd
import os
from datetime import datetime

# Define connection and cursor
connection = sqlite3.connect("economic_data.db")
cursor = connection.cursor()

# Create Indicators table
command1 = """
CREATE TABLE IF NOT EXISTS Indicators (
    IndicatorID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);
"""
cursor.execute(command1)

# cursor.execute("DELETE FROM Indicators")
# cursor.execute("INSERT INTO Indicators VALUES (1, 'GDP')")
# cursor.execute("INSERT INTO Indicators VALUES (2, 'Unemployment Rate')")
# cursor.execute("INSERT INTO Indicators VALUES (3, 'Inflation Rate')")
# cursor.execute("INSERT INTO Indicators VALUES (4, 'GDP Per Capita')")
# connection .commit()

# cursor.execute("SELECT * FROM Indicators")
# results = cursor.fetchall()
# print(results)

# Create Users table
command2 = """
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);
"""
cursor.execute(command2)

# Create EconomicData table
command3 = """
CREATE TABLE IF NOT EXISTS EconomicData (
    DataID INTEGER PRIMARY KEY,
    IndicatorID INTEGER NOT NULL,
    Date DATE NOT NULL,
    Value DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID)
);
"""
cursor.execute(command3)

# Create UserInputs table
command4 = """
CREATE TABLE IF NOT EXISTS UserInputs (
    InputID INTEGER PRIMARY KEY,
    UserID INTEGER NOT NULL,
    IndicatorID INTEGER NOT NULL,
    CustomValue DECIMAL(15, 2) NOT NULL,
    InputDate DATE NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID)
);
"""
cursor.execute(command4)

# Create Graphs table
command5 = """
CREATE TABLE IF NOT EXISTS Graphs (
    GraphID INTEGER PRIMARY KEY,
    UserID INTEGER NOT NULL,
    IndicatorID INTEGER NOT NULL,
    GraphType TEXT NOT NULL,
    Parameters TEXT,
    CreateTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID)
);
"""
cursor.execute(command5)

# # Delete all data from the EconomicData table
# cursor.execute("DELETE FROM EconomicData")
# connection.commit()


###
# # Insert this data FIRST into the EconomicData table:

# # Load the data from the cleaned_gdp.xlsx file
# excel_file = 'cleaned_gdp.xlsx'  # Replace with your actual file path
# data = pd.read_excel(excel_file, header=None)  # Load data without a header row

# # Display the first few rows of the data to check its structure
# print(data.head())

# # Add IndicatorID for GDP data (assuming it's IndicatorID = 1 for GDP)
# data['IndicatorID'] = 1

# # Create a new column to store the corresponding quarter date
# quarters = ['01-01', '04-01', '07-01', '10-01']  # The start dates for each quarter

# # Update the Date column with the full date including the quarter
# dates = []
# for idx, year in enumerate(data[0]):
#     quarter = quarters[idx % 4]  # Cycle through the quarters
#     date = f"{int(year)}-{quarter}"
#     dates.append(date)

# data['Date'] = dates

# # Rename the second column to 'Value'
# data['Value'] = data[1]

# # Drop the old columns (keep only IndicatorID, Date, and Value)
# data = data[['IndicatorID', 'Date', 'Value']]

# # Verify the changes in the DataFrame
# print(data.head())

# # Connect to the economic_data.db database
# db_connection = sqlite3.connect('economic_data.db')  # Use your database file name
# cursor = db_connection.cursor()

# # Insert data into the EconomicData table
# for index, row in data.iterrows():
#     try:
#         query = """
#         INSERT INTO EconomicData (IndicatorID, Date, Value)
#         VALUES (?, ?, ?)
#         """
#         cursor.execute(query, (row['IndicatorID'], row['Date'], row['Value']))
#     except Exception as e:
#         print(f"Error inserting row {index}: {e}")

# # Commit the transaction and close the connection
# db_connection.commit()
# db_connection.close()

# print("Data successfully inserted into the EconomicData table.")

# # Verify the data has been inserted correctly
# connection = sqlite3.connect("economic_data.db")
# cursor = connection.cursor()
# cursor.execute("SELECT COUNT(*) FROM EconomicData")
# count = cursor.fetchone()
# print(f"Number of rows in EconomicData: {count[0]}")

# # Retrieve the data to verify
# cursor.execute("SELECT * FROM EconomicData")
# results = cursor.fetchall()
# print(results)

# connection.close()
###





###
# # Insert this data SECOND into the EconomicData table:

# # Load the data from the cleaned_unemployment.xlsx file
# excel_file = 'cleaned_unemployment.xlsx'  # Replace with your actual file path
# data = pd.read_excel(excel_file, header=None)  # Load data without a header row

# # Display the first few rows of the data to check its structure
# print(data.head())

# # Add IndicatorID for Unemployment data (assuming it's IndicatorID = 2 for Unemployment)
# data['IndicatorID'] = 2

# # Create a new column to store the corresponding quarter date
# quarters = ['01-01', '04-01', '07-01', '10-01']  # The start dates for each quarter

# # Update the Date column with the full date including the quarter
# dates = []
# for idx, year in enumerate(data[0]):
#     quarter = quarters[idx % 4]  # Cycle through the quarters
#     date = f"{int(year)}-{quarter}"
#     dates.append(date)

# data['Date'] = dates

# # Rename the second column to 'Value'
# data['Value'] = data[1]

# # Drop the old columns (keep only IndicatorID, Date, and Value)
# data = data[['IndicatorID', 'Date', 'Value']]

# # Verify the changes in the DataFrame
# print(data.head())

# # Connect to the economic_data.db database
# db_connection = sqlite3.connect('economic_data.db')  # Use your database file name
# cursor = db_connection.cursor()

# # Insert data into the EconomicData table
# for index, row in data.iterrows():
#     try:
#         query = """
#         INSERT INTO EconomicData (IndicatorID, Date, Value)
#         VALUES (?, ?, ?)
#         """
#         cursor.execute(query, (row['IndicatorID'], row['Date'], row['Value']))
#     except Exception as e:
#         print(f"Error inserting row {index}: {e}")

# # Commit the transaction and close the connection
# db_connection.commit()
# db_connection.close()

# print("Data successfully inserted into the EconomicData table.")

# # Verify the data has been inserted correctly
# connection = sqlite3.connect("economic_data.db")
# cursor = connection.cursor()
# cursor.execute("SELECT COUNT(*) FROM EconomicData")
# count = cursor.fetchone()
# print(f"Number of rows in EconomicData: {count[0]}")

# # Retrieve the data to verify
# cursor.execute("SELECT * FROM EconomicData WHERE IndicatorID = 2")
# results = cursor.fetchall()
# print(results)

# connection.close()
###




###
# # Insert this data THIRD into the EconomicData table:

# # Load the data from the Excel file
# excel_file = 'cleaned_cpi.xlsx'  # Replace with your actual file path
# data = pd.read_excel(excel_file, header=None)  # Load data without a header row

# # Display the first few rows of the data to check its structure
# print(data.head())

# # Add IndicatorID for CPI data (assuming it's IndicatorID = 3 for CPI)
# data['IndicatorID'] = 3

# # Create a new column to store the corresponding quarter date
# quarters = ['01-01', '04-01', '07-01', '10-01']  # The start dates for each quarter

# # Update the Date column with the full date including the quarter
# dates = []
# for idx, year in enumerate(data[0]):
#     quarter = quarters[idx % 4]  # Cycle through the quarters
#     date = f"{int(year)}-{quarter}"
#     dates.append(date)

# data['Date'] = dates

# # Rename the second column to 'Value'
# data['Value'] = data[1]

# # Drop the old columns (keep only IndicatorID, Date, and Value)
# data = data[['IndicatorID', 'Date', 'Value']]

# # Verify the changes in the DataFrame
# print(data.head())

# # Connect to the economic_data.db database
# db_connection = sqlite3.connect('economic_data.db')  # Use your database file name
# cursor = db_connection.cursor()

# # Insert data into the EconomicData table
# for index, row in data.iterrows():
#     try:
#         query = """
#         INSERT INTO EconomicData (IndicatorID, Date, Value)
#         VALUES (?, ?, ?)
#         """
#         cursor.execute(query, (row['IndicatorID'], row['Date'], row['Value']))
#     except Exception as e:
#         print(f"Error inserting row {index}: {e}")

# # Commit the transaction and close the connection
# db_connection.commit()
# db_connection.close()

# print("Data successfully inserted into the EconomicData table.")

# # Verify the data has been inserted correctly
# connection = sqlite3.connect("economic_data.db")
# cursor = connection.cursor()
# cursor.execute("SELECT COUNT(*) FROM EconomicData")
# count = cursor.fetchone()
# print(f"Number of rows in EconomicData: {count[0]}")

# # Retrieve the data to verify
# cursor.execute("SELECT * FROM EconomicData")
# results = cursor.fetchall()
# print(results)

# connection.close()
###





###
# # Insert this data LAST into the database

# # Load the data from the cleaned_gdp_cap.xlsx file
# excel_file = 'cleaned_gdp_per_cap.xlsx'  # Replace with your actual file path
# data = pd.read_excel(excel_file, header=None)  # Load data without a header row

# # Display the first few rows of the data to check its structure
# print(data.head())

# # Add IndicatorID for GDP per Capita data (assuming it's IndicatorID = 4 for GDP Per Capita)
# data['IndicatorID'] = 4

# # Create a new column to store the corresponding quarter date
# quarters = ['01-01', '04-01', '07-01', '10-01']  # The start dates for each quarter

# # Update the Date column with the full date including the quarter
# dates = []
# for idx, year in enumerate(data[0]):
#     quarter = quarters[idx % 4]  # Cycle through the quarters
#     date = f"{int(year)}-{quarter}"
#     dates.append(date)

# data['Date'] = dates

# # Rename the second column to 'Value'
# data['Value'] = data[1]

# # Drop the old columns (keep only IndicatorID, Date, and Value)
# data = data[['IndicatorID', 'Date', 'Value']]

# # Verify the changes in the DataFrame
# print(data.head())

# # Connect to the economic_data.db database
# db_connection = sqlite3.connect('economic_data.db')  # Use your database file name
# cursor = db_connection.cursor()

# # Insert data into the EconomicData table
# for index, row in data.iterrows():
#     try:
#         query = """
#         INSERT INTO EconomicData (IndicatorID, Date, Value)
#         VALUES (?, ?, ?)
#         """
#         cursor.execute(query, (row['IndicatorID'], row['Date'], row['Value']))
#     except Exception as e:
#         print(f"Error inserting row {index}: {e}")

# # Commit the transaction and close the connection
# db_connection.commit()
# db_connection.close()

# print("Data successfully inserted into the EconomicData table.")

# # Verify the data has been inserted correctly
# connection = sqlite3.connect("economic_data.db")
# cursor = connection.cursor()
# cursor.execute("SELECT COUNT(*) FROM EconomicData")
# count = cursor.fetchone()
# print(f"Number of rows in EconomicData: {count[0]}")

# # Retrieve the data to verify
# cursor.execute("SELECT * FROM EconomicData WHERE IndicatorID = 4")
# results = cursor.fetchall()
# print(results)

# connection.close()

###


cursor.execute("SELECT * FROM EconomicData")
results = cursor.fetchall()
print(results)