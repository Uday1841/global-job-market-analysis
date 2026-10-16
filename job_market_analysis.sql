#Creating table in side Database
-- USE job_market_clean;
-- CREATE TABLE job_market_dataset_full (
--     country TEXT,
--     city TEXT,
--     occupation TEXT,
--     field TEXT,
--     years_of_experience INT,
--     salary INT,
--     employment_type TEXT,
--     education_level TEXT,
--     gender TEXT,
--     company_size TEXT,
--     year INT,
--     month INT
-- );

#--Checking the coulmns was created are not
-- SELECT COUNT(*) AS total_records
-- FROM job_market_dataset_full;

-- DESCRIBE job_market_dataset_full;

#--Loding the csv data into the SQL on by quicly
-- LOAD DATA LOCAL INFILE 'E:/Uday Kumar/Power BI/job_market_dataset.csv'
-- INTO TABLE job_market_dataset_full
-- CHARACTER SET utf8mb4
-- FIELDS TERMINATED BY ','
-- OPTIONALLY ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES
-- (country, city, occupation, field, years_of_experience,
--  salary, employment_type, education_level, gender,
--  company_size, year, month);

#--Checking how many records have been Created
-- SELECT COUNT(*) AS total_records
-- FROM job_market_dataset_full;


#--Query 1: Average salary by occupation
-- select occupation,avg(salary) AS Average_Salary,count(*) as job_Records
-- from job_market_dataset_full
-- group by occupation
-- order by Average_Salary Desc;

#--Query 2: Highest-paying countries
-- select country, Avg(salary) As Average_Salary, count(*) as job_records
-- from job_market_dataset_full
-- group by country
-- order by Average_Salary DESC;

#--Query 3: Salary by education level
-- SELECT education_level, AVG(salary) AS average_salary, COUNT(*) AS job_records
-- FROM job_market_dataset_full
-- GROUP BY education_level
-- ORDER BY average_salary DESC;

#--Query 4: Salary by years of experience
-- select years_of_experience, Avg(salary) as Average_Salary, count(*) AS Job_Records
-- from job_market_dataset_full
-- group by years_of_experience
-- order by Average_Salary DESC;

#--Query 5: Job market trends by year
-- select year , count(*) as Job_Records, AVG(salary) as Average_Salary
-- from job_market_dataset_full
-- group by year
-- order by year;

#--Query 6: Employment type analysis
-- SELECT
--     employment_type,
--     COUNT(*) AS job_records,
--     AVG(salary) AS average_salary
-- FROM job_market_dataset_full
-- GROUP BY employment_type
-- ORDER BY average_salary DESC;

#--Query 7 — Salary by company size
-- SELECT
--     company_size,
--     AVG(salary) AS average_salary,
--     COUNT(*) AS job_records
-- FROM job_market_dataset_full
-- GROUP BY company_size
-- ORDER BY average_salary DESC;

#--Query 8 — Job opportunities by country
-- SELECT
--     country,
--     COUNT(*) AS job_records
-- FROM job_market_dataset_full
-- GROUP BY country
-- ORDER BY job_records DESC
-- LIMIT 10;

#--Query 9 — Salary by gender
-- SELECT
--     gender,
--     AVG(salary) AS average_salary,
--     COUNT(*) AS job_records
-- FROM job_market_dataset_full
-- GROUP BY gender
-- ORDER BY average_salary DESC;
