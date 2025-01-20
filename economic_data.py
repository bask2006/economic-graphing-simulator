import sqlite3
import pandas as pd
import os

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

# # Commit the transaction to save the changes
# connection.commit()

# # Print a confirmation message
# print("All data from EconomicData has been deleted.")



def insert_data_from_excel(file_path, indicator_id):
    # Read Excel file
    df = pd.read_excel(file_path)
    
    # Ensure that 'Value' column is numeric and clean any non-numeric values
    df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1], errors='coerce')  # Ensure the second column is numeric
    
    # Check if there is data in the file
    if df.empty:
        print(f"Warning: The file {file_path} is empty!")
        return

    # Iterate over the rows of the DataFrame
    for _, row in df.iterrows():
        year = row.iloc[0]  # Accessing year column (first column)
        value = row.iloc[1]  # Accessing value column (second column)

        # Skip any rows with invalid 'Value' (NaN values)
        if pd.isna(value):
            continue

        # Print for debugging
        print(f"Inserting data for IndicatorID {indicator_id}: Year = {year}, Value = {value}")
        
        # Insert data for each quarter of the year
        quarters = ['-03-31', '-06-30', '-09-30', '-12-31']  # End of Q1, Q2, Q3, Q4
        for quarter in quarters:
            date = f"{int(year)}{quarter}"
            cursor.execute("""
                INSERT INTO EconomicData (IndicatorID, Date, Value)
                VALUES (?, ?, ?)
            """, (indicator_id, date, value))
    
    # Commit changes
    connection.commit()

# Path to the 'cleaned_data' folder
folder_path = "cleaned_data"

# Mapping files to their corresponding IndicatorID (now in order from smallest to largest ID)
files_to_indicators = {
    "cleaned_gdp.xlsx": 1,                     # 'GDP' = IndicatorID 1
    "cleaned_unemployment.xlsx": 2,             # 'Unemployment Rate' = IndicatorID 2
    "cleaned_cpi.xlsx": 3,                     # 'Inflation Rate' = IndicatorID 3
    "cleaned_gdp_per_cap.xlsx": 4              # 'GDP Per Capita' = IndicatorID 4
}

# Iterate over the files and insert data, ensuring they are in order by indicator_id
for file_name, indicator_id in sorted(files_to_indicators.items(), key=lambda x: x[1]):
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        print(f"Processing file: {file_name} for IndicatorID {indicator_id}")
        insert_data_from_excel(file_path, indicator_id)
    else:
        print(f"File not found: {file_name}")

# Close the connection
connection.close()
