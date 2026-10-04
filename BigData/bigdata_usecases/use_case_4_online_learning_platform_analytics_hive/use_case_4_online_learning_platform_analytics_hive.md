# USE CASE 4: Online Learning Platform Analytics Using Hive

## 1. Problem Statement

An online learning platform stores information about learners, courses, and course enrollments. The data engineering team needs to build a Hive-based analytics system to answer questions such as:
- Which learners are enrolled in which courses?
- Which courses have the highest number of enrollments?
- Which learners have not enrolled in any course?
- Which courses currently have no learners?
- How can small reference tables (like course metadata) be joined efficiently with a large enrollment table via **Map-Side Joins**?
- How can enrollment data be partitioned by date or category so that queries process only the required data?

---

## 2. Step-by-Step Execution Workflow

1. Start Hadoop ecosystem services (HDFS, YARN).
2. Create local CSV files (`learners.csv`, `courses.csv`, `enrollments.csv`).
3. Upload raw data into HDFS directories.
4. Start the Hive CLI/Beeline interface.
5. Create and use a dedicated database (`CREATE DATABASE online_learning;`).
6. Create an **Internal / Managed Table** for learners.
7. Load data using `LOAD DATA LOCAL INPATH`.
8. Create an **External Table** pointing to raw HDFS data for courses.
9. Load data using `LOAD DATA INPATH` (from HDFS).
10. Create the large enrollment table.
11. Perform **Inner Joins** to see active enrollments.
12. Perform **Left / Right / Full Outer Joins** to identify missing enrollments or inactive courses.
13. Execute a **Map-Side Join** optimization using hints for small lookup tables.
14. Create a **Partitioned Table** for enrollments based on course categories or dates.
15. Insert data into partitions (`INSERT INTO TABLE ... PARTITION (...)`).
16. Show partitions and query partitioned data to save cluster scan cost.

---

## 3. Core HiveQL Code Patterns

```sql
-- Create Database
CREATE DATABASE IF NOT EXISTS online_learning;
USE online_learning;

-- Create Managed Table for Courses
CREATE TABLE IF NOT EXISTS courses (
    course_id INT,
    course_name STRING,
    category STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Load Data from Local
LOAD DATA LOCAL INPATH '/home/user/courses.csv' INTO TABLE courses;

-- Create External Table for Enrollments
CREATE EXTERNAL TABLE IF NOT EXISTS enrollments (
    enrollment_id INT,
    learner_id INT,
    course_id INT,
    enroll_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/hive/warehouse/enrollments';

-- Partitioned Table Example
CREATE TABLE IF NOT EXISTS enrollments_partitioned (
    enrollment_id INT,
    learner_id INT,
    course_id INT
)
PARTITIONED BY (enroll_date STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS PARQUET;
```