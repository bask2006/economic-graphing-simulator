import pandas as pd

# Path to the cleaned Excel file
file_path = 'cleaned_gdp_per_cap.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Assume the column with "Qx" (e.g., "1995 Q1") is the first column (adjust if necessary)
# Remove "Q1", "Q2", "Q3", "Q4" from the strings in the first column
df.iloc[:, 0] = df.iloc[:, 0].str.replace(r' Q[1-4]', '', regex=True)

# Save the updated DataFrame back to the Excel file
df.to_excel(file_path, index=False)

print(f"'Q1', 'Q2', 'Q3', 'Q4' have been removed from the first column. Changes saved to {file_path}.")
