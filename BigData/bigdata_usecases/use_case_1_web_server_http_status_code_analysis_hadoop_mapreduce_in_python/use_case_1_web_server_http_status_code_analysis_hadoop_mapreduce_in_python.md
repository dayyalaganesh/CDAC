# USE CASE 1: Web Server HTTP Status Code Analysis

## 1. Problem Statement

A company maintains millions of web-server access logs in HDFS. The data engineering team wants to analyze the logs and determine how many requests were received for each HTTP status code.

For example:
- $200 \to$ Successful request
- $404 \to$ Page not found
- $500 \to$ Server error

The MapReduce program should:
1. Read web-server logs from HDFS.
2. Extract the HTTP status code.
3. Generate `(status_code, 1)` from the Mapper.
4. Use a Combiner for local aggregation.
5. Use a custom Partitioner to distribute status codes among Reducers.
6. Shuffle and group (sort) identical status codes.
7. Use the Reducer to calculate the final count.
8. Store the result in HDFS.

---

## 2. Sample Input

`web_logs.txt`
```text
192.168.1.10 GET /home 200
192.168.1.11 GET /login 200
192.168.1.12 GET /product 404
192.168.1.13 GET /home 200
192.168.1.14 GET /checkout 500
192.168.1.15 GET /product 404
192.168.1.16 GET /home 200
192.168.1.17 GET /server 500
```

---

## 3. Expected Output

```text
200    4
404    2
500    2
```

Meaning:
- HTTP $200 \to 4$ requests
- HTTP $404 \to 2$ requests
- HTTP $500 \to 2$ requests

---

## 4. Technology Stack

| Component | Technology |
| :--- | :--- |
| Operating System | Ubuntu / WSL |
| Programming Language | Java |
| Processing | Hadoop MapReduce |
| Storage | HDFS |
| Mapper | Java |
| Combiner | Java |
| Partitioner | Custom Java |
| Reducer | Java |
| Execution | Hadoop YARN |
| Input | Text file |
| Output | HDFS |

---

## 5. Complete Architecture

```text
                 Web Server Logs
                       |
                       v
                      HDFS
                       |
                       v
                +--------------+
                | Java Mapper  |
                +--------------+
                       |
             (200,1), (200,1)
             (404,1), (500,1)
                       |
                       v
                +--------------+
                |   Combiner   |
                +--------------+
                       |
                 (200,2)
                 (404,1)
                 (500,1)
                       |
                       v
                +--------------+
                |  Partitioner |
                +--------------+
                   /          \
                  /            \
                 v              v
          Reducer 0          Reducer 1
               |                 |
               +-------+---------+
                       |
                  Shuffle/Sort
                       |
                       v
                  Reducer
                       |
                       v
                      HDFS
                       |
                       v
                 Final Output
```

---

## 6. Map Stage

The Mapper reads:
`192.168.1.10 GET /home 200`

and generates:
`200    1`

Another record:
`192.168.1.12 GET /product 404`

generates:
`404    1`

So Mapper output could be:
```text
200    1
200    1
404    1
200    1
500    1
404    1
200    1
500    1
```

---

## 7. Combiner Stage

The Combiner performs local aggregation. For example, if one Mapper produces:
```text
200    1
200    1
200    1
404    1
```
The Combiner can produce:
```text
200    3
404    1
```

This reduces the amount of intermediate data transferred over the network.

> **Interview point:** Combiner is a local mini-reducer. It reduces intermediate data before it is transferred to Reducers.
> **Important:** Combiner is optional. Hadoop does not guarantee that it will execute.

---

## 8. Partitioner Stage

The Partitioner decides which Reducer receives each key. For example:
- $200 \to$ Reducer 0
- $404 \to$ Reducer 1
- $500 \to$ Reducer 1

The important rule is:
> All values belonging to the same key must go to the same Reducer.

---

## 9. Shuffle and Sort

Hadoop groups the values belonging to the same key:
- $200 \to [1, 1, 1, 1]$
- $404 \to [1, 1]$
- $500 \to [1, 1]$

---

## 10. Reduce Stage

The Reducer receives the grouped key-value collections and calculates final counts:
```text
200    4
404    2
500    2
```
Stored finally in HDFS.