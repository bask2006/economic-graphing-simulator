import pandas as pd

# Step 1: Load the file and skip unnecessary rows
file_path = "unemployment.xlsx"
df = pd.read_excel(file_path, skiprows=8)  # Adjust 'skiprows' if needed to skip metadata rows

# Step 2: Filter rows where the first column contains "Year Qx"
# Keep rows where the format is like "1995 Q1", "2020 Q3", etc.
df = df[df.iloc[:, 0].str.contains(r'^\d{4} Q[1-4]$', na=False)]

# Step 3: Rename columns if necessary (e.g., Year and Value)
df.columns = ["Year", "Unemployment Rate"]  # Adjust column names based on your dataset

# Step 4: Remove "Qx" from the first column
df["Year"] = df["Year"].str.replace(r' Q[1-4]', '', regex=True)

# Step 5: Save the cleaned data into a new Excel file
cleaned_file_path = "cleaned_unemployment.xlsx"
df.to_excel(cleaned_file_path, index=False)

print(f"Data has been cleaned and saved to {cleaned_file_path}.")
