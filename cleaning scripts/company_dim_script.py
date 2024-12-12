import pandas as pd

# Load the CSV file
file_path = 'csv_files/company_dim.csv'  # Replace with your file path
output_path = 'cleaned data/cleaned_company_dim.csv'  # Specify the output file name

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)

# Check if 'thumbnail' column exists and remove it
if 'thumbnail' in df.columns:
    df.drop(columns=['thumbnail'], inplace=True)
    print("'thumbnail' column removed successfully.")
else:
    print("'thumbnail' column not found. No changes made.")

# Save the cleaned DataFrame to a new CSV file
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
