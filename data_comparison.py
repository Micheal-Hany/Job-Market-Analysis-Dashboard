import os
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data and compute data quality metrics


def get_data_quality_metrics(file_path):
    try:
        # Load data with the specified encoding (ISO-8859-1 is common for CSV issues)
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        print(f"Error decoding {file_path}, skipping this file.")
        return {}

    # Initialize a dictionary to store detailed metrics
    data_quality = {}

    # Compute the number of missing values per column
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * \
        100  # Percentage of missing values

    # Count duplicates
    duplicate_rows = df.duplicated().sum()

    # Get basic column information (number of columns, rows, and data types)
    data_types = df.dtypes
    column_info = {
        'Columns': len(df.columns),
        'Rows': len(df),
        'Data Types': data_types.value_counts()
    }

    # Compute unique values per column
    unique_values = df.nunique()

    # Basic statistics for numeric columns (mean, std, min, max, etc.)
    numeric_stats = df.describe()

    # Outlier detection: Calculate the Interquartile Range (IQR) for numeric columns
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    outliers = {}
    for col in numeric_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers[col] = df[(df[col] < lower_bound) | (
            df[col] > upper_bound)].shape[0]  # Count of outliers

    # Frequency counts for categorical columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    value_counts = {col: df[col].value_counts() for col in categorical_columns}

    # Store all metrics in the dictionary
    data_quality['Missing Values'] = missing_values.sum()
    data_quality['Missing Percentage'] = missing_percentage
    data_quality['Duplicate Rows'] = duplicate_rows
    data_quality['Unique Values'] = unique_values
    data_quality['Column Info'] = column_info
    data_quality['Numeric Statistics'] = numeric_stats
    data_quality['Outliers'] = outliers
    data_quality['Value Counts'] = value_counts

    return data_quality


# Define the directories for before and after cleaning
before_cleaning_dir = r"D:\Power BI Course\SQL\csv_files"
after_cleaning_dir = r"D:\Power BI Course\SQL\cleaned data"

# List of CSV files to compare
before_files = [f for f in os.listdir(
    before_cleaning_dir) if f.endswith('.csv')]
after_files = [f for f in os.listdir(after_cleaning_dir) if f.endswith('.csv')]

# Data structure to store the quality metrics
before_quality = {}
after_quality = {}

# Gather quality metrics for before cleaning data
for file in before_files:
    file_path = os.path.join(before_cleaning_dir, file)
    before_quality[file] = get_data_quality_metrics(file_path)

# Gather quality metrics for after cleaning data
for file in after_files:
    file_path = os.path.join(after_cleaning_dir, file)
    after_quality[file] = get_data_quality_metrics(file_path)

# Create a DataFrame for visualization
before_df = pd.DataFrame.from_dict(before_quality, orient='index')
after_df = pd.DataFrame.from_dict(after_quality, orient='index')

# Plot the comparison of missing values before and after cleaning
plt.figure(figsize=(12, 8))
plt.barh(before_df.index, before_df['Missing Values'],
         color='blue', alpha=0.6, label='Before Cleaning')
plt.barh(after_df.index, after_df['Missing Values'],
         color='green', alpha=0.6, label='After Cleaning')
plt.xlabel('Number of Missing Values')
plt.title('Missing Values Comparison')
plt.legend()
plt.tight_layout()
plt.show()

# Plot the comparison of duplicate rows before and after cleaning
plt.figure(figsize=(12, 8))
plt.barh(before_df.index, before_df['Duplicate Rows'],
         color='blue', alpha=0.6, label='Before Cleaning')
plt.barh(after_df.index, after_df['Duplicate Rows'],
         color='green', alpha=0.6, label='After Cleaning')
plt.xlabel('Number of Duplicate Rows')
plt.title('Duplicate Rows Comparison')
plt.legend()
plt.tight_layout()
plt.show()

# Save comparison results as a CSV for documentation
comparison_df = pd.concat([before_df[['Missing Values', 'Duplicate Rows']],
                           after_df[['Missing Values', 'Duplicate Rows']]],
                          axis=1, keys=['Before Cleaning', 'After Cleaning'])

comparison_df.to_csv("data_quality_comparison.csv")