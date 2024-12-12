import pandas as pd

# Load the CSV file with specified encoding
#  job_postings_fact
file_path = 'PATH TO job_postings_fact FILE'
df = pd.read_csv(file_path, encoding='ISO-8859-1', low_memory=False)

# Print column names to verify
print("Columns in the dataset:", df.columns)

# Fill missing values in 'salary_year_avg' and 'salary_hour_avg' with their means
df['salary_year_avg'].fillna(df['salary_year_avg'].mean(), inplace=True)
df['salary_hour_avg'].fillna(df['salary_hour_avg'].mean(), inplace=True)

# Fill missing or empty values in 'job_schedule_type' and 'job_location'
df['job_schedule_type'] = df['job_schedule_type'].fillna('Contractor')
df['job_schedule_type'] = df['job_schedule_type'].replace('', 'Contractor')

df['job_location'] = df['job_location'].fillna('Egypt')
df['job_location'] = df['job_location'].replace('', 'Egypt')

# Drop 'salary_rate' column if it exists
if 'salary_rate' in df.columns:
    df.drop(columns=['salary_rate'], inplace=True)
else:
    print("'salary_rate' column not found. Skipping drop operation.")

# Rename columns to follow snake_case convention
column_mapping = {
    'job_id': 'job_id',
    'company_id': 'company_id',
    'job_title_short': 'job_title_short',
    'job_title': 'job_title',
    'job_location': 'job_location',
    'job_via': 'job_via',
    'job_schedule_type': 'job_schedule_type',
    'job_work_from_home': 'job_work_from_home',
    'search_location': 'search_location',
    'job_posted_date': 'job_posted_date',
    'job_no_degree_mention': 'job_no_degree_mention',
    'job_health_insurance': 'job_health_insurance',
    'job_country': 'job_country',
    'salary_year_avg': 'avg_yearly_salary',
    'salary_hour_avg': 'avg_hourly_salary'
}
df.rename(columns=column_mapping, inplace=True)

# Extract only the date from 'job_posted_date'
if 'job_posted_date' in df.columns:
    df['job_posted_date'] = pd.to_datetime(df['job_posted_date']).dt.date
else:
    print("'job_posted_date' column not found. Skipping date extraction.")

# Remove "via " prefix from 'job_via'
df['job_via'] = df['job_via'].str.replace('via ', '', regex=False)

# Save the cleaned data to a new CSV file
output_path = 'cleaned data/cleaned_job_postings_fact.csv'
df.to_csv(output_path, index=False)

print(f"Data cleaned and saved to {output_path}")
