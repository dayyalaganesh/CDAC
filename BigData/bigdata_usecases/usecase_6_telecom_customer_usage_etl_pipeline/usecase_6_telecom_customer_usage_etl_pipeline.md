# Use Case 6: Telecom Customer Usage ETL Pipeline using Airflow, HDFS, and Hive

## Problem Statement

A telecom company collects daily customer usage information in a CSV file. The file contains details such as customer ID, mobile plan, call minutes, sms count, data consumed, usage date, and telecom circle.

The company wants to build a simple ETL pipeline to process this data automatically. You are required to develop an Airflow-based ETL pipeline with the following stages:

---

## Pipeline Stages

### 1. Extract
Read the telecom usage CSV file from the given input location. The input data should contain the following fields:
* `usage_id`
* `customer_id`
* `plan`
* `call_minutes`
* `sms_count`
* `data_gb`
* `usage_date`
* `circle`

#### Raw Input Data (`telecom_usage.csv`)
```csv
usage_id,customer_id,plan,call_minutes,sms_count,data_gb,usage_date,circle
U001,C101,Premium,450,120,8.5,2026-09-25,Bangalore
U002,C102,Basic,120,45,2.3,2026-09-25,Mysore
U003,C103,Premium,620,180,15.2,2026-09-25,Bangalore
U004,C104,Basic,210,60,4.5,2026-09-26,Chennai
U005,C105,Premium,580,150,10.5,2026-09-26,Hyderabad
U006,C106,Basic,95,30,1.8,2026-09-26,Mangalore
U007,C107,Premium,710,220,18.7,2026-09-27,Bangalore
U008,C108,Basic,165,55,6.2,2026-09-27,Mysore
U009,C109,Premium,490,135,9.9,2026-09-27,Chennai
U010,C110,Basic,250,75,10.0,2026-09-28,Hyderabad
U011,C111,Premium,530,160,12.4,2026-09-28,Bangalore
U012,C112,Basic,140,40,3.7,2026-09-28,Mangalore
U013,C113,Premium,680,200,20.1,2026-09-29,Chennai
U014,C114,Basic,190,65,7.5,2026-09-29,Mysore
U015,C115,Premium,455,110,9.5,2026-09-29,Hyderabad
```

Store the raw input data in HDFS.

---

### 2. Load Raw Data into Hive
* Create a Hive table named: `telecom_usage_raw`
* Load the data from HDFS into this table.
* The raw table should preserve the original data without applying any transformation.

---

### 3. Transform
The business team wants to categorize customers based on their data usage. Apply the following business requirement:

> **Customers who consume 10 GB or more data should be classified as `HIGH` usage customers. All other customers should be classified as `NORMAL` usage customers.**

* Create a transformed Hive table named: `telecom_usage_final`
* The final table should contain all the original columns along with a new column: `usage_category`
* The value of `usage_category` must be derived from `data_gb` according to the business requirement.

---

### 4. Airflow Orchestration
Create an Airflow DAG to automate the complete pipeline. The DAG should perform the activities in the following order:

```text
Input CSV
   ↓
Store Raw Data in HDFS
   ↓
Create/Load Hive Raw Table
   ↓
Apply Transformation
   ↓
Create Hive Final Table
```

The tasks must execute in the correct sequence using Airflow dependencies.

---

## Expected Output

The final Hive table should contain data similar to:

| usage_id | customer_id | plan | data_gb | circle | usage_category |
| :--- | :--- | :--- | :---: | :--- | :--- |
| U001 | C101 | Premium | 8.5 | Bangalore | NORMAL |
| U002 | C102 | Basic | 2.3 | Mysore | NORMAL |
| U003 | C103 | Premium | 15.2 | Bangalore | HIGH |
| U004 | C104 | Basic | 4.5 | Chennai | NORMAL |
| U005 | C105 | Premium | 10.5 | Hyderabad | HIGH |

---

## Requirements Checklist

1. Create the required project directory structure.
2. Prepare the telecom usage input CSV file.
3. Upload/store the raw data in HDFS.
4. Create the Hive raw table.
5. Load the data into the raw table.
6. Implement the required business transformation.
7. Create the final Hive table.
8. Create an Airflow DAG to orchestrate the ETL process.
9. Execute the DAG successfully.
10. Verify the final output using Hive queries.

---

## Verification Criteria

Students must demonstrate:
* HDFS contains the raw input data.
* `telecom_usage_raw` contains the original records.
* `telecom_usage_final` contains the transformed records.
* `usage_category` is correctly generated based on `data_gb`.
* The complete workflow is successfully executed through Airflow.

> **Important Note:** Do not modify the original raw data while performing the transformation. The transformation should be applied while creating the final Hive table.