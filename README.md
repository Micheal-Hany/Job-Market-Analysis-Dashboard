# Job Market Analysis Dashboard

This project focuses on analyzing job market data using SQL for data cleaning and processing, and Power BI for visualization. The dashboard serves two primary user groups:

1. **Job Seekers:** Individuals looking to explore career opportunities or make informed career decisions.
2. **Startup Owners:** Business owners aiming to identify high-potential markets and emerging trends.

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


## Project Features
get more Insights about job posting around world

### Insights for Job Seekers

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

[see dashboard](https://app.powerbi.com/links/DHigIDIGsK?ctid=dee1ed73-19ca-4ce0-8066-8261fbabbeaa&pbi_source=linkShare)


---

## Getting Started

1. Clone this repository.
2. Import the SQL scripts to your database and execute the queries.
3. Use the provided queries to visualize data in Power BI.

---

## Author

Michael Hany | [michealhany991@gmail.com](mailto:michealhany991@gmail.com) | Micheal-Hany

---

Feel free to contribute to this project by submitting issues or pull requests!
"""
#   J o b - M a r k e t - A n a l y s i s - D a s h b o a r d  
 