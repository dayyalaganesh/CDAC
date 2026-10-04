# USE CASE 2: Social Media Hashtag Analysis

## 1. Problem Statement

A social-media platform stores user posts in HDFS. Each post contains information such as post ID, username, caption, and hashtags. The data engineering team wants to determine how many posts contain each hashtag.

The MapReduce application should:
1. Read social-media post data from HDFS.
2. Extract hashtags.
3. Generate `(hashtag, 1)` using a Python Mapper.
4. Use a Combiner for local aggregation.
5. Use Hadoop's Partitioner to distribute hashtags among Reducers.
6. Shuffle and group identical hashtags.
7. Calculate the final hashtag frequency.
8. Store the result in HDFS.

---

## 2. Sample Input

`social_posts.txt`
```text
P1001 rahul #python #hadoop #bigdata
P1002 priya #python #spark
P1003 amit #hadoop #spark #bigdata
P1004 neha #python #bigdata
```

---

## 3. Expected Output

```text
#bigdata    3
#hadoop     2
#python     3
#spark      2
```

---

## 4. Technology Stack

| Component | Technology |
| :--- | :--- |
| Operating System | Ubuntu / WSL |
| Programming Language | Python |
| Processing | Hadoop MapReduce |
| Storage | HDFS |
| Mapper | Python |
| Combiner | Python |
| Partitioner | Hadoop Default Partitioner |
| Reducer | Python |
| Execution | Hadoop Streaming |
| Input | Text / semi-structured data |
| Output | HDFS |

> **Why Python here?** Hadoop MapReduce is traditionally associated with Java, but Hadoop Streaming allows programs written in languages such as Python to participate in MapReduce via standard input/output streams.

---

## 5. Complete Architecture

```text
             Social Media Posts
                     |
                     v
                    HDFS
                     |
                     v
              Python Mapper
                     |
       +-------------+-------------+
       |             |             |
   #python,1     #hadoop,1    #bigdata,1
       |             |             |
       +-------------+-------------+
                     |
                     v
                Combiner
                     |
             Local aggregation
                     |
                     v
               Partitioner
                     |
            +--------+--------+
            |                 |
            v                 v
       Reducer 0          Reducer 1
            |                 |
            +--------+--------+
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

Input: `P1001 rahul #python #hadoop #bigdata`  
Python Mapper produces:
```text
#python    1
#hadoop    1
#bigdata   1
```

---

## 7. Combiner Stage

Instead of sending multiple duplicate tuples like `#python 1` repeatedly across the network, the Combiner performs local aggregation:
```text
#python    3
#bigdata   2
```

---

## 8. Partitioner Stage & Shuffle/Sort

Hadoop's default Partitioner determines which Reducer receives each hashtag based on a hash of the key. Shuffle and sort group the keys:
- `#python  \to [1, 1, 1]`
- `#hadoop  \to [1, 1]`
- `#bigdata \to [1, 1, 1]`
- `#spark   \to [1, 1]`

---

## 9. Reduce Stage

The Reducer aggregates totals and writes to HDFS:
```text
#bigdata    3
#hadoop     2
#python     3
#spark      2
```