# USE CASE 3: HBase Use Case - Customer 360 / Customer Profile

## 1. Business Problem

A telecom company has millions of customers. It needs very fast lookup of a customer's profile attributes:
- Customer ID
- Name
- City
- Mobile number
- Plan
- Status
- Data usage

HBase is suitable because customer information can be retrieved in sub-millisecond latencies using a `Customer ID` as the row key.

---

## 2. Architecture & Flow

```text
Application
    |
    | Customer ID (e.g., CUST1001)
    v
+----------------------+
|        HBase         |
|                      |
| customer_profiles    |
|                      |
| RowKey = CUST1001    |
| RowKey = CUST1002    |
| RowKey = CUST1003    |
+----------------------+
    |
    v
Fast customer lookup
```

---

## 3. Essential HBase Commands

| HBase Command | Purpose |
| :--- | :--- |
| `create` | Create a table |
| `put` | Insert / update data |
| `get` | Read one specific row |
| `scan` | Read multiple rows sequentially |
| `delete` | Delete a specific column value |
| `deleteall` | Delete an entire row |
| `count` | Count total rows in a table |
| `describe` | Display table metadata & column families |
| `disable` | Disable table prior to dropping/altering |
| `drop` | Permanently remove table |

---

## 4. Implementation Example (Shell)

```bash
# Start HBase shell
hbase shell

# 1. Create table with a column family 'personal' and 'account'
create 'customer_profiles', 'personal', 'account'

# 2. Insert customer record (RowKey = CUST1001)
put 'customer_profiles', 'CUST1001', 'personal:name', 'Rahul Sharma'
put 'customer_profiles', 'CUST1001', 'personal:city', 'Hyderabad'
put 'customer_profiles', 'CUST1001', 'account:plan', 'Postpaid-5G'
put 'customer_profiles', 'CUST1001', 'account:status', 'ACTIVE'

# 3. Retrieve customer details quickly
get 'customer_profiles', 'CUST1001'

# 4. Scan all profiles
scan 'customer_profiles'
```