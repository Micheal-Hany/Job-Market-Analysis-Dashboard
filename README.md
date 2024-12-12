# Job Market Analysis Dashboard

This project focuses on analyzing job market data using Python and SQL for data cleaning and processing, and Power BI for visualization. The dashboard serves two primary user groups:

1. **Job Seekers:** Individuals looking to explore career opportunities or make informed career decisions.
2. **Startup Owners:** Business owners aiming to identify high-potential markets and emerging trends.

## lets understand Data
-  database schema
![database_schema](https://github.com/user-attachments/assets/458d6a80-7d32-4cc5-9055-8236fc1bb266)


## **[Date Before Cleaing](https://drive.google.com/drive/folders/1JszPD5y8bf2LhIAPwccrypQZdUhUFWwe?usp=sharing)**

---
## Data Cleaning & preparation 
## ```job_postings_fact``` 
- Filled values for ```avg_yearly_salary``` and ```avg_hourly_salary``` etc...
- No ```salary_rate``` column.
- Updated column names.
- Dates in ```job_posted_date``` column without the time part.
- Cleaned job_via values without the "via" prefix.

## ``` company_dim``` 
- Delete ```thumbnail``` column
- Replace Empty Values wth value

## **[Date After Cleaing](https://drive.google.com/drive/folders/1-v8bUaTvMCTNsIuVYk_Rv4K-4Sia2LU7?usp=sharing)**
---
## Graphs compare data Before & After Cleaing
- duplication in rows graph :
- ![duplcation in rows graph](https://github.com/user-attachments/assets/93e82acc-bb47-4cc4-8c89-4ff046d21e2e)
---
- missing values graph :
- ![missing values graph](https://github.com/user-attachments/assets/9098529f-252c-437c-9366-57f818fde4ee)

## Project Features
get more Insights about job posting around world

### Insights for Job Seekers
---
1. **Top Companies Hiring in a Specific Location or Industry**
   - **SQL Query:**
     ```sql
     SELECT company_dim.name AS company_name,
            COUNT(job_postings_fact.job_id) AS job_postings_count
     FROM job_postings_fact
     JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
     WHERE job_postings_fact.job_location IS NOT NULL
           AND job_postings_fact.job_title IS NOT NULL
     GROUP BY company_dim.name
     ORDER BY job_postings_count DESC
     LIMIT 10;
     ```
   - **Visualization:** Horizontal bar chart showing the top 10 hiring companies.
   - **Query Result:**
   - 
| Industry        | Job Count |
|-----------------|-----------|
| programming     | 1,398,696 |
| analyst_tools   | 632,696   |
| cloud           | 552,271   |
| libraries       | 521,217   |
| other           | 260,389   |
| databases       | 152,168   |
| os              | 60,279    |
| webframeworks   | 44,241    |
| async           | 39,697    |
| sync            | 7,950     |
---
2. **Job Titles with the Highest Average Salary**
   - **SQL Query:**
     ```sql
     SELECT job_title,
            AVG(COALESCE(salary_year_avg, random() * 13400)) AS avg_yearly_salary,
            AVG(COALESCE(salary_hour_avg, random() * 17800)) AS avg_hourly_salary
     FROM job_postings_fact
     WHERE job_postings_fact.job_location IS NOT NULL
     GROUP BY job_title
     ORDER BY avg_yearly_salary DESC
     LIMIT 10;
     ```
   - **Visualization:** Grouped bar chart comparing yearly and hourly salaries.
   - **Query Result:**
   -
| Job Title                                                   | Average Yearly Salary | Average Hourly Salary |
|-------------------------------------------------------------|-----------------------|-----------------------|
| Senior Data Engineer (Live Streaming)                       | $375,000              | $9,663.95             |
| Senior Data Engineer (ETL Pipelines)                        | $350,000              | $2,674.59             |
| Senior Data Engineer (Kafka)                                | $325,000              | $6,452.37             |
| Vice President of Data Platforms and Data Science           | $275,000              | $8,610.34             |
| Senior Director, Data Science                               | $273,555              | $7,635.56             |
| Lead SoC Architect, NPU AI/ML                               | $270,000              | $9,564.20             |
| Principal Data Engineer, Knowledge Graphs and Data Semantics| $269,500              | $6,938.33             |
| Principal Data Scientist - BCG X & BCG Fed (Pittsburgh, PA) | $253,000              | $5,167.63             |
| Principal, Data Scientist, Knowledge Management             | $250,000              | $8,185.98             |
| Vice President of Data Platforms & Data Science             | $250,000              | $4,690.37             |

---
3. **Most Frequently Required Skills in a Specific Industry or Role**
   - **SQL Query:**
     ```sql
     SELECT skills_dim.skills,
            COUNT(skills_job_dim.skill_id) AS skill_count
     FROM skills_job_dim
     JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
     JOIN job_postings_fact ON skills_job_dim.job_id = job_postings_fact.job_id
     WHERE job_postings_fact.job_title LIKE '%Data%'
     GROUP BY skills_dim.skills
     ORDER BY skill_count DESC
     LIMIT 10;
     ```
   - **Visualization:** Word cloud highlighting in-demand skills.
   - **Query Result:**
   - 
| Skill      | Skill Count |
|------------|-------------|
| sql        | 334,513     |
| python     | 332,300     |
| aws        | 124,049     |
| r          | 117,236     |
| azure      | 114,388     |
| tableau    | 108,698     |
| spark      | 105,005     |
| excel      | 96,984      |
| power bi   | 81,521      |
| sas        | 72,390      |
---
4. **Jobs Allowing Work-from-Home Flexibility**
   - **SQL Query:**
     ```sql
     SELECT job_title_short,
            job_schedule_type,
            job_location
     FROM job_postings_fact
     WHERE job_work_from_home = TRUE
     ORDER BY job_location;
     ```
   - **Visualization:** Table or pie chart showing the distribution of work-from-home jobs.
---
5. **Most Common Job Schedules**
   - **SQL Query:**
     ```sql
     SELECT job_schedule_type,
            COUNT(*) AS schedule_count
     FROM job_postings_fact
     WHERE job_postings_fact.job_location IS NOT NULL
     GROUP BY job_schedule_type
     ORDER BY schedule_count DESC
     LIMIT 10;
     ```
   - **Visualization:** Pie chart showing the proportions of different job schedules.
---
6. **Industries/Roles Offering Health Insurance Benefits**
   - **SQL Query:**
     ```sql
     SELECT job_title,
            COUNT(*) AS health_insurance_count
     FROM job_postings_fact
     WHERE job_health_insurance = TRUE
     GROUP BY job_title
     ORDER BY health_insurance_count DESC
     LIMIT 10;
     ```
   - **Visualization:** Horizontal bar chart highlighting roles with health insurance benefits.
---
7. **Companies/Roles That Do Not Require a Degree**
   - **SQL Query:**
     ```sql
     SELECT company_dim.name AS company_name,
            job_title
     FROM job_postings_fact
     JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
     WHERE job_postings_fact.job_no_degree_mention = TRUE
     ORDER BY company_name
     LIMIT 10;
     ```
   - **Visualization:** Table listing companies and roles that do not require a degree.
---
8. **Top Ten Websites Posting Jobs**
   - **SQL Query:**
```sql
SELECT job_via, COUNT(*) AS job_count
FROM public.job_postings_fact
GROUP BY job_via
ORDER BY job_count DESC
LIMIT 10;
```
- **Visualization:** A bar chart in Power BI would effectively display the top ten job posting websites with the number of jobs posted on each..
---
9. **Most Common Job Publish Time**
   - **SQL Query:**
```sql
SELECT 
    TO_CHAR(job_posted_date, 'Month') AS publish_month, 
    COUNT(*) AS frequency
FROM 
    public.job_postings_fact
GROUP BY 
    publish_month
ORDER BY 
    frequency DESC;
```
- **Visualization:** A column chart in Power BI would work well to show the frequency of job postings per month. You can use months as the axis and the count of job postings as the values.
---

10. **Job Postings by Industry**
   - **SQL Query:**
```sql

SELECT s.type AS skill_type, COUNT(*) AS job_count
FROM skills_job_dim sj
JOIN skills_dim s ON sj.skill_id = s.skill_id
GROUP BY s.type
ORDER BY job_count DESC;
```
- **Visualization:** 
---


## Technologies Used

- **Python:** for data cleaning .
- **SQL:** for get Insights
- **Power BI:** To create interactive visualizations and dashboards.

## libraries or frameworks

 - **pandas:** Python library for cleaning data.
 - **PostgreSQL:**  enterprise-class open-source relational database that supports both SQL (relational) and JSON (non-relational) querying
 - **Vscode:** for runing queries 
---
## **[Dashboard](https://app.powerbi.com/links/DHigIDIGsK?ctid=dee1ed73-19ca-4ce0-8066-8261fbabbeaa&pbi_source=linkShare)**
---
## Getting Started

Follow these steps to set up and use the project:
## Required Technologies

- Python 3.11.9
- Git
- PostgreSQL

3. **Clone the Repository :**  

   ```bash
   git clone https://github.com/Micheal-Hany/Job-Market-Analysis-Dashboard.git

---

## Author

Michael Hany | [michealhany991@gmail.com](mailto:michealhany991@gmail.com) | [Micheal-Hany](https://www.linkedin.com/in/michael-hany-572034262/)

---

Feel free to contribute to this project by submitting issues or pull requests

