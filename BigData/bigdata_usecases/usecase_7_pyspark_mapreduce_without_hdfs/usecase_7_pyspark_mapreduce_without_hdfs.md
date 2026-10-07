# Use Case for MapReduce with Spark, without Hadoop/HDFS

**Use Case:** Employee Department Salary Analysis using Spark

## 1. Problem Statement

A company has employee salary data stored in a CSV file.

The requirement is to calculate:
1. Total salary paid by each department
2. Number of employees in each department
3. Average salary of each department

We will implement this using Apache Spark RDD MapReduce operations without using Hadoop or HDFS.

### Input
```csv
emp_id,name,department,salary
101,Rahul,IT,60000
102,Priya,HR,45000
103,Arun,IT,70000
104,Neha,Finance,55000
105,Kiran,HR,50000
106,Anita,Finance,65000
107,Ravi,IT,80000
```

### Expected Output
```csv
Finance,2,120000,60000.0
HR,2,95000,47500.0
IT,3,210000,70000.0
```

**Where:**
`Department`, `Employee_Count`, `Total_Salary`, `Average_Salary`

---

## 2. Technology Stack

| Component | Technology |
| :--- | :--- |
| Programming | Python |
| Processing | Apache Spark |
| API | Spark RDD |
| Execution Mode | Local |
| Input | Local CSV |
| Storage | Local Linux filesystem |
| Cluster Manager | None |
| Hadoop/HDFS | Not used |
| YARN | Not used |
| Database | Not required |

### Architecture Flow
```text
Local CSV File
      |
      v
 Apache Spark
      |
      v
    RDD
      |
      +---- map()
      |
      +---- reduceByKey()
      |
      +---- mapValues()
      |
      v
Local Output Directory
```

---

## 3. Why Spark Without Hadoop?

Normally you may see:
```text
Spark
  |
  v
HDFS
```

But Spark does not require Hadoop/HDFS to process data:
```text
Local File
    |
    v
Spark Local Mode
    |
    v
Local Output
```

Spark can directly read CSV, TXT, JSON, and Parquet files from the local filesystem. For a beginner, this is a good way to understand Spark processing before introducing HDFS.

---

## 4. Check Python

Open your Ubuntu/WSL terminal and run:

```bash
python3 --version
```

**Expected Output:**
```text
Python 3.12.3
```

Check pip:
```bash
pip3 --version
```

---

## 5. Check Java

Spark requires Java. Check your Java version:

```bash
java -version
```

> **Note:** Your current environment might have Java 8, but Spark 4.x requires Java 17 or later. If you want to use Java 8, keep Spark version 3.x.x.

Check installed Java versions:
```bash
ls /usr/lib/jvm/
```

You may see:
* `java-8-openjdk-amd64`
* `java-11-openjdk-amd64`
* `java-17-openjdk-amd64`
* `java-21-openjdk-amd64`

Configure Java for Spark:
```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

Verify:
```bash
java -version
```

**Expected Output:**
```text
openjdk version "17..."
```

---

## 6. Install PySpark

Create a virtual environment:
```bash
python3 -m venv ~/spark-venv
```

Activate it:
```bash
source ~/spark-venv/bin/activate
```

You should see your prompt prefixed with `(spark-venv)`. Upgrade pip and install PySpark:
```bash
pip install --upgrade pip
pip install pyspark
```

Check PySpark version:
```bash
pyspark --version
```

---

## 7. Create Project Directory

```bash
mkdir -p ~/spark-mapreduce-lab
cd ~/spark-mapreduce-lab
mkdir input output
```

Check directory structure:
```bash
find .
```

**Expected Output:**
```text
.
./input
./output
```

---

## 8. Create Input CSV

Create the input file:
```bash
nano input/employees.csv
```

Paste the following data:
```csv
emp_id,name,department,salary
101,Rahul,IT,60000
102,Priya,HR,45000
103,Arun,IT,70000
104,Neha,Finance,55000
105,Kiran,HR,50000
106,Anita,Finance,65000
107,Ravi,IT,80000
```

Verify the file content:
```bash
cat input/employees.csv
```

---

## 9. Understand the Input

For example, a record like:
```text
101,Rahul,IT,60000
```
means:
* Employee ID = `101`
* Name = `Rahul`
* Department = `IT`
* Salary = `60000`

---

## 10. Spark MapReduce Concept

We will use Spark RDD operations in this sequence:
```text
File()
   |
   v
map()
   |
   v
reduceByKey()
   |
   v
mapValues()
   |
   v
sortByKey()
   |
   v
saveAsFile()
```

### MapReduce Visual Flow
```text
              MAP
               |
               v
      (IT, (60000,1))
      (HR, (45000,1))
      (IT, (70000,1))
      (Finance,(55000,1))
               |
               v
            SHUFFLE
               |
               v
        Same keys together
               |
               v
             REDUCE
               |
               v
      IT      -> (210000,3)
      HR      -> (95000,2)
      Finance -> (120000,2)
```

---

## 11. Create Spark Program

Create the Python script:
```bash
nano employee_salary.py
```

Add the following code:

```python
from pyspark import SparkConf, SparkContext

# Create Spark configuration
conf = SparkConf().setAppName("EmployeeSalaryAnalysis").setMaster("local[*]")

# Create SparkContext
sc = SparkContext(conf=conf)

# Read input file
lines = sc.textFile("input/employees.csv")

# Remove header
header = lines.first()
data = lines.filter(lambda line: line != header)

# MAP
# Convert each record into: (department, (salary, employee_count))
mapped = data.map(
    lambda line: (
        line.split(",")[2],
        (int(line.split(",")[3]), 1)
    )
)

# REDUCE
# Add salaries and employee counts department-wise
reduced = mapped.reduceByKey(
    lambda x, y: (
        x[0] + y[0],
        x[1] + y[1]
    )
)

# Calculate average salary
result = reduced.mapValues(
    lambda x: (
        x[1],
        x[0],
        x[0] / x[1]
    )
)

# Sort by department
sorted_result = result.sortByKey()

# Display result
for department, values in sorted_result.collect():
    employee_count = values[0]
    total_salary = values[1]
    average_salary = values[2]

    print(
        department,
        employee_count,
        total_salary,
        average_salary
    )

# Save output
output = sorted_result.map(
    lambda x: (
        x[0],
        x[1][0],
        x[1][1],
        x[1][2]
    )
)

output.map(lambda x: ",".join(map(str, x))) \
      .coalesce(1) \
      .saveAsTextFile("output/department_salary")

# Stop Spark
sc.stop()
```

---

## 12. Understand the Mapper

The mapping step:
```python
mapped = data.map(
    lambda line: (
        line.split(",")[2],
        (int(line.split(",")[3]), 1)
    )
)
```
Transforms input rows like `101,Rahul,IT,60000` into key-value pairs like `(IT, (60000, 1))`.

---

## 13. Shuffle Stage

`reduceByKey()` automatically groups records sharing the same key before reduction takes place:
* **IT:** `(60000,1)`, `(70000,1)`, `(80000,1)`
* **HR:** `(45000,1)`, `(50000,1)`
* **Finance:** `(55000,1)`, `(65000,1)`

---

## 14. Reduce Stage

The reduction aggregates salaries and counts:
```python
reduced = mapped.reduceByKey(
    lambda x, y: (
        x[0] + y[0],
        x[1] + y[1]
    )
)
```
* **IT:** `210000`, `3` $\rightarrow$ `(210000, 3)`
* **HR:** `95000`, `2` $\rightarrow$ `(95000, 2)`
* **Finance:** `120000`, `2` $\rightarrow$ `(120000, 2)`

---

## 15. Calculate Average

```python
result = reduced.mapValues(
    lambda x: (
        x[1],
        x[0],
        x[0] / x[1]
    )
)
```
Calculates $\text{Average Salary} = \frac{\text{Total Salary}}{\text{Employee Count}}$.

---

## 16. Run the Spark Program

Ensure your virtual environment is active:
```bash
cd ~/spark-mapreduce-lab
source ~/spark-venv/bin/activate
spark-submit employee_salary.py
```

`local[*]` instructs Spark to use all available local CPU cores.

---

## 17. Expected Console Output

```text
Finance 2 120000 60000.0
HR 2 95000 47500.0
IT 3 210000 70000.0
```

---

## 18. Check and View Output

Check output folder contents:
```bash
ls output/department_salary
```
View the generated part file:
```bash
cat output/department_salary/part-*
```

**Expected Output:**
```csv
Finance,2,120000,60000.0
HR,2,95000,47500.0
IT,3,210000,70000.0
```

---

## 19. Summary Table of Operations

| Stage | Spark Operation | Purpose |
| :--- | :--- | :--- |
| Input | `textFile()` | Read CSV |
| Map | `map()` | Convert records to key-value pairs |
| Shuffle | `reduceByKey()` | Group same department keys |
| Reduce | `reduceByKey()` | Aggregate salary and count |
| Transformation | `mapValues()` | Calculate average |
| Output | `saveAsTextFile()` | Write local result |