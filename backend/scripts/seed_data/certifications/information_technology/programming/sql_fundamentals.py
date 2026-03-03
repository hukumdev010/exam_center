"""SQL Fundamentals Certification"""

CERTIFICATION = {
    "name": "SQL Fundamentals",
    "description": "Structured Query Language Fundamentals Certification",
    "slug": "sql-fundamentals",
    "level": "Intermediate",
    "duration": 10,
    "questions_count": 120,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does SQL stand for?",
        "explanation": """# SQL - Structured Query Language

**SQL** stands for **Structured Query Language**, a standardized language used to manage and manipulate relational databases.

## Key Features:
- **Data Querying**: Retrieve specific information from databases
- **Data Manipulation**: Insert, update, and delete records
- **Schema Definition**: Create and modify database structures
- **Data Control**: Manage user permissions and access

## Basic Examples:

### 1. Simple Query
```sql
SELECT * FROM users;
-- Retrieves all columns and rows from the users table
```

### 2. Create Table
```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Insert Data
```sql
INSERT INTO products (id, name, price) 
VALUES (1, 'Laptop', 999.99);

-- Multiple records
INSERT INTO products VALUES 
    (2, 'Mouse', 29.99, NOW()),
    (3, 'Keyboard', 79.99, NOW());
```

### 4. Update Data
```sql
UPDATE products 
SET price = 899.99 
WHERE id = 1;
```

### 5. Query with Conditions
```sql
SELECT name, price 
FROM products 
WHERE price > 50 
ORDER BY price DESC;
```""",
        "reference": "https://www.w3schools.com/sql/sql_intro.asp",
        "points": 1,
        "answers": [
            {"text": "Simple Query Language", "is_correct": False},
            {"text": "Structured Query Language", "is_correct": True},
            {"text": "Standard Query Language", "is_correct": False},
            {"text": "System Query Language", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL statement is used to retrieve data from a database?",
        "explanation": """# SELECT Statement - Data Retrieval

**SELECT** is the fundamental SQL statement used to retrieve data from one or more tables in a database.

## Basic Syntax:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column
LIMIT number;
```

## Examples:

### 1. Get All Data
```sql
SELECT * FROM customers;
-- Retrieves all columns and rows from customers table
```

### 2. Select Specific Columns
```sql
SELECT name, email, phone FROM customers;
-- Only retrieves name, email, and phone columns
```

### 3. Select with Conditions
```sql
SELECT * FROM customers 
WHERE age > 25 AND city = 'New York';
-- Filters results based on conditions
```

### 4. Select with Sorting
```sql
SELECT name, email FROM customers 
ORDER BY name ASC, age DESC;
-- Sorts by name (ascending) then age (descending)
```

### 5. Select with Aggregation
```sql
SELECT 
    COUNT(*) as total_customers,
    AVG(age) as average_age,
    MIN(age) as youngest,
    MAX(age) as oldest
FROM customers;
```

### 6. Select Distinct Values
```sql
SELECT DISTINCT city FROM customers;
-- Returns unique city values only
```

### 7. Select with Aliases
```sql
SELECT 
    name AS customer_name,
    email AS contact_email,
    age * 365 AS age_in_days
FROM customers;
```""",
        "reference": "https://www.w3schools.com/sql/sql_select.asp",
        "points": 1,
        "answers": [
            {"text": "GET", "is_correct": False},
            {"text": "SELECT", "is_correct": True},
            {"text": "RETRIEVE", "is_correct": False},
            {"text": "FETCH", "is_correct": False},
        ],
    },
    {
        "text": ("What is the correct syntax to select all columns from "
                 "a table named 'users'?"),
        "explanation": """# Selecting All Columns with Asterisk (*)

**SELECT * FROM table_name** selects all columns from a table. The asterisk (*) is a wildcard that represents all columns.

## Examples:

### 1. Basic Select All
```sql
SELECT * FROM users;
-- Returns all columns and all rows from users table
```

### 2. Qualified Table Name
```sql
SELECT users.* FROM users;
-- Same result, but explicitly specifies the table name
```

### 3. Select All with WHERE Clause
```sql
SELECT * FROM users 
WHERE status = 'active';
-- All columns for active users only
```

### 4. Select All with ORDER BY
```sql
SELECT * FROM users 
ORDER BY created_date DESC;
-- All columns, sorted by creation date (newest first)
```

### 5. Select All vs Specific Columns
```sql
-- All columns (can be slower for large tables)
SELECT * FROM users;

-- Specific columns (better performance)
SELECT id, name, email FROM users;
```

## Best Practices:
- Use SELECT * for quick exploration and development
- Specify column names in production code for better performance
- Be careful with SELECT * on tables with many columns""",
        "reference": "https://www.w3schools.com/sql/sql_select.asp",
        "points": 1,
        "answers": [
            {"text": "SELECT ALL FROM users", "is_correct": False},
            {"text": "SELECT * FROM users", "is_correct": True},
            {"text": "GET * FROM users", "is_correct": False},
            {"text": "SELECT users.*", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL clause is used to filter records?",
        "explanation": """# WHERE Clause - Filtering Records

The **WHERE** clause is used to filter records based on specified conditions. It appears after the FROM clause and before GROUP BY, ORDER BY, or LIMIT clauses.

## Basic Syntax:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

## Comparison Operators:
- `=` Equal to
- `!=` or `<>` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

## Examples:

### 1. Equality Filter
```sql
SELECT * FROM users WHERE age = 25;
-- Returns users exactly 25 years old
```

### 2. Range Filter
```sql
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
-- Returns users aged 20 to 30 (inclusive)

SELECT * FROM products WHERE price > 100 AND price < 500;
-- Alternative range syntax
```

### 3. Pattern Matching
```sql
SELECT * FROM users WHERE name LIKE 'John%';
-- Names starting with 'John'

SELECT * FROM users WHERE email LIKE '%@gmail.com';
-- Gmail addresses

SELECT * FROM users WHERE phone LIKE '___-___-____';
-- Phone numbers with specific format
```

### 4. Multiple Conditions
```sql
SELECT * FROM employees 
WHERE department = 'IT' 
   AND salary > 50000 
   AND hire_date >= '2023-01-01';
```

### 5. OR Conditions
```sql
SELECT * FROM products 
WHERE category = 'Electronics' 
   OR category = 'Computers' 
   OR price < 100;
```

### 6. IN Operator
```sql
SELECT * FROM users 
WHERE city IN ('New York', 'Los Angeles', 'Chicago');
-- More efficient than multiple OR conditions
```

### 7. NULL Values
```sql
SELECT * FROM customers WHERE phone IS NOT NULL;
SELECT * FROM orders WHERE notes IS NULL;
-- Note: Use IS NULL/IS NOT NULL, not = NULL
```

### 8. Complex Conditions
```sql
SELECT * FROM products 
WHERE (category = 'Electronics' AND price > 500) 
   OR (category = 'Books' AND price > 50);
```""",
        "reference": "https://www.w3schools.com/sql/sql_where.asp",
        "points": 1,
        "answers": [
            {"text": "FILTER", "is_correct": False},
            {"text": "WHERE", "is_correct": True},
            {"text": "HAVING", "is_correct": False},
            {"text": "CONDITION", "is_correct": False},
        ],
    },
    {
        "text": "What is the correct SQL statement to insert a new record?",
        "explanation": """# INSERT INTO Statement - Adding New Records

**INSERT INTO** statement is used to insert new records into a table.

## Basic Syntax:
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

## Examples:

### 1. Insert with Specified Columns
```sql
INSERT INTO users (name, age, email)
VALUES ('John Doe', 25, 'john@email.com');
```

### 2. Insert All Columns (in order)
```sql
INSERT INTO users
VALUES (1, 'Jane Smith', 30, 'jane@email.com', NOW());
```

### 3. Insert Multiple Records
```sql
INSERT INTO users (name, age, email) VALUES
    ('Alice Johnson', 28, 'alice@email.com'),
    ('Bob Wilson', 32, 'bob@email.com'),
    ('Carol Brown', 29, 'carol@email.com');
```

### 4. Insert from Another Table
```sql
INSERT INTO active_users (name, email)
SELECT name, email FROM users
WHERE last_login > DATE_SUB(NOW(), INTERVAL 30 DAY);
```

### 5. Insert with Default Values
```sql
INSERT INTO products (name, price)
VALUES ('New Product', 99.99);
-- Other columns will use default values or NULL
```

### 6. Insert with Subquery
```sql
INSERT INTO order_summary (customer_id, total_orders)
SELECT customer_id, COUNT(*)
FROM orders
GROUP BY customer_id;
```""",
        "reference": "https://www.w3schools.com/sql/sql_insert.asp",
        "points": 1,
        "answers": [
            {"text": "ADD INTO", "is_correct": False},
            {"text": "INSERT INTO", "is_correct": True},
            {"text": "CREATE RECORD", "is_correct": False},
            {"text": "NEW RECORD", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL statement is used to update existing records?",
        "explanation": """# UPDATE Statement - Modifying Existing Records

**UPDATE** statement is used to modify existing records in a table. Always use WHERE clause to avoid updating all records accidentally.

## Syntax:
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

## Examples:

### 1. Update Single Column
```sql
UPDATE users SET age = 26 WHERE id = 1;
-- Updates only the age for user with id = 1
```

### 2. Update Multiple Columns
```sql
UPDATE users 
SET age = 27, 
    email = 'newemail@example.com',
    last_updated = NOW()
WHERE name = 'John Doe';
```

### 3. Update with Calculations
```sql
-- Give 10% salary increase to all employees
UPDATE employees 
SET salary = salary * 1.10
WHERE department = 'Engineering';

-- Update product prices based on category
UPDATE products
SET price = CASE
    WHEN category = 'Electronics' THEN price * 1.05
    WHEN category = 'Books' THEN price * 1.02
    ELSE price * 1.03
END;
```

### 4. Update from Another Table (JOIN)
```sql
-- Update customer total orders from orders table
UPDATE customers c
SET total_orders = (
    SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id = c.id
);

-- Using JOIN syntax (MySQL)
UPDATE customers c
INNER JOIN (
    SELECT customer_id, COUNT(*) as order_count
    FROM orders
    GROUP BY customer_id
) o ON c.id = o.customer_id
SET c.total_orders = o.order_count;
```

### 5. Conditional Updates
```sql
-- Update status based on last login
UPDATE users
SET status = CASE
    WHEN last_login < DATE_SUB(NOW(), INTERVAL 90 DAY) THEN 'inactive'
    WHEN last_login < DATE_SUB(NOW(), INTERVAL 30 DAY) THEN 'dormant'
    ELSE 'active'
END;
```

### 6. Update with Subquery
```sql
-- Update employee salaries to department average
UPDATE employees e1
SET salary = (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department = e1.department
    AND e2.id != e1.id
)
WHERE performance_rating = 'Average';
```

### 7. Safety Practices
```sql
-- WRONG: Updates ALL records (dangerous!)
UPDATE users SET status = 'active';

-- CORRECT: Always use WHERE clause
UPDATE users SET status = 'active' WHERE id = 123;

-- Use transactions for multiple updates
BEGIN TRANSACTION;
    UPDATE orders SET status = 'shipped' WHERE id = 1001;
    UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 456;
COMMIT;
```

## ⚠️ **Important Safety Tips:**
- Always use WHERE clause unless updating all records intentionally
- Test with SELECT first: `SELECT * FROM table WHERE condition`
- Use transactions for multiple related updates
- Backup important data before bulk updates
- Consider using LIMIT in MySQL for large updates""",
        "reference": "https://www.w3schools.com/sql/sql_update.asp",
        "points": 1,
        "answers": [
            {"text": "MODIFY", "is_correct": False},
            {"text": "UPDATE", "is_correct": True},
            {"text": "CHANGE", "is_correct": False},
            {"text": "ALTER", "is_correct": False},
        ],
    },
    {
        "text": "What SQL statement is used to delete records from a table?",
        "explanation": """# DELETE Statement - Removing Records

**DELETE FROM** statement removes existing records from a table based on specified conditions.

## Syntax:
```sql
DELETE FROM table_name
WHERE condition;
```

## Examples:

### 1. Delete Specific Records
```sql
-- Delete users under 18
DELETE FROM users WHERE age < 18;

-- Delete inactive accounts
DELETE FROM accounts 
WHERE last_login < DATE_SUB(NOW(), INTERVAL 2 YEAR)
AND status = 'inactive';
```

### 2. Delete Single Record
```sql
DELETE FROM users WHERE id = 123;
-- Deletes exactly one user by primary key
```

### 3. Delete with Multiple Conditions
```sql
-- Delete old, incomplete orders
DELETE FROM orders 
WHERE status = 'pending' 
   AND created_date < DATE_SUB(NOW(), INTERVAL 30 DAY)
   AND total = 0;
```

### 4. Delete with Subquery
```sql
-- Delete users who have never placed orders
DELETE FROM users 
WHERE id NOT IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE customer_id IS NOT NULL
);

-- Delete duplicate records (keep newest)
DELETE u1 FROM users u1
INNER JOIN users u2 
WHERE u1.id > u2.id 
   AND u1.email = u2.email;
```

### 5. Delete with JOIN (MySQL)
```sql
-- Delete orders for inactive customers
DELETE o FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.status = 'inactive';
```

### 6. Delete vs TRUNCATE vs DROP
```sql
-- DELETE: Removes rows, can use WHERE, slower, logged
DELETE FROM products WHERE category = 'discontinued';

-- TRUNCATE: Removes ALL rows, faster, resets identity
TRUNCATE TABLE temp_data;

-- DROP: Removes entire table structure
DROP TABLE old_table;
```

### 7. CASCADE DELETE (Foreign Key)
```sql
-- When deleting a customer, also delete their orders
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(id)
ON DELETE CASCADE;

-- Now deleting customer automatically deletes their orders
DELETE FROM customers WHERE id = 123;
```

### 8. Soft Delete (Recommended Pattern)
```sql
-- Instead of DELETE, mark as deleted
UPDATE users 
SET deleted_at = NOW(), 
    status = 'deleted'
WHERE id = 123;

-- Query for active users only
SELECT * FROM users WHERE deleted_at IS NULL;
```

## ⚠️ **Safety Guidelines:**

### Before Deleting:
```sql
-- 1. Always test with SELECT first
SELECT * FROM users WHERE age < 18;

-- 2. Count records to be deleted
SELECT COUNT(*) FROM users WHERE age < 18;

-- 3. Use transactions for safety
BEGIN TRANSACTION;
    DELETE FROM users WHERE age < 18;
    -- Check results, then COMMIT or ROLLBACK
ROLLBACK;  -- if something goes wrong
```

### Common Mistakes:
```sql
-- DANGER: Deletes ALL records!
DELETE FROM users;  -- Missing WHERE clause

-- SAFE: Delete specific records
DELETE FROM users WHERE status = 'inactive';
```

## Performance Tips:
- Use indexes on WHERE clause columns
- Delete in batches for large datasets
- Consider TRUNCATE for clearing entire tables
- Use soft deletes for auditing purposes""",
        "reference": "https://www.w3schools.com/sql/sql_delete.asp",
        "points": 1,
        "answers": [
            {"text": "REMOVE", "is_correct": False},
            {"text": "DELETE FROM", "is_correct": True},
            {"text": "DROP", "is_correct": False},
            {"text": "CLEAR", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL clause is used to sort the result set?",
        "explanation": """# ORDER BY Clause - Sorting Results

**ORDER BY** clause sorts the result set in ascending (ASC) or descending (DESC) order based on one or more columns.

## Syntax:
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...
```

## Examples:

### 1. Basic Sorting
```sql
-- Sort by age (ascending is default)
SELECT name, age FROM users ORDER BY age;

-- Sort by age descending
SELECT name, age FROM users ORDER BY age DESC;
```

### 2. Multiple Column Sorting
```sql
-- First by department, then by salary (highest first)
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

### 3. Sort by Column Position
```sql
-- Sort by 2nd column (name), then 3rd column (age)
SELECT id, name, age FROM users ORDER BY 2, 3 DESC;
```

### 4. Sort by Expression/Calculation
```sql
-- Sort by calculated field
SELECT 
    name, 
    salary,
    salary * 12 as annual_salary
FROM employees
ORDER BY salary * 12 DESC;

-- Sort by string length
SELECT name FROM products ORDER BY LENGTH(name);
```

### 5. Sort with CASE Statement
```sql
-- Custom sort order
SELECT name, status
FROM orders
ORDER BY 
    CASE status
        WHEN 'urgent' THEN 1
        WHEN 'high' THEN 2
        WHEN 'normal' THEN 3
        WHEN 'low' THEN 4
    END,
    created_date DESC;
```

### 6. Sort with NULL Values
```sql
-- NULLs first (PostgreSQL)
SELECT name, phone FROM customers
ORDER BY phone NULLS FIRST;

-- NULLs last (default in most databases)
SELECT name, phone FROM customers
ORDER BY phone NULLS LAST;

-- Handle NULLs with COALESCE
SELECT name, phone FROM customers
ORDER BY COALESCE(phone, 'ZZZZZZ');  -- NULLs appear last
```

### 7. Random Ordering
```sql
-- Random order (different syntax per database)
SELECT * FROM products ORDER BY RANDOM();     -- PostgreSQL
SELECT * FROM products ORDER BY RAND();       -- MySQL
SELECT * FROM products ORDER BY NEWID();      -- SQL Server
```

### 8. Sorting with JOINs
```sql
-- Sort by related table column
SELECT 
    o.order_id,
    c.name,
    o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id
ORDER BY c.name, o.order_date DESC;
```

### 9. Performance Optimization
```sql
-- Create index for frequently sorted columns
CREATE INDEX idx_employees_dept_salary 
ON employees(department, salary DESC);

-- Query benefits from the index
SELECT * FROM employees 
ORDER BY department, salary DESC;
```

### 10. Pagination with ORDER BY
```sql
-- Always use ORDER BY with LIMIT/OFFSET
SELECT * FROM products
ORDER BY created_date DESC
LIMIT 10 OFFSET 20;  -- Page 3 (rows 21-30)
```

## Important Notes:

### ⚠️ **ORDER BY Performance:**
- Sorting large result sets is expensive
- Use indexes on ORDER BY columns
- Avoid sorting by expressions when possible
- Consider pagination for large datasets

### 📝 **Best Practices:**
- Always specify ASC or DESC explicitly for clarity
- Use column names instead of positions for maintainability
- Be careful with NULL handling across different databases
- Use ORDER BY with LIMIT/OFFSET for pagination
- Consider the impact on query performance

### 🔍 **Common Patterns:**
```sql
-- Latest records first
ORDER BY created_date DESC;

-- Alphabetical sorting
ORDER BY name ASC;

-- Priority-based sorting
ORDER BY priority DESC, created_date ASC;

-- Business logic sorting (VIP customers first)
ORDER BY 
    CASE WHEN customer_tier = 'VIP' THEN 1 ELSE 2 END,
    name ASC;
```""",
        "reference": "https://www.w3schools.com/sql/sql_orderby.asp",
        "points": 1,
        "answers": [
            {"text": "SORT BY", "is_correct": False},
            {"text": "ORDER BY", "is_correct": True},
            {"text": "ARRANGE BY", "is_correct": False},
            {"text": "GROUP BY", "is_correct": False},
        ],
    },
    {
        "text": "What does the DISTINCT keyword do in SQL?",
        "explanation": """# DISTINCT Keyword - Eliminating Duplicates

**DISTINCT** returns only unique values, eliminating duplicates from results.

## Examples:

### 1. Unique Cities
```sql
SELECT DISTINCT city FROM customers;
-- Returns each city only once
```

### 2. Unique Combinations  
```sql
SELECT DISTINCT city, country FROM customers;
-- Returns unique city-country pairs
```

### 3. Count Unique Values
```sql
SELECT COUNT(DISTINCT city) AS unique_cities FROM customers;
-- Counts different cities
```

### 4. With Filtering
```sql
SELECT DISTINCT department
FROM employees
WHERE salary > 50000;
```""",
        "reference": "https://www.w3schools.com/sql/sql_distinct.asp",
        "points": 1,
        "answers": [
            {"text": "Sorts the data", "is_correct": False},
            {"text": "Returns only unique values", "is_correct": True},
            {"text": "Filters null values", "is_correct": False},
            {"text": "Counts records", "is_correct": False},
        ],
    },
    {
        "text": ("Which operator is used to search for a specified "
                 "pattern in a column?"),
        "explanation": """# LIKE Operator - Pattern Matching

**LIKE** operator is used with WHERE clause to search for patterns in text columns using wildcards.

## Wildcards:
- **%** - Zero or more characters
- **_** - Exactly one character

## Examples:

### 1. Names Starting with Specific Letter
```sql
-- Names starting with 'A'
SELECT * FROM customers WHERE name LIKE 'A%';
-- Returns: Alice, Andrew, Anthony

-- Names starting with 'Jo'
SELECT * FROM employees WHERE name LIKE 'Jo%';
-- Returns: John, Joseph, Joan
```

### 2. Names Ending with Pattern
```sql
-- Names ending with 'son'
SELECT * FROM users WHERE last_name LIKE '%son';
-- Returns: Johnson, Anderson, Wilson

-- Email addresses ending with specific domain
SELECT * FROM customers WHERE email LIKE '%@gmail.com';
-- Returns all Gmail users
```

### 3. Names Containing Pattern
```sql
-- Names containing 'ar'
SELECT * FROM users WHERE name LIKE '%ar%';
-- Returns: Mary, Charles, Margaret

-- Products containing 'phone'
SELECT * FROM products WHERE name LIKE '%phone%';
-- Returns: iPhone, Smartphone, Headphone
```

### 4. Exact Length Patterns
```sql
-- Names with exactly 5 characters
SELECT * FROM users WHERE name LIKE '_____';
-- Returns: Smith, Jones, Brown (5 chars each)

-- Product codes: ABC followed by 3 digits
SELECT * FROM products WHERE code LIKE 'ABC___';
-- Returns: ABC123, ABC456, ABC789
```

### 5. Complex Patterns
```sql
-- Phone numbers format: (xxx) xxx-xxxx
SELECT * FROM customers 
WHERE phone LIKE '(___) ___-____';

-- Second character is 'a'
SELECT * FROM words WHERE word LIKE '_a%';
-- Returns: cat, bat, car, etc.
```

### 6. Case Sensitivity
```sql
-- Case insensitive search (depends on database)
SELECT * FROM users WHERE name LIKE 'john%';  -- john, John, JOHN

-- Explicit case handling
SELECT * FROM users WHERE UPPER(name) LIKE 'JOHN%';
```

### 7. Escaping Special Characters
```sql
-- Search for literal % or _ characters
SELECT * FROM products 
WHERE description LIKE '%50\% off%' ESCAPE '\';

-- Find products with underscores in name
SELECT * FROM products 
WHERE name LIKE '%\_special%' ESCAPE '\';
```""",
        "reference": "https://www.w3schools.com/sql/sql_like.asp",
        "points": 1,
        "answers": [
            {"text": "MATCH", "is_correct": False},
            {"text": "LIKE", "is_correct": True},
            {"text": "CONTAINS", "is_correct": False},
            {"text": "SEARCH", "is_correct": False},
        ],
    },
    {
        "text": "What wildcard character represents zero or more characters in SQL?",
        "explanation": """# Percent (%) Wildcard

The **%** (percent) wildcard represents zero or more characters in SQL LIKE patterns.

## Examples:
```sql
-- Names starting with 'A'
SELECT * FROM customers WHERE name LIKE 'A%';

-- Names ending with 'son'  
SELECT * FROM customers WHERE name LIKE '%son';

-- Names containing 'ar'
SELECT * FROM customers WHERE name LIKE '%ar%';

-- Empty string matches too
SELECT * FROM products WHERE description LIKE '%';
```""",
        "reference": "https://www.w3schools.com/sql/sql_wildcards.asp",
        "points": 1,
        "answers": [
            {"text": "*", "is_correct": False},
            {"text": "%", "is_correct": True},
            {"text": "_", "is_correct": False},
            {"text": "?", "is_correct": False},
        ],
    },
    {
        "text": "Which wildcard character represents exactly one character in SQL?",
        "explanation": """# Underscore (_) Wildcard

The **_** (underscore) wildcard represents exactly one character in SQL LIKE patterns.

## Examples:
```sql
-- Phone numbers: (XXX) XXX-XXXX
SELECT * FROM customers 
WHERE phone LIKE '(___) ___-____';

-- Product codes: ABC123
SELECT * FROM products 
WHERE code LIKE 'ABC___';

-- Names with exactly 4 letters
SELECT * FROM users WHERE name LIKE '____';

-- Second character is 'a'
SELECT * FROM words WHERE word LIKE '_a%';
```""",
        "reference": "https://www.w3schools.com/sql/sql_wildcards.asp",
        "points": 1,
        "answers": [
            {"text": "%", "is_correct": False},
            {"text": "_", "is_correct": True},
            {"text": "?", "is_correct": False},
            {"text": "*", "is_correct": False},
        ],
    },
    {
        "text": ("What SQL operator is used to check if a value is "
                 "within a range?"),
        "explanation": """# BETWEEN Operator - Range Filtering

**BETWEEN** operator filters results within a specified range of values (inclusive of both boundary values).

## Syntax:
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

## Examples:

### 1. Numeric Range Filtering
```sql
-- Ages between 18 and 65 (inclusive)
SELECT name, age FROM employees 
WHERE age BETWEEN 18 AND 65;

-- Salaries in mid-range
SELECT name, salary FROM employees
WHERE salary BETWEEN 40000 AND 80000;

-- Product prices
SELECT name, price FROM products
WHERE price BETWEEN 10.00 AND 50.00;
```

### 2. Date Range Filtering
```sql
-- Orders from specific year
SELECT * FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

-- Recent orders (last 30 days)
SELECT * FROM orders
WHERE order_date BETWEEN 
    DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW();

-- Q1 sales data
SELECT * FROM sales
WHERE sale_date BETWEEN '2024-01-01' AND '2024-03-31';
```

### 3. Alphabetical Range
```sql
-- Names starting with A through M
SELECT * FROM customers
WHERE last_name BETWEEN 'A' AND 'N';  -- 'N' not included

-- Product codes in specific range
SELECT * FROM products
WHERE product_code BETWEEN 'ABC001' AND 'ABC999';
```

### 4. NOT BETWEEN (Exclusion)
```sql
-- Exclude mid-range prices
SELECT name, price FROM products
WHERE price NOT BETWEEN 100 AND 500;
-- Returns items under $100 OR over $500

-- Exclude working hours
SELECT * FROM events
WHERE event_time NOT BETWEEN '09:00:00' AND '17:00:00';
```

### 5. BETWEEN vs Comparison Operators
```sql
-- These queries are equivalent:

-- Using BETWEEN
SELECT * FROM products WHERE price BETWEEN 10 AND 50;

-- Using comparison operators  
SELECT * FROM products WHERE price >= 10 AND price <= 50;
```

### 6. Time Range Queries
```sql
-- Orders during business hours
SELECT * FROM orders
WHERE TIME(order_timestamp) BETWEEN '09:00:00' AND '18:00:00';

-- Weekend sales
SELECT * FROM sales
WHERE DAYOFWEEK(sale_date) BETWEEN 1 AND 2;  -- Sunday and Monday
```

### 7. Performance Tips
```sql
-- Create indexes for range queries
CREATE INDEX idx_employees_age ON employees(age);
CREATE INDEX idx_orders_date ON orders(order_date);

-- Range queries benefit from these indexes
SELECT * FROM employees WHERE age BETWEEN 25 AND 35;
SELECT * FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';
```

## Important Notes:
- BETWEEN is **inclusive** of both boundary values
- Value1 should be less than Value2 for proper results
- Works with numbers, dates, and strings
- Can be combined with other WHERE conditions using AND/OR""",
        "reference": "https://www.w3schools.com/sql/sql_between.asp",
        "points": 1,
        "answers": [
            {"text": "RANGE", "is_correct": False},
            {"text": "BETWEEN", "is_correct": True},
            {"text": "WITHIN", "is_correct": False},
            {"text": "IN RANGE", "is_correct": False},
        ],
    },
    {
        "text": ("Which operator is used to specify multiple possible "
                 "values for a column?"),
        "explanation": """# IN Operator - Multiple Value Matching

**IN** operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions.

## Syntax:
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, value3, ...);
```

## Examples:

### 1. Multiple Specific Values
```sql
-- Cities filter
SELECT * FROM customers 
WHERE city IN ('New York', 'Los Angeles', 'Chicago');

-- Equivalent to:
SELECT * FROM customers 
WHERE city = 'New York' 
   OR city = 'Los Angeles' 
   OR city = 'Chicago';
```

### 2. Numeric Values
```sql
-- Specific employee IDs
SELECT name, department FROM employees
WHERE employee_id IN (101, 102, 105, 110);

-- Product categories
SELECT * FROM products
WHERE category_id IN (1, 3, 5, 7);
```

### 3. NOT IN (Exclusion)
```sql
-- Exclude specific ages
SELECT name, age FROM users 
WHERE age NOT IN (18, 65, 99);

-- Exclude certain departments
SELECT * FROM employees
WHERE department NOT IN ('HR', 'Legal', 'Admin');
```

### 4. IN with Subquery
```sql
-- Customers who have placed orders
SELECT * FROM customers
WHERE customer_id IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE order_date >= '2024-01-01'
);

-- Products that have been sold
SELECT * FROM products
WHERE product_id IN (
    SELECT product_id 
    FROM order_items 
    WHERE quantity > 0
);
```

### 5. Complex Subquery Examples
```sql
-- High-value customers
SELECT name, email FROM customers
WHERE customer_id IN (
    SELECT customer_id 
    FROM orders 
    GROUP BY customer_id 
    HAVING SUM(total) > 5000
);

-- Employees in top-performing departments
SELECT name, salary FROM employees
WHERE department IN (
    SELECT department 
    FROM (
        SELECT department, AVG(sales) as avg_sales
        FROM sales_data 
        GROUP BY department
        ORDER BY avg_sales DESC
        LIMIT 3
    ) top_depts
);
```

### 6. Performance Comparisons
```sql
-- IN vs Multiple OR (IN is usually faster)
-- Using IN (preferred)
SELECT * FROM orders 
WHERE status IN ('shipped', 'delivered', 'completed');

-- Using OR (less efficient)
SELECT * FROM orders 
WHERE status = 'shipped' 
   OR status = 'delivered' 
   OR status = 'completed';
```

### 7. String Values with IN
```sql
-- Multiple string matches
SELECT * FROM employees
WHERE job_title IN (
    'Software Engineer', 
    'Senior Developer', 
    'Tech Lead',
    'Principal Engineer'
);

-- Country filtering
SELECT customer_name, country FROM customers
WHERE country IN ('USA', 'Canada', 'Mexico');
```

### 8. Common Patterns
```sql
-- Active status filtering
SELECT * FROM users
WHERE status IN ('active', 'premium', 'verified');

-- Date-based filtering (quarters)
SELECT * FROM sales
WHERE QUARTER(sale_date) IN (1, 2);  -- Q1 and Q2

-- Weekend days
SELECT * FROM events
WHERE DAYOFWEEK(event_date) IN (1, 7);  -- Sunday and Saturday
```

## Performance Tips:
- **IN** is generally faster than multiple OR conditions
- Use indexes on columns frequently used with IN
- Consider EXISTS instead of IN for better performance with large subqueries
- NOT IN with NULL values can produce unexpected results

## Best Practices:
- Use IN for small, static lists of values
- Use EXISTS for dynamic subquery results
- Be careful with NOT IN when columns might contain NULL values""",
        "reference": "https://www.w3schools.com/sql/sql_in.asp",
        "points": 1,
        "answers": [
            {"text": "OR", "is_correct": False},
            {"text": "IN", "is_correct": True},
            {"text": "ANY", "is_correct": False},
            {"text": "MULTIPLE", "is_correct": False},
        ],
    },
    {
        "text": "What does NULL represent in SQL?",
        "explanation": """# NULL Values in SQL

**NULL** represents a missing or unknown value in SQL. It's **not** zero, empty string, or false.

## Key Points:
- NULL means "no value" or "unknown value"
- NULL ≠ 0 (zero)
- NULL ≠ '' (empty string)
- NULL ≠ FALSE

## Examples:

### 1. Find NULL Values
```sql
SELECT * FROM users WHERE phone IS NULL;
-- Returns users without phone numbers
```

### 2. Find Non-NULL Values
```sql
SELECT * FROM users WHERE phone IS NOT NULL;
-- Returns users with phone numbers
```

### 3. Handle NULL in Calculations
```sql
SELECT 
    name,
    COALESCE(phone, email, 'No contact') AS contact,
    salary * COALESCE(bonus_rate, 0) AS bonus
FROM employees;
```

### 4. NULL in Comparisons (WRONG vs CORRECT)
```sql
-- WRONG: This returns no results!
SELECT * FROM products WHERE price = NULL;

-- CORRECT: Use IS NULL
SELECT * FROM products WHERE price IS NULL;
```

### 5. NULL with Aggregate Functions
```sql
-- COUNT(*) includes NULLs, COUNT(column) excludes NULLs
SELECT 
    COUNT(*) AS total_rows,
    COUNT(phone) AS rows_with_phone,
    COUNT(*) - COUNT(phone) AS rows_without_phone
FROM customers;
```

### 6. CASE with NULL
```sql
SELECT 
    name,
    CASE 
        WHEN phone IS NOT NULL THEN 'Has phone'
        WHEN email IS NOT NULL THEN 'Has email'  
        ELSE 'No contact info'
    END AS contact_status
FROM customers;
```""",
        "reference": "https://www.w3schools.com/sql/sql_null_values.asp",
        "points": 1,
        "answers": [
            {"text": "Zero value", "is_correct": False},
            {"text": "Missing or unknown value", "is_correct": True},
            {"text": "Empty string", "is_correct": False},
            {"text": "Default value", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used to test for NULL values?",
        "explanation": """# Testing for NULL Values

**IS NULL** and **IS NOT NULL** are the correct operators for testing NULL values. You **cannot** use = NULL or != NULL.

## Why = NULL Doesn't Work:
NULL represents "unknown" value, so any comparison with NULL returns NULL (which is falsy), not true or false.

## Examples:

### 1. Find NULL Values
```sql
-- Find customers without phone numbers
SELECT name, email FROM customers 
WHERE phone IS NULL;

-- Find orders without delivery dates
SELECT order_id, customer_id FROM orders
WHERE delivery_date IS NULL;
```

### 2. Find Non-NULL Values
```sql
-- Find users with email addresses
SELECT name, email FROM users 
WHERE email IS NOT NULL;

-- Find products with descriptions
SELECT name, price FROM products
WHERE description IS NOT NULL;
```

### 3. Common Mistakes vs Correct Usage
```sql
-- WRONG: This returns no results!
SELECT * FROM customers WHERE phone = NULL;

-- CORRECT: Use IS NULL
SELECT * FROM customers WHERE phone IS NULL;

-- WRONG: This also fails
SELECT * FROM customers WHERE phone != NULL;

-- CORRECT: Use IS NOT NULL
SELECT * FROM customers WHERE phone IS NOT NULL;
```

### 4. NULL in Calculations
```sql
-- NULL in arithmetic results in NULL
SELECT 
    product_name,
    price,
    price * discount_rate as discounted_price,  -- NULL if discount_rate is NULL
    price * COALESCE(discount_rate, 0) as safe_discount  -- Handle NULL
FROM products;
```

### 5. Filtering with NULL Considerations
```sql
-- Find incomplete customer records
SELECT * FROM customers
WHERE phone IS NULL 
   OR email IS NULL 
   OR address IS NULL;

-- Complete customer records only
SELECT * FROM customers
WHERE phone IS NOT NULL 
  AND email IS NOT NULL 
  AND address IS NOT NULL;
```

### 6. NULL with Aggregate Functions
```sql
-- COUNT(*) includes NULLs, COUNT(column) excludes NULLs
SELECT 
    COUNT(*) as total_customers,
    COUNT(phone) as customers_with_phone,
    COUNT(email) as customers_with_email
FROM customers;
```

### 7. Handling NULL in ORDER BY
```sql
-- NULLs appear last by default (MySQL)
SELECT name, phone FROM customers 
ORDER BY phone;

-- Force NULLs first
SELECT name, phone FROM customers 
ORDER BY phone IS NULL DESC, phone;

-- Replace NULLs for sorting
SELECT name, phone FROM customers 
ORDER BY COALESCE(phone, 'ZZZZZZZ');
```

### 8. CASE Statement with NULL
```sql
SELECT 
    name,
    CASE 
        WHEN phone IS NOT NULL THEN 'Has phone'
        WHEN email IS NOT NULL THEN 'Has email only'
        ELSE 'No contact info'
    END as contact_status
FROM customers;
```

### 9. NULL-Safe Comparisons (MySQL)
```sql
-- MySQL NULL-safe equality operator
SELECT * FROM users 
WHERE manager_id <=> NULL;  -- Same as IS NULL

-- Compare two columns that might be NULL
SELECT * FROM employees
WHERE manager_id <=> supervisor_id;
```

## Key Points:
- Always use **IS NULL** / **IS NOT NULL** for NULL tests
- **= NULL** and **!= NULL** don't work as expected
- NULL in calculations produces NULL results
- Aggregate functions handle NULL differently
- Consider NULL behavior when designing queries""",
        "reference": "https://www.w3schools.com/sql/sql_null_values.asp",
        "points": 1,
        "answers": [
            {"text": "= NULL", "is_correct": False},
            {"text": "IS NULL", "is_correct": True},
            {"text": "== NULL", "is_correct": False},
            {"text": "EQUALS NULL", "is_correct": False},
        ],
    },
    {
        "text": "What SQL function is used to return the number of records?",
        "explanation": """# COUNT() Function - Counting Records

**COUNT()** function returns the number of rows that match specified criteria.

## Variations:
- `COUNT(*)` - Counts all rows (including NULLs)
- `COUNT(column)` - Counts non-NULL values in column
- `COUNT(DISTINCT column)` - Counts unique non-NULL values

## Examples:

### 1. Count All Rows
```sql
SELECT COUNT(*) AS total_users FROM users;
-- Returns total number of users
```

### 2. Count Non-NULL Values
```sql
SELECT 
    COUNT(*) AS total_users,
    COUNT(email) AS users_with_email,
    COUNT(phone) AS users_with_phone
FROM users;
```

### 3. Count with Conditions
```sql
SELECT COUNT(*) AS adults FROM users WHERE age >= 18;

SELECT COUNT(*) AS active_users 
FROM users 
WHERE status = 'active' AND last_login > NOW() - INTERVAL 30 DAY;
```

### 4. Count Distinct Values
```sql
SELECT 
    COUNT(DISTINCT city) AS unique_cities,
    COUNT(DISTINCT country) AS unique_countries
FROM customers;
```

### 5. Count by Group
```sql
SELECT 
    department,
    COUNT(*) AS employee_count,
    COUNT(CASE WHEN salary > 50000 THEN 1 END) AS high_earners
FROM employees
GROUP BY department;
```

### 6. Conditional Counting
```sql
SELECT 
    COUNT(CASE WHEN age < 30 THEN 1 END) AS young_employees,
    COUNT(CASE WHEN age BETWEEN 30 AND 50 THEN 1 END) AS mid_age,
    COUNT(CASE WHEN age > 50 THEN 1 END) AS senior_employees
FROM employees;
```""",
        "reference": "https://www.w3schools.com/sql/sql_count_avg_sum.asp",
        "points": 1,
        "answers": [
            {"text": "NUMBER()", "is_correct": False},
            {"text": "COUNT()", "is_correct": True},
            {"text": "SIZE()", "is_correct": False},
            {"text": "LENGTH()", "is_correct": False},
        ],
    },
    {
        "text": ("Which function returns the average value of a "
                 "numeric column?"),
        "explanation": """# AVG() Function - Calculating Averages

**AVG()** function calculates the arithmetic mean (average) of a numeric column, automatically ignoring NULL values.

## Syntax:
```sql
AVG([DISTINCT] column_name)
```

## Examples:

### 1. Simple Average
```sql
-- Average age of all users
SELECT AVG(age) as average_age FROM users;

-- Average with rounding
SELECT ROUND(AVG(age), 2) as average_age FROM users;
```

### 2. Average by Group
```sql
-- Average salary by department
SELECT 
    department,
    AVG(salary) as avg_salary,
    COUNT(*) as employee_count
FROM employees 
GROUP BY department
ORDER BY avg_salary DESC;
```

### 3. Conditional Averages
```sql
-- Average price for electronics only
SELECT AVG(price) as avg_electronics_price
FROM products
WHERE category = 'Electronics';

-- Average using CASE for conditional calculation
SELECT 
    AVG(CASE WHEN age < 30 THEN salary END) as avg_young_salary,
    AVG(CASE WHEN age >= 30 THEN salary END) as avg_senior_salary
FROM employees;
```

### 4. Average with DISTINCT
```sql
-- Average of unique salaries (removes duplicates first)
SELECT AVG(DISTINCT salary) FROM employees;

-- Compare regular vs distinct average
SELECT 
    AVG(salary) as regular_avg,
    AVG(DISTINCT salary) as distinct_avg,
    COUNT(salary) as total_count,
    COUNT(DISTINCT salary) as unique_count
FROM employees;
```

### 5. Moving Average (Window Function)
```sql
-- 3-month moving average of sales
SELECT 
    month,
    sales,
    AVG(sales) OVER (
        ORDER BY month 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3month
FROM monthly_sales
ORDER BY month;
```

### 6. Average with JOINs
```sql
-- Average order value per customer
SELECT 
    c.name,
    COUNT(o.id) as order_count,
    AVG(o.total) as avg_order_value,
    SUM(o.total) as total_spent
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
HAVING COUNT(o.id) > 0;
```

### 7. Comparing to Average (Subqueries)
```sql
-- Employees earning above company average
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Products priced above category average
SELECT p1.name, p1.price, p1.category
FROM products p1
WHERE p1.price > (
    SELECT AVG(p2.price)
    FROM products p2
    WHERE p2.category = p1.category
);
```

### 8. Average with Date Functions
```sql
-- Average daily sales by month
SELECT 
    YEAR(order_date) as year,
    MONTH(order_date) as month,
    AVG(daily_total) as avg_daily_sales
FROM (
    SELECT 
        order_date,
        SUM(total) as daily_total
    FROM orders
    GROUP BY order_date
) daily_sales
GROUP BY YEAR(order_date), MONTH(order_date);
```

### 9. Weighted Average
```sql
-- Weighted average grade (grade * credits)
SELECT 
    student_id,
    SUM(grade * credits) / SUM(credits) as weighted_gpa
FROM student_grades
GROUP BY student_id;
```

### 10. NULL Handling
```sql
-- AVG ignores NULLs automatically
SELECT 
    AVG(salary) as avg_with_nulls,
    AVG(COALESCE(salary, 0)) as avg_treating_null_as_zero,
    COUNT(*) as total_rows,
    COUNT(salary) as non_null_salaries
FROM employees;
```

## Advanced Patterns:

### Performance Optimization
```sql
-- Index for GROUP BY columns
CREATE INDEX idx_employees_dept ON employees(department);

-- Efficient average calculation
SELECT department, AVG(salary)
FROM employees
WHERE department IN ('Engineering', 'Sales', 'Marketing')
GROUP BY department;
```

### Statistical Analysis
```sql
-- Comprehensive statistics
SELECT 
    department,
    COUNT(*) as count,
    AVG(salary) as mean_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary,
    STDDEV(salary) as std_deviation,
    VARIANCE(salary) as variance
FROM employees
GROUP BY department;
```

### Business Intelligence Queries
```sql
-- Monthly performance comparison
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') as month,
    AVG(total) as avg_order_value,
    AVG(total) - LAG(AVG(total)) OVER (ORDER BY DATE_FORMAT(order_date, '%Y-%m')) as month_over_month_change
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
```

## Important Notes:

### 🔍 **Key Behaviors:**
- NULL values are automatically excluded
- Returns NULL if no non-NULL values exist
- Result is always decimal/float, even for integer columns
- DISTINCT removes duplicates before calculation

### 📊 **Common Use Cases:**
- Performance metrics (average response time, sales)
- Academic grading (GPA calculations)
- Financial analysis (average revenue, costs)
- Quality metrics (average rating, score)""",
        "reference": "https://www.w3schools.com/sql/sql_count_avg_sum.asp",
        "points": 1,
        "answers": [
            {"text": "MEAN()", "is_correct": False},
            {"text": "AVG()", "is_correct": True},
            {"text": "AVERAGE()", "is_correct": False},
            {"text": "MEDIAN()", "is_correct": False},
        ],
    },
    {
        "text": "What function returns the sum of a numeric column?",
        "explanation": """# SUM() Function - Calculating Totals

**SUM()** function calculates the total sum of all values in a numeric column, automatically ignoring NULL values.

## Syntax:
```sql
SUM([DISTINCT] column_name)
```

## Examples:

### 1. Basic Sum Calculation
```sql
-- Total sales revenue
SELECT SUM(amount) as total_revenue FROM sales;

-- Total inventory value
SELECT SUM(price * quantity) as total_inventory_value 
FROM products;
```

### 2. Sum by Groups
```sql
-- Revenue by department
SELECT 
    department,
    SUM(salary) as total_department_salary,
    COUNT(*) as employee_count,
    AVG(salary) as average_salary
FROM employees 
GROUP BY department;

-- Sales by product category
SELECT 
    category,
    SUM(quantity_sold) as total_units,
    SUM(quantity_sold * price) as total_revenue
FROM product_sales 
GROUP BY category
ORDER BY total_revenue DESC;
```

### 3. Conditional Sums
```sql
-- Sum with WHERE clause
SELECT SUM(salary) as engineering_payroll
FROM employees
WHERE department = 'Engineering';

-- Sum for specific date range
SELECT SUM(order_total) as q1_revenue
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';
```

### 4. Sum with CASE (Conditional Aggregation)
```sql
-- Sum different types of transactions
SELECT 
    SUM(CASE WHEN transaction_type = 'sale' THEN amount ELSE 0 END) as total_sales,
    SUM(CASE WHEN transaction_type = 'refund' THEN amount ELSE 0 END) as total_refunds,
    SUM(amount) as net_total
FROM transactions;

-- Sum by status
SELECT 
    SUM(CASE WHEN status = 'completed' THEN total END) as completed_orders,
    SUM(CASE WHEN status = 'pending' THEN total END) as pending_orders,
    SUM(CASE WHEN status = 'cancelled' THEN total END) as cancelled_orders
FROM orders;
```

### 5. Sum with DISTINCT
```sql
-- Sum unique salaries (removes duplicates first)
SELECT SUM(DISTINCT salary) FROM employees;

-- Compare regular vs distinct sum
SELECT 
    SUM(salary) as total_payroll,
    SUM(DISTINCT salary) as sum_unique_salaries,
    COUNT(salary) as total_employees,
    COUNT(DISTINCT salary) as unique_salary_levels
FROM employees;
```

### 6. Running Sum (Window Function)
```sql
-- Cumulative sales by date
SELECT 
    sale_date,
    daily_sales,
    SUM(daily_sales) OVER (
        ORDER BY sale_date 
        ROWS UNBOUNDED PRECEDING
    ) as running_total
FROM (
    SELECT 
        sale_date,
        SUM(amount) as daily_sales
    FROM sales
    GROUP BY sale_date
) daily_totals
ORDER BY sale_date;
```

### 7. Sum with JOINs
```sql
-- Customer total purchases
SELECT 
    c.customer_name,
    c.customer_id,
    COUNT(o.order_id) as total_orders,
    SUM(o.order_total) as lifetime_value
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.order_total) > 1000
ORDER BY lifetime_value DESC;
```

### 8. Complex Calculations
```sql
-- Profit calculation
SELECT 
    product_category,
    SUM(quantity * selling_price) as total_revenue,
    SUM(quantity * cost_price) as total_cost,
    SUM(quantity * (selling_price - cost_price)) as total_profit,
    ROUND(
        SUM(quantity * (selling_price - cost_price)) / 
        SUM(quantity * selling_price) * 100, 2
    ) as profit_margin_percent
FROM product_sales
GROUP BY product_category;
```

### 9. Sum with Subqueries
```sql
-- Compare department totals to company average
SELECT 
    department,
    SUM(salary) as dept_total,
    (SELECT SUM(salary) FROM employees) as company_total,
    ROUND(
        SUM(salary) * 100.0 / (SELECT SUM(salary) FROM employees), 2
    ) as percent_of_total
FROM employees
GROUP BY department;
```

### 10. NULL Handling
```sql
-- SUM ignores NULLs automatically
SELECT 
    SUM(bonus) as total_bonus,              -- Ignores NULL bonuses
    SUM(COALESCE(bonus, 0)) as total_with_zeros,  -- Treats NULL as 0
    COUNT(*) as total_employees,
    COUNT(bonus) as employees_with_bonus
FROM employees;
```

### 11. Performance Optimization
```sql
-- Index for GROUP BY columns
CREATE INDEX idx_sales_category_date ON sales(category, sale_date);

-- Efficient sum query
SELECT 
    category, 
    SUM(amount) 
FROM sales 
WHERE sale_date >= '2024-01-01'
GROUP BY category;
```

## Key Points:
- **SUM()** only works with numeric data types
- **NULL values are automatically ignored**
- Use **COALESCE()** if you want to treat NULL as 0
- **SUM()** returns NULL if no rows match or all values are NULL
- Combine with **GROUP BY** for category totals
- Use **window functions** for running totals""",
        "reference": "https://www.w3schools.com/sql/sql_count_avg_sum.asp",
        "points": 1,
        "answers": [
            {"text": "TOTAL()", "is_correct": False},
            {"text": "SUM()", "is_correct": True},
            {"text": "ADD()", "is_correct": False},
            {"text": "PLUS()", "is_correct": False},
        ],
    },
    {
        "text": "Which function returns the smallest value in a column?",
        "explanation": """# MIN() Function - Finding Minimum Values

**MIN()** function returns the smallest value in a column, working with numeric, date, and text data.

## Examples:

### 1. Numeric Minimums
```sql
-- Youngest employee age
SELECT MIN(age) as youngest_age FROM employees;

-- Lowest salary
SELECT MIN(salary) as minimum_salary FROM employees;

-- Cheapest product price
SELECT MIN(price) as lowest_price FROM products;
```

### 2. Date Minimums
```sql
-- Earliest order date
SELECT MIN(order_date) as first_order FROM orders;

-- Oldest employee hire date
SELECT MIN(hire_date) as earliest_hire FROM employees;
```

### 3. MIN by Groups
```sql
-- Lowest price by category
SELECT 
    category,
    MIN(price) as cheapest_item,
    MAX(price) as most_expensive,
    AVG(price) as average_price
FROM products 
GROUP BY category;
```

### 4. MIN with Text Data
```sql
-- Alphabetically first name
SELECT MIN(last_name) as first_alphabetically FROM employees;

-- Earliest product code
SELECT MIN(product_code) FROM products;
```

### 5. MIN with Conditions
```sql
-- Minimum salary in IT department
SELECT MIN(salary) FROM employees 
WHERE department = 'IT';

-- Cheapest available product
SELECT MIN(price) FROM products 
WHERE in_stock = 1;
```""",
        "reference": "https://www.w3schools.com/sql/sql_min_max.asp",
        "points": 1,
        "answers": [
            {"text": "SMALLEST()", "is_correct": False},
            {"text": "MIN()", "is_correct": True},
            {"text": "LOWEST()", "is_correct": False},
            {"text": "BOTTOM()", "is_correct": False},
        ],
    },
    {
        "text": "What function returns the largest value in a column?",
        "explanation": """# MAX() Function - Finding Maximum Values

**MAX()** function returns the largest value in a column, working with numeric, date, and text data.

## Examples:

### 1. Numeric Maximums
```sql
-- Highest salary
SELECT MAX(salary) as highest_salary FROM employees;

-- Most expensive product
SELECT MAX(price) as most_expensive FROM products;

-- Oldest employee age
SELECT MAX(age) as oldest_employee FROM employees;
```

### 2. Date Maximums
```sql
-- Latest order date
SELECT MAX(order_date) as most_recent_order FROM orders;

-- Most recent hire
SELECT MAX(hire_date) as latest_hire FROM employees;
```

### 3. MAX by Groups
```sql
-- Most expensive product by category
SELECT 
    category,
    MAX(price) as highest_price,
    MIN(price) as lowest_price,
    COUNT(*) as product_count
FROM products 
GROUP BY category;
```

### 4. MAX with Text Data
```sql
-- Alphabetically last name
SELECT MAX(last_name) as last_alphabetically FROM employees;

-- Latest product code
SELECT MAX(product_code) FROM products;
```

### 5. Finding Records with MAX Values
```sql
-- Employee with highest salary
SELECT name, salary FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Most recent order details
SELECT * FROM orders
WHERE order_date = (SELECT MAX(order_date) FROM orders);
```""",
        "reference": "https://www.w3schools.com/sql/sql_min_max.asp",
        "points": 1,
        "answers": [
            {"text": "LARGEST()", "is_correct": False},
            {"text": "MAX()", "is_correct": True},
            {"text": "HIGHEST()", "is_correct": False},
            {"text": "TOP()", "is_correct": False},
        ],
    },
    {
        "text": "What clause is used with aggregate functions to group rows?",
        "explanation": """# GROUP BY Clause - Grouping Data

**GROUP BY** groups rows that have the same values into summary rows, typically used with aggregate functions.

## Syntax:
```sql
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1, column2, ...
HAVING group_condition
ORDER BY column1;
```

## Examples:

### 1. Count Users by City
```sql
SELECT city, COUNT(*) AS user_count
FROM users 
GROUP BY city
ORDER BY user_count DESC;
```

### 2. Average Age by Department
```sql
SELECT 
    department,
    COUNT(*) AS employee_count,
    AVG(age) AS average_age,
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM employees 
GROUP BY department;
```

### 3. Multiple Column Grouping
```sql
SELECT 
    city, 
    country, 
    COUNT(*) AS customers,
    AVG(order_value) AS avg_order
FROM customers 
GROUP BY city, country
HAVING COUNT(*) > 10;
```

### 4. Sales Summary by Year and Month
```sql
SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    COUNT(*) AS total_orders,
    SUM(total) AS total_revenue,
    AVG(total) AS average_order_value
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;
```

### 5. Product Categories Analysis
```sql
SELECT 
    category,
    COUNT(*) AS product_count,
    MIN(price) AS cheapest,
    MAX(price) AS most_expensive,
    AVG(price) AS average_price
FROM products
GROUP BY category
HAVING AVG(price) > 50;
```""",
        "reference": "https://www.w3schools.com/sql/sql_groupby.asp",
        "points": 1,
        "answers": [
            {"text": "CLUSTER BY", "is_correct": False},
            {"text": "GROUP BY", "is_correct": True},
            {"text": "COLLECT BY", "is_correct": False},
            {"text": "ORGANIZE BY", "is_correct": False},
        ],
    },
    {
        "text": "Which clause is used to filter groups created by GROUP BY?",
        "explanation": ("HAVING clause is used to filter groups because WHERE "
                        "cannot be used with aggregate functions. Examples:\n\n"
                        "-- Departments with more than 5 employees\n"
                        "SELECT department, COUNT(*)\n"
                        "FROM employees GROUP BY department\n"
                        "HAVING COUNT(*) > 5;\n\n"
                        "-- Categories with average price > 100\n"
                        "SELECT category, AVG(price)\n"
                        "FROM products GROUP BY category\n"
                        "HAVING AVG(price) > 100;"),
        "reference": "https://www.w3schools.com/sql/sql_having.asp",
        "points": 1,
        "answers": [
            {"text": "WHERE", "is_correct": False},
            {"text": "HAVING", "is_correct": True},
            {"text": "FILTER", "is_correct": False},
            {"text": "GROUP_FILTER", "is_correct": False},
        ],
    },
    {
        "text": ("What type of JOIN returns records that have matching "
                 "values in both tables?"),
        "explanation": """# INNER JOIN - Matching Records Only

**INNER JOIN** returns only records that have matching values in both tables. Records without matches are excluded.

## Syntax:
```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.column = table2.column;
```

## Examples:

### 1. Basic INNER JOIN
```sql
SELECT users.name, orders.total
FROM users 
INNER JOIN orders ON users.id = orders.user_id;
-- Only users who have placed orders
```

### 2. Multiple Table JOIN
```sql
SELECT 
    u.name, 
    o.total, 
    p.name as product
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN products p ON o.product_id = p.id;
```

### 3. JOIN with WHERE
```sql
SELECT c.name, o.order_date, o.total
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
WHERE o.total > 100;
```

### 4. Aggregate with JOIN
```sql
SELECT 
    c.name,
    COUNT(o.id) as total_orders,
    SUM(o.total) as total_spent
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name;
```""",
        "reference": "https://www.w3schools.com/sql/sql_join_inner.asp",
        "points": 1,
        "answers": [
            {"text": "OUTER JOIN", "is_correct": False},
            {"text": "INNER JOIN", "is_correct": True},
            {"text": "CROSS JOIN", "is_correct": False},
            {"text": "FULL JOIN", "is_correct": False},
        ],
    },
    {
        "text": "Which JOIN returns all records from the left table and matched records from the right table?",
        "explanation": """# LEFT JOIN - All Left Records + Matching Right

**LEFT JOIN** returns ALL records from the left table and matched records from the right table. If no match exists, NULL values are returned for right table columns.

## Syntax:
```sql
SELECT columns
FROM left_table
LEFT JOIN right_table ON left_table.column = right_table.column;
```

## Examples:

### 1. Customers and Their Orders
```sql
-- All customers, including those without orders
SELECT 
    c.customer_name,
    c.email,
    o.order_id,
    o.order_date,
    o.total
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- Result includes customers with no orders (order columns show NULL)
```

### 2. Employees and Departments
```sql
-- All employees, even if department is missing
SELECT 
    e.name,
    e.salary,
    d.department_name,
    d.budget
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

### 3. Finding Records with No Matches
```sql
-- Customers who haven't placed any orders
SELECT 
    c.customer_name,
    c.email
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;
```

### 4. Aggregate with LEFT JOIN
```sql
-- Customer order summary (including customers with 0 orders)
SELECT 
    c.customer_name,
    COUNT(o.order_id) as total_orders,
    COALESCE(SUM(o.total), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name;
```

### 5. Multiple LEFT JOINs
```sql
-- Complete customer profile with optional data
SELECT 
    c.customer_name,
    a.street_address,
    p.phone_number,
    COUNT(o.order_id) as order_count
FROM customers c
LEFT JOIN addresses a ON c.customer_id = a.customer_id
LEFT JOIN phones p ON c.customer_id = p.customer_id
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, a.street_address, p.phone_number;
```

## Key Points:
- Returns **ALL rows from LEFT table**
- Returns **matching rows from RIGHT table** 
- **NULL values** for non-matching right table columns
- Useful for finding records that **don't have relationships**""",
        "reference": "https://www.w3schools.com/sql/sql_join_left.asp",
        "points": 1,
        "answers": [
            {"text": "RIGHT JOIN", "is_correct": False},
            {"text": "LEFT JOIN", "is_correct": True},
            {"text": "INNER JOIN", "is_correct": False},
            {"text": "OUTER JOIN", "is_correct": False},
        ],
    },
    {
        "text": "What does RIGHT JOIN do?",
        "explanation": """# RIGHT JOIN - All Right Records + Matching Left

**RIGHT JOIN** returns ALL records from the right table and matched records from the left table. If no match exists, NULL values are returned for left table columns.

## Syntax:
```sql
SELECT columns
FROM left_table
RIGHT JOIN right_table ON left_table.column = right_table.column;
```

## Examples:

### 1. All Departments with Employee Count
```sql
-- All departments, even those without employees
SELECT 
    d.department_name,
    d.budget,
    e.name as employee_name,
    e.salary
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;

-- Shows all departments, NULL for employee data if no employees
```

### 2. Product Categories and Products
```sql
-- All categories, including empty ones
SELECT 
    c.category_name,
    p.product_name,
    p.price
FROM products p
RIGHT JOIN categories c ON p.category_id = c.id
ORDER BY c.category_name;
```

### 3. Finding Empty Groups
```sql
-- Departments without any employees
SELECT d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id
WHERE e.department_id IS NULL;
```

### 4. Complete Coverage Analysis
```sql
-- All possible statuses with order counts
SELECT 
    s.status_name,
    COUNT(o.order_id) as order_count,
    COALESCE(SUM(o.total), 0) as total_value
FROM orders o
RIGHT JOIN order_statuses s ON o.status = s.status_code
GROUP BY s.status_name;
```

## Note:
RIGHT JOIN is less commonly used than LEFT JOIN. Most developers prefer to rewrite RIGHT JOINs as LEFT JOINs by switching table order:

```sql
-- RIGHT JOIN version
SELECT columns FROM table1 RIGHT JOIN table2 ON condition;

-- Equivalent LEFT JOIN (preferred)
SELECT columns FROM table2 LEFT JOIN table1 ON condition;
```""",
        "reference": "https://www.w3schools.com/sql/sql_join_right.asp",
        "points": 1,
        "answers": [
            {"text": "Returns all records from left table", "is_correct": False},
            {"text": "Returns all records from right table", "is_correct": True},
            {"text": "Returns only matching records", "is_correct": False},
            {"text": "Returns all records from both tables", "is_correct": False},
        ],
    },
    {
        "text": "Which JOIN returns all records when there is a match in either table?",
        "explanation": """# FULL OUTER JOIN - All Records from Both Tables

**FULL OUTER JOIN** returns ALL records when there is a match in either left or right table. It's like combining LEFT JOIN and RIGHT JOIN.

## Syntax:
```sql
SELECT columns
FROM left_table
FULL OUTER JOIN right_table ON left_table.column = right_table.column;
```

## Examples:

### 1. Complete Customer-Order Overview
```sql
-- All customers AND all orders (even orphaned ones)
SELECT 
    c.customer_name,
    c.email,
    o.order_id,
    o.order_date,
    o.total
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;

-- Shows: customers without orders + orders without customers + matches
```

### 2. Employee-Department Complete View
```sql
-- All employees AND all departments
SELECT 
    e.name as employee_name,
    e.salary,
    d.department_name,
    d.budget
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;
```

### 3. Finding Data Quality Issues
```sql
-- Identify orphaned records on both sides
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    CASE 
        WHEN c.customer_id IS NULL THEN 'Orphaned Order'
        WHEN o.order_id IS NULL THEN 'Customer No Orders'
        ELSE 'Valid Relationship'
    END as relationship_status
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL OR o.order_id IS NULL;
```

### 4. Comparison Analysis
```sql
-- Compare last year vs this year sales
SELECT 
    COALESCE(ly.month, ty.month) as month,
    ly.sales as last_year_sales,
    ty.sales as this_year_sales,
    (ty.sales - ly.sales) as growth
FROM last_year_sales ly
FULL OUTER JOIN this_year_sales ty ON ly.month = ty.month
ORDER BY month;
```

## Database Support:
- **PostgreSQL**: FULL OUTER JOIN ✓
- **SQL Server**: FULL OUTER JOIN ✓  
- **Oracle**: FULL OUTER JOIN ✓
- **MySQL**: Not supported directly (use UNION of LEFT and RIGHT JOIN)

## MySQL Workaround:
```sql
-- MySQL doesn't support FULL OUTER JOIN directly
SELECT columns FROM table1 LEFT JOIN table2 ON condition
UNION
SELECT columns FROM table1 RIGHT JOIN table2 ON condition;
```""",
        "reference": "https://www.w3schools.com/sql/sql_join_full.asp",
        "points": 1,
        "answers": [
            {"text": "INNER JOIN", "is_correct": False},
            {"text": "FULL OUTER JOIN", "is_correct": True},
            {"text": "LEFT JOIN", "is_correct": False},
            {"text": "RIGHT JOIN", "is_correct": False},
        ],
    },
    {
        "text": "What is a primary key in SQL?",
        "explanation": ("A primary key is a column (or combination of columns) "
                        "that uniquely identifies each row in a table. Examples:\n\n"
                        "-- Single column primary key\n"
                        "CREATE TABLE users (\n"
                        "  id INT PRIMARY KEY,\n"
                        "  name VARCHAR(50)\n"
                        ");\n\n"
                        "-- Auto-increment primary key\n"
                        "CREATE TABLE orders (\n"
                        "  order_id INT AUTO_INCREMENT PRIMARY KEY,\n"
                        "  customer_id INT,\n"
                        "  total DECIMAL(10,2)\n"
                        ");\n\n"
                        "-- Composite primary key\n"
                        "CREATE TABLE order_items (\n"
                        "  order_id INT,\n"
                        "  product_id INT,\n"
                        "  quantity INT,\n"
                        "  PRIMARY KEY (order_id, product_id)\n"
                        ");"),
        "reference": "https://www.w3schools.com/sql/sql_primarykey.asp",
        "points": 1,
        "answers": [
            {"text": "A column that can contain null values", "is_correct": False},
            {"text": "A column that uniquely identifies each row", "is_correct": True},
            {"text": "A column that references another table", "is_correct": False},
            {"text": "A column with duplicate values", "is_correct": False},
        ],
    },
    {
        "text": "What is a foreign key in SQL?",
        "explanation": ("A foreign key is a column that refers to the primary "
                        "key in another table, creating a link between tables. "
                        "Examples:\n\n"
                        "-- Create referenced table first\n"
                        "CREATE TABLE departments (\n"
                        "  dept_id INT PRIMARY KEY,\n"
                        "  dept_name VARCHAR(50)\n"
                        ");\n\n"
                        "-- Create table with foreign key\n"
                        "CREATE TABLE employees (\n"
                        "  emp_id INT PRIMARY KEY,\n"
                        "  name VARCHAR(100),\n"
                        "  dept_id INT,\n"
                        "  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)\n"
                        ");\n\n"
                        "-- Add foreign key to existing table\n"
                        "ALTER TABLE employees\n"
                        "ADD CONSTRAINT fk_dept\n"
                        "FOREIGN KEY (dept_id) REFERENCES departments(dept_id);"),
        "reference": "https://www.w3schools.com/sql/sql_foreignkey.asp",
        "points": 1,
        "answers": [
            {"text": "A unique identifier in the same table", "is_correct": False},
            {"text": "A column that refers to primary key in another table", "is_correct": True},
            {"text": "A column that cannot be null", "is_correct": False},
            {"text": "A column with auto-increment values", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL statement is used to create a new table?",
        "explanation": """# CREATE TABLE Statement

**CREATE TABLE** creates a new table in a database with specified columns and constraints.

## Basic Syntax:
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
    table_constraints
);
```

## Examples:

### 1. Basic Table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);
```

### 2. Table with All Constraint Types
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18 AND age <= 65),
    salary DECIMAL(10,2) CHECK (salary > 0),
    department_id INT,
    hire_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

### 3. Table with Composite Primary Key
```sql
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### 4. Create Table from Another Table
```sql
CREATE TABLE active_customers AS
SELECT customer_id, name, email
FROM customers
WHERE status = 'active';
```""",
        "reference": "https://www.w3schools.com/sql/sql_create_table.asp",
        "points": 1,
        "answers": [
            {"text": "NEW TABLE", "is_correct": False},
            {"text": "CREATE TABLE", "is_correct": True},
            {"text": "MAKE TABLE", "is_correct": False},
            {"text": "BUILD TABLE", "is_correct": False},
        ],
    },
    {
        "text": ("What statement is used to add a new column to an "
                 "existing table?"),
        "explanation": ("ALTER TABLE with ADD COLUMN is used to add a new "
                        "column to an existing table. Examples:\n\n"
                        "-- Add a single column\n"
                        "ALTER TABLE users ADD COLUMN phone VARCHAR(15);\n\n"
                        "-- Add column with default value\n"
                        "ALTER TABLE users ADD COLUMN status VARCHAR(20)\n"
                        "DEFAULT 'active';\n\n"
                        "-- Add multiple columns\n"
                        "ALTER TABLE users\n"
                        "ADD COLUMN city VARCHAR(50),\n"
                        "ADD COLUMN country VARCHAR(50);"),
        "reference": "https://www.w3schools.com/sql/sql_alter.asp",
        "points": 1,
        "answers": [
            {"text": "ADD COLUMN", "is_correct": False},
            {"text": "ALTER TABLE ... ADD COLUMN", "is_correct": True},
            {"text": "INSERT COLUMN", "is_correct": False},
            {"text": "CREATE COLUMN", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to delete a table?",
        "explanation": "DROP TABLE statement is used to delete an existing table in a database.",
        "reference": "https://www.w3schools.com/sql/sql_drop_table.asp",
        "points": 1,
        "answers": [
            {"text": "DELETE TABLE", "is_correct": False},
            {"text": "DROP TABLE", "is_correct": True},
            {"text": "REMOVE TABLE", "is_correct": False},
            {"text": "DESTROY TABLE", "is_correct": False},
        ],
    },
    {
        "text": "What is an index in SQL?",
        "explanation": """# Database Indexes - Performance Optimization

An **index** is a database object that improves the speed of data retrieval operations on a table at the cost of additional storage space and slower write operations.

## How Indexes Work:
Think of an index like a book's index - it points to where data is located without scanning every page (row).

## Types of Indexes:

### 1. Clustered Index
- Physical order of data matches index order
- One per table (usually primary key)
- Data pages stored in order of index key

### 2. Non-Clustered Index
- Separate structure pointing to data rows
- Multiple per table allowed
- Faster lookups, doesn't change data order

## Examples:

### 1. Simple Single-Column Index
```sql
-- Index on frequently searched column
CREATE INDEX idx_employee_lastname 
ON employees(last_name);

-- Query now runs faster
SELECT * FROM employees WHERE last_name = 'Smith';
```

### 2. Composite (Multi-Column) Index
```sql
-- Index on multiple columns
CREATE INDEX idx_order_customer_date 
ON orders(customer_id, order_date);

-- Optimizes queries using both or first column
SELECT * FROM orders 
WHERE customer_id = 123 AND order_date >= '2024-01-01';
```

### 3. Unique Index
```sql
-- Ensures uniqueness AND improves performance
CREATE UNIQUE INDEX idx_employee_email 
ON employees(email);

-- Prevents duplicate emails and speeds up lookups
SELECT * FROM employees WHERE email = 'john@company.com';
```

### 4. Partial Index (PostgreSQL)
```sql
-- Index only on subset of data
CREATE INDEX idx_active_customers 
ON customers(customer_id)
WHERE status = 'active';

-- Only indexes active customers, saves space
```

### 5. Covering Index
```sql
-- Include additional columns for complete coverage
CREATE INDEX idx_order_covering 
ON orders(customer_id, order_date)
INCLUDE (total, status);

-- Query can be satisfied entirely from index
SELECT total, status FROM orders 
WHERE customer_id = 123 AND order_date = '2024-01-15';
```

## Index Management:

### Creating Indexes
```sql
-- Basic syntax
CREATE INDEX index_name ON table_name(column_list);

-- With options
CREATE INDEX idx_product_price 
ON products(price DESC)  -- Descending order
WHERE price > 0;         -- Conditional
```

### Dropping Indexes
```sql
-- Remove when no longer needed
DROP INDEX idx_employee_lastname;

-- Check index usage before dropping
SELECT * FROM sys.dm_db_index_usage_stats;  -- SQL Server
```

### Analyzing Index Performance
```sql
-- Check query execution plan
EXPLAIN SELECT * FROM employees WHERE last_name = 'Smith';

-- Index usage statistics
SHOW INDEX FROM employees;  -- MySQL
```

## Best Practices:

### ✅ Create Indexes For:
- Primary keys (automatic)
- Foreign keys
- Frequently searched columns (WHERE, ORDER BY)
- JOIN columns
- Columns used in GROUP BY

### ❌ Avoid Indexes On:
- Small tables (< 1000 rows)
- Columns that change frequently
- Tables with high INSERT/UPDATE rates
- Very wide columns (large text/binary data)

### Performance Examples:
```sql
-- Without index: Full table scan (slow)
SELECT * FROM orders WHERE customer_id = 123;
-- Execution time: 500ms on 1M rows

-- With index: Index seek (fast)
CREATE INDEX idx_orders_customer ON orders(customer_id);
SELECT * FROM orders WHERE customer_id = 123;
-- Execution time: 2ms on 1M rows

-- Composite index for complex queries
CREATE INDEX idx_orders_multi 
ON orders(customer_id, order_date, status);

-- Optimizes all these queries:
SELECT * FROM orders WHERE customer_id = 123;
SELECT * FROM orders WHERE customer_id = 123 AND order_date >= '2024-01-01';
SELECT * FROM orders WHERE customer_id = 123 AND order_date >= '2024-01-01' AND status = 'shipped';
```

## Index Maintenance:
```sql
-- Rebuild fragmented indexes (SQL Server)
ALTER INDEX ALL ON orders REBUILD;

-- Update index statistics
UPDATE STATISTICS orders;

-- Monitor index fragmentation
SELECT avg_fragmentation_in_percent 
FROM sys.dm_db_index_physical_stats(DB_ID(), OBJECT_ID('orders'), NULL, NULL, NULL);
```""",
        "reference": "https://www.w3schools.com/sql/sql_create_index.asp",
        "points": 1,
        "answers": [
            {"text": "A type of table", "is_correct": False},
            {"text": "A database object that speeds up data retrieval", "is_correct": True},
            {"text": "A data constraint", "is_correct": False},
            {"text": "A backup mechanism", "is_correct": False},
        ],
    },
    {
        "text": "Which statement creates an index?",
        "explanation": ("CREATE INDEX statement is used to create indexes "
                        "in tables. Examples:\n\n"
                        "-- Basic index syntax\n"
                        "CREATE INDEX index_name ON table_name(column_name);\n\n"
                        "-- Real examples\n"
                        "CREATE INDEX idx_customer_name\n"
                        "ON customers(last_name);\n\n"
                        "CREATE INDEX idx_order_date\n"
                        "ON orders(order_date DESC);\n\n"
                        "-- Multi-column index\n"
                        "CREATE INDEX idx_employee_dept_salary\n"
                        "ON employees(department, salary);\n\n"
                        "-- Unique index\n"
                        "CREATE UNIQUE INDEX idx_product_code\n"
                        "ON products(product_code);\n\n"
                        "-- Clustered index (SQL Server)\n"
                        "CREATE CLUSTERED INDEX idx_employee_id\n"
                        "ON employees(employee_id);"),
        "reference": "https://www.w3schools.com/sql/sql_create_index.asp",
        "points": 1,
        "answers": [
            {"text": "MAKE INDEX", "is_correct": False},
            {"text": "CREATE INDEX", "is_correct": True},
            {"text": "BUILD INDEX", "is_correct": False},
            {"text": "ADD INDEX", "is_correct": False},
        ],
    },
    {
        "text": "What is a view in SQL?",
        "explanation": ("A view is a virtual table based on the result-set "
                        "of an SQL statement. Examples:\n\n"
                        "-- Create a simple view\n"
                        "CREATE VIEW active_users AS\n"
                        "SELECT id, name, email\n"
                        "FROM users WHERE status = 'active';\n\n"
                        "-- Create view with joins\n"
                        "CREATE VIEW employee_details AS\n"
                        "SELECT e.name, e.salary, d.dept_name\n"
                        "FROM employees e\n"
                        "JOIN departments d ON e.dept_id = d.dept_id;\n\n"
                        "-- Use the view like a table\n"
                        "SELECT * FROM active_users WHERE name LIKE 'J%';\n\n"
                        "-- Update through view (if updatable)\n"
                        "UPDATE active_users SET email = 'new@email.com'\n"
                        "WHERE id = 1;"),
        "reference": "https://www.w3schools.com/sql/sql_view.asp",
        "points": 1,
        "answers": [
            {"text": "A physical table", "is_correct": False},
            {"text": "A virtual table based on SQL statement result", "is_correct": True},
            {"text": "A backup of a table", "is_correct": False},
            {"text": "A type of index", "is_correct": False},
        ],
    },
    {
        "text": "Which statement creates a view?",
        "explanation": "CREATE VIEW statement is used to create a view.",
        "reference": "https://www.w3schools.com/sql/sql_view.asp",
        "points": 1,
        "answers": [
            {"text": "MAKE VIEW", "is_correct": False},
            {"text": "CREATE VIEW", "is_correct": True},
            {"text": "BUILD VIEW", "is_correct": False},
            {"text": "NEW VIEW", "is_correct": False},
        ],
    },
    {
        "text": "What SQL function is used to convert text to uppercase?",
        "explanation": ("UPPER() function converts a string to uppercase "
                        "letters. Examples:\n\n"
                        "-- Convert names to uppercase\n"
                        "SELECT UPPER(name) FROM users;\n\n"
                        "-- Search case-insensitive\n"
                        "SELECT * FROM users\n"
                        "WHERE UPPER(name) = UPPER('john doe');\n\n"
                        "-- Update to uppercase\n"
                        "UPDATE users SET name = UPPER(name);"),
        "reference": "https://www.w3schools.com/sql/sql_ref_upper.asp",
        "points": 1,
        "answers": [
            {"text": "UPPERCASE()", "is_correct": False},
            {"text": "UPPER()", "is_correct": True},
            {"text": "UCASE()", "is_correct": False},
            {"text": "TOUPPER()", "is_correct": False},
        ],
    },
    {
        "text": "Which function converts text to lowercase?",
        "explanation": "LOWER() function converts a string to lowercase letters.",
        "reference": "https://www.w3schools.com/sql/sql_ref_lower.asp",
        "points": 1,
        "answers": [
            {"text": "LOWERCASE()", "is_correct": False},
            {"text": "LOWER()", "is_correct": True},
            {"text": "LCASE()", "is_correct": False},
            {"text": "TOLOWER()", "is_correct": False},
        ],
    },
    {
        "text": "What function returns the length of a string?",
        "explanation": "LEN() or LENGTH() function returns the number of characters in a string.",
        "reference": "https://www.w3schools.com/sql/sql_ref_len.asp",
        "points": 1,
        "answers": [
            {"text": "SIZE()", "is_correct": False},
            {"text": "LEN()", "is_correct": True},
            {"text": "COUNT_CHARS()", "is_correct": False},
            {"text": "STRING_SIZE()", "is_correct": False},
        ],
    },
    {
        "text": "Which function extracts a substring from a string?",
        "explanation": ("SUBSTRING() function extracts a substring from a "
                        "string starting at a specified position. Examples:\n\n"
                        "-- Get first 3 characters\n"
                        "SELECT SUBSTRING(name, 1, 3) FROM users;\n\n"
                        "-- Get area code from phone\n"
                        "SELECT SUBSTRING(phone, 1, 3) as area_code\n"
                        "FROM users;\n\n"
                        "-- Get domain from email\n"
                        "SELECT SUBSTRING(email, CHARINDEX('@', email) + 1)\n"
                        "FROM users;"),
        "reference": "https://www.w3schools.com/sql/sql_ref_substring.asp",
        "points": 1,
        "answers": [
            {"text": "EXTRACT()", "is_correct": False},
            {"text": "SUBSTRING()", "is_correct": True},
            {"text": "SUBSTR()", "is_correct": False},
            {"text": "MID()", "is_correct": False},
        ],
    },
    {
        "text": "What does CONCAT function do?",
        "explanation": """# CONCAT() Function - String Concatenation

**CONCAT()** function joins two or more strings together into a single string.

## Syntax:
```sql
CONCAT(string1, string2, ..., stringN)
```

## Examples:

### 1. Basic String Concatenation
```sql
-- Combine first and last name
SELECT CONCAT(first_name, ' ', last_name) as full_name
FROM employees;

-- Alternative syntax with || (PostgreSQL, Oracle)
SELECT first_name || ' ' || last_name as full_name
FROM employees;
```

### 2. Multiple String Concatenation
```sql
-- Build complete address
SELECT CONCAT(
    street_address, ', ',
    city, ', ',
    state, ' ',
    zip_code
) as full_address
FROM customers;
```

### 3. Concatenation with NULL Handling
```sql
-- CONCAT treats NULL as empty string
SELECT 
    CONCAT(first_name, ' ', middle_name, ' ', last_name) as full_name,
    -- vs manual concatenation (NULL breaks the chain)
    first_name + ' ' + middle_name + ' ' + last_name as broken_name
FROM employees;

-- Safe concatenation with COALESCE
SELECT CONCAT(
    first_name, ' ',
    COALESCE(middle_name || ' ', ''),
    last_name
) as safe_full_name
FROM employees;
```

### 4. Concatenation with Numbers
```sql
-- Convert numbers to strings and concatenate
SELECT CONCAT(
    'Order #', 
    CAST(order_id AS VARCHAR), 
    ' - Total: $', 
    CAST(total AS VARCHAR)
) as order_summary
FROM orders;
```

### 5. Dynamic SQL Building
```sql
-- Build email addresses
SELECT 
    CONCAT(
        LOWER(first_name), 
        '.', 
        LOWER(last_name), 
        '@company.com'
    ) as email_address
FROM employees;
```

### 6. Formatting Phone Numbers
```sql
-- Format phone number display
SELECT 
    name,
    CONCAT(
        '(', SUBSTRING(phone, 1, 3), ') ',
        SUBSTRING(phone, 4, 3), '-',
        SUBSTRING(phone, 7, 4)
    ) as formatted_phone
FROM customers
WHERE phone IS NOT NULL;
```

### 7. Creating Display Labels
```sql
-- Product display with price
SELECT 
    CONCAT(
        product_name, 
        ' - $', 
        FORMAT(price, 2),
        CASE WHEN on_sale = 1 THEN ' (ON SALE!)' ELSE '' END
    ) as product_display
FROM products;
```

### 8. URL Building
```sql
-- Build profile URLs
SELECT 
    username,
    CONCAT(
        'https://mysite.com/users/', 
        LOWER(username),
        '?id=', 
        CAST(user_id AS VARCHAR)
    ) as profile_url
FROM users;
```

### 9. Report Generation
```sql
-- Summary report strings
SELECT 
    department,
    CONCAT(
        'Department: ', department,
        ' has ', CAST(COUNT(*) AS VARCHAR), ' employees',
        ' with average salary $', CAST(ROUND(AVG(salary), 0) AS VARCHAR)
    ) as dept_summary
FROM employees
GROUP BY department;
```

### 10. Data Masking
```sql
-- Mask sensitive data for display
SELECT 
    customer_id,
    CONCAT(
        LEFT(first_name, 1),
        REPEAT('*', LENGTH(first_name) - 1),
        ' ',
        LEFT(last_name, 1),
        REPEAT('*', LENGTH(last_name) - 1)
    ) as masked_name
FROM customers;
```

## Database-Specific Variations:

### MySQL CONCAT
```sql
-- MySQL: CONCAT treats NULL as empty string
SELECT CONCAT('Hello', NULL, 'World');  -- Returns 'HelloWorld'

-- MySQL: CONCAT_WS (with separator)
SELECT CONCAT_WS(', ', first_name, middle_name, last_name) as full_name
FROM employees;  -- Ignores NULLs automatically
```

### PostgreSQL String Concatenation
```sql
-- PostgreSQL: || operator
SELECT first_name || ' ' || last_name as full_name
FROM employees;

-- PostgreSQL: String aggregation
SELECT STRING_AGG(name, ', ' ORDER BY name) as all_names
FROM employees
WHERE department = 'Sales';
```

### SQL Server Concatenation
```sql
-- SQL Server 2012+: CONCAT function
SELECT CONCAT(first_name, ' ', last_name) as full_name
FROM employees;

-- SQL Server: STRING_AGG (2017+)
SELECT STRING_AGG(name, ', ') WITHIN GROUP (ORDER BY name) as all_names
FROM employees
WHERE department = 'Sales';

-- Older SQL Server: + operator (NULL breaks chain)
SELECT first_name + ' ' + last_name as full_name
FROM employees
WHERE first_name IS NOT NULL AND last_name IS NOT NULL;
```

## Advanced Patterns:

### 1. Conditional Concatenation
```sql
SELECT 
    CONCAT(
        first_name,
        CASE 
            WHEN middle_name IS NOT NULL 
            THEN CONCAT(' ', middle_name, ' ')
            ELSE ' '
        END,
        last_name,
        CASE 
            WHEN suffix IS NOT NULL 
            THEN CONCAT(', ', suffix)
            ELSE ''
        END
    ) as formatted_name
FROM contacts;
```

### 2. Performance Considerations
```sql
-- For large datasets, consider indexing computed columns
ALTER TABLE employees 
ADD full_name AS CONCAT(first_name, ' ', last_name);

CREATE INDEX idx_employees_full_name ON employees(full_name);
```

### 3. JSON Building
```sql
-- Build simple JSON strings
SELECT CONCAT(
    '{"name":"', name, '",',
    '"email":"', email, '",',
    '"age":', CAST(age AS VARCHAR), '}'
) as user_json
FROM users;
```

## Common Use Cases:
- **Full names** from first/last name fields
- **Addresses** from separate address components  
- **Display labels** for user interfaces
- **URL generation** for web applications
- **Report formatting** for readable output
- **Data masking** for privacy protection
- **Email generation** from name patterns""",
        "reference": "https://www.w3schools.com/sql/sql_ref_concat.asp",
        "points": 1,
        "answers": [
            {"text": "Splits strings", "is_correct": False},
            {"text": "Joins strings together", "is_correct": True},
            {"text": "Compares strings", "is_correct": False},
            {"text": "Converts string case", "is_correct": False},
        ],
    },
    {
        "text": "Which function removes leading and trailing spaces?",
        "explanation": """# TRIM() Function - Removing Whitespace

**TRIM()** function removes leading and trailing whitespace (spaces, tabs, newlines) from strings.

## Basic Syntax:
```sql
TRIM([LEADING | TRAILING | BOTH] [characters FROM] string)
```

## Examples:

### 1. Basic Trimming
```sql
-- Remove leading and trailing spaces
SELECT TRIM('   Hello World   ') as cleaned;
-- Result: 'Hello World'

-- Clean user input data
UPDATE customers 
SET customer_name = TRIM(customer_name);
```

### 2. Selective Trimming
```sql
-- Remove only leading spaces
SELECT TRIM(LEADING ' ' FROM '   Hello World   ') as result;
-- Result: 'Hello World   '

-- Remove only trailing spaces  
SELECT TRIM(TRAILING ' ' FROM '   Hello World   ') as result;
-- Result: '   Hello World'
```

### 3. Custom Character Trimming
```sql
-- Remove specific characters
SELECT TRIM('0' FROM '000123000') as result;
-- Result: '123'

-- Remove multiple characters
SELECT TRIM('.,! ' FROM '...Hello World!!!   ') as result;
-- Result: 'Hello World'
```

### 4. Data Cleaning Examples
```sql
-- Clean imported data
UPDATE contacts SET
    first_name = TRIM(first_name),
    last_name = TRIM(last_name),
    email = TRIM(LOWER(email)),
    phone = TRIM(phone);

-- Find records that need cleaning
SELECT customer_id, customer_name
FROM customers 
WHERE customer_name != TRIM(customer_name);
```

### 5. Combined with Other Functions
```sql
-- Trim and convert to proper case
SELECT 
    TRIM(name) as clean_name,
    UPPER(TRIM(SUBSTRING(name, 1, 1))) || 
    LOWER(TRIM(SUBSTRING(name, 2))) as proper_case
FROM employees;

-- Clean and validate email
SELECT 
    email,
    TRIM(LOWER(email)) as cleaned_email,
    CASE 
        WHEN TRIM(email) LIKE '%@%.%' THEN 'Valid'
        ELSE 'Invalid'
    END as validation
FROM users;
```

### 6. Database-Specific Variations
```sql
-- SQL Server: LTRIM and RTRIM
SELECT 
    LTRIM('   text   ') as left_trimmed,   -- 'text   '
    RTRIM('   text   ') as right_trimmed,  -- '   text'
    LTRIM(RTRIM('   text   ')) as both;   -- 'text'

-- MySQL: TRIM variations
SELECT 
    TRIM('  text  ') as standard_trim,
    LTRIM('  text  ') as left_trim,
    RTRIM('  text  ') as right_trim;
```

## Common Use Cases:
- **Data Import**: Clean imported CSV data
- **User Input**: Sanitize form submissions  
- **Data Migration**: Clean legacy data
- **Search**: Normalize search terms
- **Display**: Format output consistently""",
        "reference": "https://www.w3schools.com/sql/sql_ref_trim.asp",
        "points": 1,
        "answers": [
            {"text": "STRIP()", "is_correct": False},
            {"text": "TRIM()", "is_correct": True},
            {"text": "CLEAN()", "is_correct": False},
            {"text": "REMOVE_SPACES()", "is_correct": False},
        ],
    },
    {
        "text": "What function returns the current date?",
        "explanation": """# Current Date Functions - Database-Specific

Different databases use different functions to get the current date and time.

## Database-Specific Functions:

### 1. SQL Server
```sql
-- Current date and time
SELECT GETDATE() as current_datetime;
-- Result: 2024-11-04 15:30:25.123

-- Current date only
SELECT CAST(GETDATE() AS DATE) as current_date;
-- Result: 2024-11-04

-- Current time only
SELECT CAST(GETDATE() AS TIME) as current_time;
-- Result: 15:30:25.123
```

### 2. MySQL
```sql
-- Current date and time
SELECT NOW() as current_datetime;
SELECT CURRENT_TIMESTAMP as current_timestamp;

-- Current date only  
SELECT CURDATE() as current_date;
SELECT CURRENT_DATE as current_date;

-- Current time only
SELECT CURTIME() as current_time;
SELECT CURRENT_TIME as current_time;
```

### 3. PostgreSQL
```sql
-- Current timestamp
SELECT NOW() as current_timestamp;
SELECT CURRENT_TIMESTAMP as current_timestamp;

-- Current date
SELECT CURRENT_DATE as current_date;

-- Current time
SELECT CURRENT_TIME as current_time;

-- Local time (without timezone)
SELECT LOCALTIMESTAMP as local_timestamp;
```

### 4. Oracle
```sql
-- Current date and time
SELECT SYSDATE FROM dual;

-- Current timestamp
SELECT CURRENT_TIMESTAMP FROM dual;

-- Current date (date only)
SELECT TRUNC(SYSDATE) FROM dual;
```

## Common Usage Examples:

### 1. Insert with Current Date
```sql
-- Insert new record with current timestamp
INSERT INTO orders (customer_id, order_date, total)
VALUES (123, GETDATE(), 299.99);  -- SQL Server

INSERT INTO orders (customer_id, order_date, total) 
VALUES (123, NOW(), 299.99);      -- MySQL/PostgreSQL
```

### 2. Filter by Current Date
```sql
-- Orders from today only
SELECT * FROM orders
WHERE DATE(order_date) = DATE(GETDATE());  -- SQL Server

SELECT * FROM orders  
WHERE DATE(order_date) = CURDATE();        -- MySQL

SELECT * FROM orders
WHERE order_date::date = CURRENT_DATE;     -- PostgreSQL
```

### 3. Date Calculations
```sql
-- Orders from last 30 days
SELECT * FROM orders
WHERE order_date >= DATEADD(day, -30, GETDATE());  -- SQL Server

SELECT * FROM orders
WHERE order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);  -- MySQL

SELECT * FROM orders  
WHERE order_date >= NOW() - INTERVAL '30 days';        -- PostgreSQL
```

### 4. Default Values in Table Creation
```sql
-- SQL Server
CREATE TABLE events (
    id INT IDENTITY(1,1) PRIMARY KEY,
    event_name VARCHAR(100),
    created_date DATETIME DEFAULT GETDATE()
);

-- MySQL
CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100),
    created_date TIMESTAMP DEFAULT NOW()
);

-- PostgreSQL
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name VARCHAR(100),
    created_date TIMESTAMP DEFAULT NOW()
);
```

### 5. Age Calculations
```sql
-- Calculate age in years
SELECT 
    name,
    birth_date,
    DATEDIFF(year, birth_date, GETDATE()) as age  -- SQL Server
FROM employees;

SELECT 
    name,
    birth_date,
    TIMESTAMPDIFF(YEAR, birth_date, NOW()) as age  -- MySQL
FROM employees;
```

### 6. Audit Timestamps
```sql
-- Update with current timestamp
UPDATE products 
SET last_modified = GETDATE(),
    modified_by = 'system'
WHERE product_id = 123;

-- Track when records were processed
SELECT 
    order_id,
    status,
    GETDATE() as processed_at
FROM orders 
WHERE status = 'pending';
```

## Best Practices:
- Use appropriate function for your database system
- Consider timezone implications for global applications  
- Use DATE() function to compare dates without time
- Store UTC timestamps for international applications""",
        "reference": "https://www.w3schools.com/sql/sql_dates.asp",
        "points": 1,
        "answers": [
            {"text": "TODAY()", "is_correct": False},
            {"text": "GETDATE()", "is_correct": True},
            {"text": "NOW_DATE()", "is_correct": False},
            {"text": "SYSDATE()", "is_correct": False},
        ],
    },
    {
        "text": "Which function extracts the year from a date?",
        "explanation": ("YEAR() function extracts the year part from a date. "
                        "Examples:\n\n"
                        "-- Extract year from order dates\n"
                        "SELECT YEAR(order_date) as order_year, COUNT(*)\n"
                        "FROM orders GROUP BY YEAR(order_date);\n\n"
                        "-- Filter by specific year\n"
                        "SELECT * FROM employees\n"
                        "WHERE YEAR(hire_date) = 2023;\n\n"
                        "-- Get current year\n"
                        "SELECT YEAR(GETDATE()) as current_year;\n\n"
                        "-- Extract other date parts\n"
                        "SELECT \n"
                        "  YEAR(order_date) as year,\n"
                        "  MONTH(order_date) as month,\n"
                        "  DAY(order_date) as day\n"
                        "FROM orders;\n\n"
                        "-- PostgreSQL syntax (EXTRACT)\n"
                        "SELECT EXTRACT(YEAR FROM order_date) FROM orders;"),
        "reference": "https://www.w3schools.com/sql/sql_dates.asp",
        "points": 1,
        "answers": [
            {"text": "GET_YEAR()", "is_correct": False},
            {"text": "YEAR()", "is_correct": True},
            {"text": "EXTRACT_YEAR()", "is_correct": False},
            {"text": "YYYY()", "is_correct": False},
        ],
    },
    {
        "text": "What does the ROUND function do?",
        "explanation": """# ROUND() Function - Number Rounding

**ROUND()** function rounds a number to a specified number of decimal places using standard rounding rules (0.5 rounds up).

## Syntax:
```sql
ROUND(number, decimal_places)
```

## Examples:

### 1. Basic Rounding
```sql
-- Round to whole numbers
SELECT ROUND(3.7) as rounded;     -- Result: 4
SELECT ROUND(3.2) as rounded;     -- Result: 3
SELECT ROUND(-3.7) as rounded;    -- Result: -4

-- Round to 2 decimal places
SELECT ROUND(3.14159, 2) as rounded;  -- Result: 3.14
SELECT ROUND(2.676, 2) as rounded;    -- Result: 2.68
```

### 2. Financial Calculations
```sql
-- Round prices to 2 decimal places
SELECT 
    product_name,
    price,
    ROUND(price * 1.0825, 2) as price_with_tax,
    ROUND(price * 0.85, 2) as sale_price
FROM products;

-- Calculate rounded totals
SELECT 
    order_id,
    SUM(quantity * unit_price) as subtotal,
    ROUND(SUM(quantity * unit_price) * 0.08, 2) as tax,
    ROUND(SUM(quantity * unit_price) * 1.08, 2) as total
FROM order_items
GROUP BY order_id;
```

### 3. Statistical Rounding
```sql
-- Round averages and percentages
SELECT 
    department,
    COUNT(*) as employee_count,
    ROUND(AVG(salary), 0) as avg_salary,
    ROUND(AVG(age), 1) as avg_age,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) as percentage
FROM employees
GROUP BY department;
```

### 4. Different Decimal Places
```sql
-- Round to different precision levels
SELECT 
    value,
    ROUND(value, 0) as whole_number,
    ROUND(value, 1) as one_decimal,
    ROUND(value, 2) as two_decimals,
    ROUND(value, -1) as nearest_ten,
    ROUND(value, -2) as nearest_hundred
FROM measurements;

-- Example with value = 1234.56789:
-- whole_number: 1235
-- one_decimal: 1234.6
-- two_decimals: 1234.57
-- nearest_ten: 1230
-- nearest_hundred: 1200
```

### 5. Performance Metrics
```sql
-- Round performance ratios
SELECT 
    employee_name,
    sales_target,
    actual_sales,
    ROUND((actual_sales / sales_target) * 100, 1) as achievement_percent,
    ROUND(actual_sales - sales_target, 0) as variance
FROM sales_performance;
```

### 6. Database-Specific Behavior
```sql
-- Most databases: standard rounding (0.5 rounds up)
SELECT ROUND(2.5);    -- Result: 3
SELECT ROUND(3.5);    -- Result: 4

-- Some databases use "banker's rounding" (round to even)
-- Check your database documentation for specific behavior
```

### 7. Comparison with Other Functions
```sql
SELECT 
    value,
    ROUND(value, 2) as rounded,
    TRUNCATE(value, 2) as truncated,  -- MySQL
    FLOOR(value) as floor_value,
    CEILING(value) as ceiling_value
FROM decimal_values;

-- Example with value = 3.789:
-- rounded: 3.79
-- truncated: 3.78 (cuts off, doesn't round)
-- floor_value: 3 (rounds down)  
-- ceiling_value: 4 (rounds up)
```

## Common Use Cases:
- **Financial calculations** (prices, taxes, totals)
- **Statistics** (averages, percentages, ratios)
- **Reporting** (clean display of calculated values)
- **Data validation** (ensuring consistent precision)""",
        "reference": "https://www.w3schools.com/sql/sql_ref_round.asp",
        "points": 1,
        "answers": [
            {"text": "Truncates numbers", "is_correct": False},
            {"text": "Rounds numbers to specified decimal places", "is_correct": True},
            {"text": "Converts to integer", "is_correct": False},
            {"text": "Finds absolute value", "is_correct": False},
        ],
    },
    {
        "text": "Which function returns the absolute value of a number?",
        "explanation": """# ABS() Function - Absolute Values

**ABS()** returns the absolute (positive) value of a number, removing the negative sign if present.

## Examples:
```sql
-- Basic absolute values
SELECT ABS(-5) as result;      -- Result: 5
SELECT ABS(5) as result;       -- Result: 5  
SELECT ABS(-3.14) as result;   -- Result: 3.14

-- Calculate differences
SELECT 
    actual_sales,
    target_sales,
    ABS(actual_sales - target_sales) as variance
FROM sales_data;

-- Distance calculations
SELECT 
    ABS(latitude1 - latitude2) as lat_diff,
    ABS(longitude1 - longitude2) as lng_diff
FROM locations;
```""",
        "reference": "https://www.w3schools.com/sql/sql_ref_abs.asp",
        "points": 1,
        "answers": [
            {"text": "ABSOLUTE()", "is_correct": False},
            {"text": "ABS()", "is_correct": True},
            {"text": "POSITIVE()", "is_correct": False},
            {"text": "MAGNITUDE()", "is_correct": False},
        ],
    },
    {
        "text": "What is a subquery in SQL?",
        "explanation": """# Subqueries - Nested Queries

A **subquery** is a query nested inside another query, used to return data that will be used by the main query.

## Types of Subqueries:
1. **Single Row Subquery** - Returns one row
2. **Multiple Row Subquery** - Returns multiple rows  
3. **Correlated Subquery** - References outer query
4. **Non-Correlated Subquery** - Independent of outer query

## Examples:

### 1. Subquery in WHERE Clause
```sql
-- Find users who have placed orders
SELECT name, email FROM users
WHERE id IN (SELECT DISTINCT user_id FROM orders);

-- Find products more expensive than average
SELECT name, price FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

### 2. Subquery in SELECT Clause
```sql
SELECT 
    name,
    email,
    (SELECT COUNT(*) FROM orders WHERE user_id = users.id) as order_count,
    (SELECT MAX(total) FROM orders WHERE user_id = users.id) as highest_order
FROM users;
```

### 3. Correlated Subquery
```sql
-- Products above average price in their category
SELECT * FROM products p1
WHERE price > (
    SELECT AVG(price) 
    FROM products p2
    WHERE p2.category = p1.category
);

-- Employees earning more than department average
SELECT name, salary, department
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```

### 4. EXISTS Subquery
```sql
-- Customers who have placed orders
SELECT name FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.customer_id = c.id
);
```

### 5. Multiple Row Subqueries
```sql
-- Products in categories with high-value orders
SELECT * FROM products
WHERE category IN (
    SELECT DISTINCT p.category
    FROM products p
    JOIN order_items oi ON p.id = oi.product_id
    JOIN orders o ON oi.order_id = o.id
    WHERE o.total > 1000
);
```

### 6. Subquery with ANY/ALL
```sql
-- Products cheaper than ANY luxury product
SELECT name, price FROM products
WHERE price < ANY (
    SELECT price FROM products WHERE category = 'Luxury'
);

-- Products more expensive than ALL budget products
SELECT name, price FROM products
WHERE price > ALL (
    SELECT price FROM products WHERE category = 'Budget'
);
```""",
        "reference": "https://www.w3schools.com/sql/sql_subqueries.asp",
        "points": 1,
        "answers": [
            {"text": "A query that runs after the main query", "is_correct": False},
            {"text": "A query nested inside another query", "is_correct": True},
            {"text": "A query that joins multiple tables", "is_correct": False},
            {"text": "A query that updates data", "is_correct": False},
        ],
    },
    {
        "text": ("Which keyword is used with subqueries to check if any "
                 "values satisfy the condition?"),
        "explanation": """# EXISTS - Checking for Subquery Results

**EXISTS** returns TRUE if the subquery returns at least one row.

## Examples:
```sql
-- Customers who have placed orders
SELECT name FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.customer_id = c.id
);

-- Products that have been sold  
SELECT product_name FROM products p
WHERE EXISTS (
    SELECT 1 FROM order_items oi
    WHERE oi.product_id = p.id
);

-- NOT EXISTS for opposite check
SELECT name FROM customers c  
WHERE NOT EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.id
);
-- Returns customers with no orders
```""",
        "reference": "https://www.w3schools.com/sql/sql_exists.asp",
        "points": 1,
        "answers": [
            {"text": "ANY", "is_correct": False},
            {"text": "EXISTS", "is_correct": True},
            {"text": "SOME", "is_correct": False},
            {"text": "ALL", "is_correct": False},
        ],
    },
    {
        "text": "What does UNION do in SQL?",
        "explanation": """# UNION Operations - Combining Result Sets

**UNION** combines the result sets of two or more SELECT statements vertically (row by row), removing duplicate records by default.

## Types of UNION:
- **UNION** - Removes duplicates (slower)
- **UNION ALL** - Keeps duplicates (faster)

## Rules for UNION:
1. Same number of columns in all SELECT statements
2. Columns must have compatible data types
3. Column order matters
4. Column names from first SELECT are used

## Examples:

### 1. Basic UNION (Remove Duplicates)
```sql
-- Combine customer and supplier names
SELECT name, 'Customer' as type FROM customers
UNION
SELECT name, 'Supplier' as type FROM suppliers
ORDER BY name;
```

### 2. UNION ALL (Keep Duplicates)
```sql
-- Include all cities, even duplicates
SELECT city FROM customers
UNION ALL
SELECT city FROM suppliers
UNION ALL
SELECT city FROM employees;
```

### 3. Complex UNION with Filtering
```sql
-- Active customers and premium suppliers
SELECT 
    id,
    name, 
    email,
    'Active Customer' as category
FROM customers 
WHERE status = 'active'

UNION

SELECT 
    supplier_id as id,
    company_name as name,
    contact_email as email,
    'Premium Supplier' as category
FROM suppliers 
WHERE tier = 'premium'

ORDER BY name;
```

### 4. UNION with Aggregations
```sql
-- Monthly summary combining online and store sales
SELECT 
    'Online' as channel,
    MONTH(order_date) as month,
    COUNT(*) as orders,
    SUM(total) as revenue
FROM online_orders
GROUP BY MONTH(order_date)

UNION ALL

SELECT 
    'Store' as channel,
    MONTH(sale_date) as month,
    COUNT(*) as orders,
    SUM(amount) as revenue
FROM store_sales
GROUP BY MONTH(sale_date)

ORDER BY channel, month;
```

### 5. UNION for Report Generation
```sql
-- Comprehensive contact list
SELECT 
    'Employee' as contact_type,
    CONCAT(first_name, ' ', last_name) as full_name,
    work_email as email,
    work_phone as phone,
    department as category
FROM employees
WHERE status = 'active'

UNION

SELECT 
    'Customer' as contact_type,
    customer_name as full_name,
    email,
    phone,
    customer_tier as category
FROM customers
WHERE active = 1

UNION

SELECT 
    'Vendor' as contact_type,
    vendor_name as full_name,
    contact_email as email,
    contact_phone as phone,
    vendor_type as category
FROM vendors
WHERE status = 'approved';
```

### 6. UNION vs JOIN Comparison
```sql
-- UNION: Combines rows vertically
SELECT name FROM table1
UNION
SELECT name FROM table2;

-- JOIN: Combines columns horizontally
SELECT t1.name, t2.name
FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id;
```

### 7. Performance Considerations
```sql
-- Use UNION ALL when you know there are no duplicates (faster)
SELECT id, name FROM current_customers
UNION ALL
SELECT id, name FROM archived_customers;

-- Use indexes on columns being UNIONed
CREATE INDEX idx_customer_name ON customers(name);
CREATE INDEX idx_supplier_name ON suppliers(name);

-- UNION with large result sets
SELECT name FROM customers WHERE region = 'North'
UNION
SELECT name FROM customers WHERE region = 'South';
```

## When to Use UNION:
- ✅ Combining similar data from different tables
- ✅ Creating comprehensive reports
- ✅ Merging current and historical data
- ✅ Consolidating data from multiple sources

## Alternatives to UNION:
- **INTERSECT** - Returns common records
- **EXCEPT** - Returns records from first query not in second
- **JOIN** - Combines tables horizontally""",
        "reference": "https://www.w3schools.com/sql/sql_union.asp",
        "points": 1,
        "answers": [
            {"text": "Joins tables horizontally", "is_correct": False},
            {"text": "Combines result sets vertically", "is_correct": True},
            {"text": "Updates multiple tables", "is_correct": False},
            {"text": "Creates intersections", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between UNION and UNION ALL?",
        "explanation": """# UNION vs UNION ALL

**UNION** removes duplicates, **UNION ALL** keeps all records including duplicates.

## Examples:
```sql
-- UNION (removes duplicates - slower)
SELECT city FROM customers
UNION 
SELECT city FROM suppliers;
-- Returns unique cities only

-- UNION ALL (keeps duplicates - faster)  
SELECT city FROM customers
UNION ALL
SELECT city FROM suppliers;  
-- Returns all cities, including duplicates

-- Performance difference:
-- UNION ALL is faster because it doesn't need to
-- check for and remove duplicates
```

## When to Use:
- **UNION**: When you need unique results
- **UNION ALL**: When duplicates are OK and you want better performance""",
        "reference": "https://www.w3schools.com/sql/sql_union.asp",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "UNION removes duplicates, UNION ALL includes duplicates", "is_correct": True},
            {"text": "UNION ALL is faster", "is_correct": False},
            {"text": "UNION ALL sorts results", "is_correct": False},
        ],
    },
    {
        "text": ("What constraint ensures that all values in a column "
                 "are different?"),
        "explanation": """# UNIQUE Constraint - No Duplicates

**UNIQUE** constraint ensures all values in a column are different (no duplicates allowed).

## Examples:

### 1. Single Column Unique
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    username VARCHAR(50) UNIQUE
);

-- This will fail due to UNIQUE constraint
INSERT INTO users VALUES (1, 'john@email.com', 'john');
INSERT INTO users VALUES (2, 'john@email.com', 'jane');  -- Error!
```

### 2. Composite Unique Constraint  
```sql
CREATE TABLE enrollments (
    id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    UNIQUE (student_id, course_id)
);

-- Student can't enroll in same course twice
INSERT INTO enrollments VALUES (1, 100, 201);
INSERT INTO enrollments VALUES (2, 100, 201);  -- Error!
```

### 3. Add to Existing Table
```sql
ALTER TABLE products
ADD CONSTRAINT uk_product_code UNIQUE (product_code);

-- Now product codes must be unique
```

## Key Points:
- UNIQUE allows one NULL value (NULL ≠ NULL)
- Different from PRIMARY KEY (table can have multiple UNIQUE constraints)
- Automatically creates an index for performance""",
        "reference": "https://www.w3schools.com/sql/sql_unique.asp",
        "points": 1,
        "answers": [
            {"text": "DISTINCT", "is_correct": False},
            {"text": "UNIQUE", "is_correct": True},
            {"text": "PRIMARY", "is_correct": False},
            {"text": "DIFFERENT", "is_correct": False},
        ],
    },
    {
        "text": "Which constraint prevents NULL values in a column?",
        "explanation": ("NOT NULL constraint prevents NULL values from being "
                        "inserted into a column. Examples:\n\n"
                        "-- Create table with NOT NULL constraints\n"
                        "CREATE TABLE employees (\n"
                        "  id INT PRIMARY KEY,\n"
                        "  name VARCHAR(100) NOT NULL,\n"
                        "  email VARCHAR(100) NOT NULL UNIQUE,\n"
                        "  salary DECIMAL(10,2),\n"
                        "  hire_date DATE NOT NULL\n"
                        ");\n\n"
                        "-- This will fail due to NOT NULL constraint\n"
                        "INSERT INTO employees (id, salary) VALUES (1, 50000);\n"
                        "-- Error: name, email, hire_date cannot be NULL\n\n"
                        "-- This will succeed\n"
                        "INSERT INTO employees (id, name, email, hire_date)\n"
                        "VALUES (1, 'John Doe', 'john@company.com', '2023-01-15');"),
        "reference": "https://www.w3schools.com/sql/sql_notnull.asp",
        "points": 1,
        "answers": [
            {"text": "NO_NULL", "is_correct": False},
            {"text": "NOT NULL", "is_correct": True},
            {"text": "REQUIRED", "is_correct": False},
            {"text": "MANDATORY", "is_correct": False},
        ],
    },
    {
        "text": "What does DEFAULT constraint do?",
        "explanation": ("DEFAULT constraint provides a default value for a "
                        "column when no value is specified. Examples:\n\n"
                        "-- Create table with default values\n"
                        "CREATE TABLE users (\n"
                        "  id INT PRIMARY KEY,\n"
                        "  name VARCHAR(100) NOT NULL,\n"
                        "  status VARCHAR(20) DEFAULT 'active',\n"
                        "  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n"
                        "  country VARCHAR(50) DEFAULT 'US'\n"
                        ");\n\n"
                        "-- Insert without specifying default columns\n"
                        "INSERT INTO users (id, name) VALUES (1, 'John Doe');\n"
                        "-- Will use defaults: status='active', created_at=now, country='US'\n\n"
                        "-- Insert with some defaults overridden\n"
                        "INSERT INTO users (id, name, country)\n"
                        "VALUES (2, 'Jane Smith', 'CA');"),
        "reference": "https://www.w3schools.com/sql/sql_default.asp",
        "points": 1,
        "answers": [
            {"text": "Sets maximum value", "is_correct": False},
            {"text": "Provides default value when none specified", "is_correct": True},
            {"text": "Validates data format", "is_correct": False},
            {"text": "Prevents duplicates", "is_correct": False},
        ],
    },
    {
        "text": ("Which constraint is used to limit the range of "
                 "values in a column?"),
        "explanation": ("CHECK constraint is used to limit the value range "
                        "that can be placed in a column. Examples:\n\n"
                        "-- Create table with CHECK constraints\n"
                        "CREATE TABLE employees (\n"
                        "  id INT PRIMARY KEY,\n"
                        "  name VARCHAR(100) NOT NULL,\n"
                        "  age INT CHECK (age >= 18 AND age <= 65),\n"
                        "  salary DECIMAL(10,2) CHECK (salary > 0),\n"
                        "  email VARCHAR(100) CHECK (email LIKE '%@%.%')\n"
                        ");\n\n"
                        "-- This will fail CHECK constraint\n"
                        "INSERT INTO employees VALUES (1, 'John', 16, 50000, 'john@email.com');\n"
                        "-- Error: age must be between 18 and 65\n\n"
                        "-- This will succeed\n"
                        "INSERT INTO employees VALUES (2, 'Jane', 25, 60000, 'jane@company.com');"),
        "reference": "https://www.w3schools.com/sql/sql_check.asp",
        "points": 1,
        "answers": [
            {"text": "RANGE", "is_correct": False},
            {"text": "CHECK", "is_correct": True},
            {"text": "LIMIT", "is_correct": False},
            {"text": "VALIDATE", "is_correct": False},
        ],
    },
    {
        "text": "What is normalization in database design?",
        "explanation": """# Database Normalization

**Normalization** is the process of organizing database tables to minimize redundancy and dependency, improving data integrity.

## Goals:
- Eliminate redundant data
- Ensure data consistency  
- Reduce storage space
- Prevent update anomalies

## Example - Before Normalization:
```sql
-- Poor design with redundancy
CREATE TABLE orders_bad (
    order_id INT,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    customer_phone VARCHAR(15),
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    quantity INT
);
-- Problems: Customer data repeated for each order
```

## After Normalization:
```sql
-- Better design - separate concerns
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

## Benefits:
- No duplicate customer data
- Update customer info in one place
- Data consistency maintained""",
        "reference": "https://www.studytonight.com/dbms/database-normalization.php",
        "points": 1,
        "answers": [
            {"text": "Adding more tables", "is_correct": False},
            {"text": "Organizing data to minimize redundancy", "is_correct": True},
            {"text": "Increasing data size", "is_correct": False},
            {"text": "Creating more indexes", "is_correct": False},
        ],
    },
    {
        "text": "What is First Normal Form (1NF)?",
        "explanation": """# First Normal Form (1NF)

**1NF** requires atomic values and unique records.

## Rules:
- Each column contains single values (no lists)  
- No duplicate rows
- Each row is uniquely identifiable

## Violation Example:
```sql
-- BAD: Multiple values in one column
CREATE TABLE employees_bad (
    id INT,
    name VARCHAR(100),  
    skills VARCHAR(200)  -- "Java,Python,SQL" violates 1NF
);
```

## 1NF Compliant:
```sql
-- GOOD: Atomic values only
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE employee_skills (
    employee_id INT,
    skill VARCHAR(50),
    PRIMARY KEY (employee_id, skill)
);

-- Each skill gets its own row
INSERT INTO employee_skills VALUES 
(1, 'Java'), (1, 'Python'), (1, 'SQL');
```""",
        "reference": "https://www.studytonight.com/dbms/first-normal-form.php",
        "points": 1,
        "answers": [
            {"text": "No duplicate rows", "is_correct": False},
            {"text": "Atomic values and unique records", "is_correct": True},
            {"text": "All columns must be keys", "is_correct": False},
            {"text": "No null values allowed", "is_correct": False},
        ],
    },
    {
        "text": "What command is used to start a transaction in SQL?",
        "explanation": """# Database Transactions

**BEGIN TRANSACTION** (or **START TRANSACTION**) starts a new database transaction, allowing multiple SQL statements to be executed as a single unit of work.

## ACID Properties:
- **A**tomicity - All operations succeed or all fail
- **C**onsistency - Database remains in valid state  
- **I**solation - Transactions don't interfere with each other
- **D**urability - Committed changes are permanent

## Examples:

### 1. Basic Transaction
```sql
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;  -- Save all changes
```

### 2. Transaction with Rollback
```sql
BEGIN TRANSACTION;
    DELETE FROM orders WHERE customer_id = 123;
    -- Oops, wrong customer!
ROLLBACK;  -- Undo all changes
```

### 3. Bank Transfer Example
```sql
BEGIN TRANSACTION;
    -- Check sufficient funds
    DECLARE @balance DECIMAL(10,2);
    SELECT @balance = balance FROM accounts WHERE id = 1;
    
    IF @balance >= 500
    BEGIN
        UPDATE accounts SET balance = balance - 500 WHERE id = 1;
        UPDATE accounts SET balance = balance + 500 WHERE id = 2;
        COMMIT;
    END
    ELSE
    BEGIN
        ROLLBACK;
        RAISERROR('Insufficient funds', 16, 1);
    END
```

### 4. Order Processing Transaction
```sql
BEGIN TRANSACTION;
    -- Create order
    INSERT INTO orders (customer_id, total, order_date)
    VALUES (123, 150.00, NOW());
    
    SET @order_id = LAST_INSERT_ID();
    
    -- Add order items
    INSERT INTO order_items (order_id, product_id, quantity, price)
    VALUES 
        (@order_id, 1, 2, 50.00),
        (@order_id, 2, 1, 50.00);
    
    -- Update inventory
    UPDATE products SET stock = stock - 2 WHERE id = 1;
    UPDATE products SET stock = stock - 1 WHERE id = 2;
    
    -- Check if any product went negative
    IF EXISTS (SELECT 1 FROM products WHERE stock < 0)
    BEGIN
        ROLLBACK;
        SELECT 'Order failed: Insufficient inventory' as error;
    END
    ELSE
    BEGIN
        COMMIT;
        SELECT 'Order processed successfully' as result;
    END
```

### 5. Different Database Syntax
```sql
-- MySQL/PostgreSQL
START TRANSACTION;
    INSERT INTO log_table VALUES ('Transaction started');
COMMIT;

-- SQL Server
BEGIN TRAN;
    UPDATE users SET last_login = GETDATE() WHERE id = 1;
COMMIT TRAN;

-- Oracle
BEGIN
    INSERT INTO audit_log VALUES (SYSDATE, 'User action');
    COMMIT;
END;
```""",
        "reference": "https://www.w3schools.com/sql/sql_transaction.asp",
        "points": 1,
        "answers": [
            {"text": "START", "is_correct": False},
            {"text": "BEGIN TRANSACTION", "is_correct": True},
            {"text": "OPEN TRANSACTION", "is_correct": False},
            {"text": "NEW TRANSACTION", "is_correct": False},
        ],
    },
    {
        "text": "Which command saves all changes made in a transaction?",
        "explanation": ("COMMIT command saves all changes made during the "
                        "current transaction. Examples:\n\n"
                        "-- Successful transaction\n"
                        "BEGIN TRANSACTION;\n"
                        "  INSERT INTO customers (name, email)\n"
                        "  VALUES ('John Doe', 'john@email.com');\n"
                        "  UPDATE customer_stats SET total_customers = total_customers + 1;\n"
                        "COMMIT; -- Saves all changes permanently\n\n"
                        "-- Banking transfer example\n"
                        "BEGIN TRANSACTION;\n"
                        "  UPDATE accounts SET balance = balance - 500\n"
                        "  WHERE account_id = 'ACC001';\n"
                        "  UPDATE accounts SET balance = balance + 500\n"
                        "  WHERE account_id = 'ACC002';\n"
                        "  -- If both updates successful\n"
                        "COMMIT; -- Make transfer permanent"),
        "reference": "https://www.w3schools.com/sql/sql_transaction.asp",
        "points": 1,
        "answers": [
            {"text": "SAVE", "is_correct": False},
            {"text": "COMMIT", "is_correct": True},
            {"text": "APPLY", "is_correct": False},
            {"text": "FINALIZE", "is_correct": False},
        ],
    },
    {
        "text": "What command undoes all changes made in a transaction?",
        "explanation": ("ROLLBACK command undoes all changes made during "
                        "the current transaction. Examples:\n\n"
                        "-- Error handling with rollback\n"
                        "BEGIN TRANSACTION;\n"
                        "  UPDATE inventory SET quantity = quantity - 10\n"
                        "  WHERE product_id = 1;\n"
                        "  -- Check if sufficient inventory\n"
                        "  IF (SELECT quantity FROM inventory WHERE product_id = 1) < 0\n"
                        "  THEN\n"
                        "    ROLLBACK; -- Undo the update\n"
                        "  ELSE\n"
                        "    COMMIT; -- Save the changes\n"
                        "  END IF;\n\n"
                        "-- Manual rollback\n"
                        "BEGIN TRANSACTION;\n"
                        "  DELETE FROM customers WHERE id = 5;\n"
                        "  -- Oops, wrong customer!\n"
                        "ROLLBACK; -- Undo the deletion"),
        "reference": "https://www.w3schools.com/sql/sql_transaction.asp",
        "points": 1,
        "answers": [
            {"text": "UNDO", "is_correct": False},
            {"text": "ROLLBACK", "is_correct": True},
            {"text": "CANCEL", "is_correct": False},
            {"text": "REVERT", "is_correct": False},
        ],
    },
    {
        "text": "What is ACID in database transactions?",
        "explanation": """# ACID Properties

**ACID** defines four key properties of reliable database transactions:

## A - Atomicity
```sql
-- All operations succeed or all fail together
BEGIN TRANSACTION;
    UPDATE account1 SET balance = balance - 100;
    UPDATE account2 SET balance = balance + 100;
COMMIT; -- Both updates or neither
```

## C - Consistency  
```sql
-- Database rules are always maintained
-- Account balances can't go negative
ALTER TABLE accounts ADD CONSTRAINT check_balance 
CHECK (balance >= 0);
```

## I - Isolation
```sql
-- Concurrent transactions don't interfere
-- Transaction 1: SELECT balance (sees $100)
-- Transaction 2: Can't modify until Transaction 1 completes
```

## D - Durability
```sql
-- Committed changes survive system crashes
COMMIT; -- Data permanently saved to disk
```

These properties ensure data reliability and consistency in multi-user database systems.""",
        "reference": "https://en.wikipedia.org/wiki/ACID",
        "points": 1,
        "answers": [
            {"text": "A type of database", "is_correct": False},
            {"text": "Properties of database transactions", "is_correct": True},
            {"text": "A SQL command", "is_correct": False},
            {"text": "A database constraint", "is_correct": False},
        ],
    },
    {
        "text": ("Which SQL clause is used to limit the number of "
                 "records returned?"),
        "explanation": ("LIMIT clause (or TOP in SQL Server) is used to "
                        "specify the number of records to return. Examples:\n\n"
                        "-- Get first 5 records\n"
                        "SELECT * FROM users LIMIT 5;\n\n"
                        "-- Get top 10 highest salaries\n"
                        "SELECT name, salary FROM employees\n"
                        "ORDER BY salary DESC LIMIT 10;\n\n"
                        "-- Pagination: Skip 20 records, get next 10\n"
                        "SELECT * FROM products\n"
                        "ORDER BY created_date DESC\n"
                        "LIMIT 10 OFFSET 20;\n\n"
                        "-- SQL Server syntax (TOP)\n"
                        "SELECT TOP 5 * FROM customers;\n\n"
                        "-- SQL Server with percent\n"
                        "SELECT TOP 10 PERCENT * FROM orders;"),
        "reference": "https://www.w3schools.com/sql/sql_top.asp",
        "points": 1,
        "answers": [
            {"text": "MAX", "is_correct": False},
            {"text": "LIMIT", "is_correct": True},
            {"text": "COUNT", "is_correct": False},
            {"text": "RESTRICT", "is_correct": False},
        ],
    },
    {
        "text": "What does OFFSET do in SQL?",
        "explanation": ("OFFSET specifies how many rows to skip before "
                        "starting to return rows from the query. Examples:\n\n"
                        "-- Basic pagination: Page 1 (first 10 records)\n"
                        "SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 0;\n\n"
                        "-- Page 2 (skip first 10, get next 10)\n"
                        "SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 10;\n\n"
                        "-- Page 3 (skip first 20, get next 10)\n"
                        "SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 20;\n\n"
                        "-- Get records 51-60 from sorted list\n"
                        "SELECT name, price FROM products\n"
                        "ORDER BY price DESC\n"
                        "LIMIT 10 OFFSET 50;\n\n"
                        "-- SQL Server syntax\n"
                        "SELECT * FROM products ORDER BY id\n"
                        "OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;"),
        "reference": "https://www.w3schools.com/mysql/mysql_limit.asp",
        "points": 1,
        "answers": [
            {"text": "Limits number of rows", "is_correct": False},
            {"text": "Skips specified number of rows", "is_correct": True},
            {"text": "Orders the results", "is_correct": False},
            {"text": "Groups the results", "is_correct": False},
        ],
    },
    {
        "text": "Which data type is used to store text in SQL?",
        "explanation": """# Text Data Types in SQL

**VARCHAR**, **CHAR**, and **TEXT** are used for storing text data.

## Common Text Types:
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),    -- Variable length, max 50 chars
    country_code CHAR(2),    -- Fixed length, exactly 2 chars
    description TEXT,        -- Large text (up to 64KB)
    bio LONGTEXT            -- Very large text (up to 4GB)
);
```

## Examples:
```sql
-- Insert text data
INSERT INTO users VALUES (
    1, 
    'john_doe',              -- VARCHAR: 8 characters
    'US',                    -- CHAR: exactly 2 characters  
    'User description here', -- TEXT: moderate length
    'Very long biography...' -- LONGTEXT: unlimited length
);

-- Query text data
SELECT * FROM users 
WHERE username LIKE 'john%'
   AND country_code = 'US';
```

## Key Differences:
- **VARCHAR(n)**: Variable length up to n characters
- **CHAR(n)**: Fixed length, exactly n characters (padded)
- **TEXT**: Large variable text (no length limit specified)""",
        "reference": "https://www.w3schools.com/sql/sql_datatypes.asp",
        "points": 1,
        "answers": [
            {"text": "STRING", "is_correct": False},
            {"text": "VARCHAR", "is_correct": True},
            {"text": "CHAR_DATA", "is_correct": False},
            {"text": "TEXT_TYPE", "is_correct": False},
        ],
    },
    {
        "text": "What data type is used for whole numbers in SQL?",
        "explanation": ("INT or INTEGER data type is used to store whole "
                        "numbers in SQL. Examples:\n\n"
                        "-- Different integer types\n"
                        "CREATE TABLE products (\n"
                        "  id INT PRIMARY KEY,          -- Standard integer\n"
                        "  quantity SMALLINT,           -- Small integer (-32,768 to 32,767)\n"
                        "  views BIGINT,               -- Large integer\n"
                        "  count TINYINT UNSIGNED      -- Tiny positive integer (0-255)\n"
                        ");\n\n"
                        "-- Insert integer data\n"
                        "INSERT INTO products VALUES (1, 100, 1500000, 25);\n\n"
                        "-- Auto-increment integer\n"
                        "CREATE TABLE orders (\n"
                        "  order_id INT AUTO_INCREMENT PRIMARY KEY,\n"
                        "  total INT\n"
                        ");"),
        "reference": "https://www.w3schools.com/sql/sql_datatypes.asp",
        "points": 1,
        "answers": [
            {"text": "NUMBER", "is_correct": False},
            {"text": "INT", "is_correct": True},
            {"text": "WHOLE", "is_correct": False},
            {"text": "NUMERIC", "is_correct": False},
        ],
    },
    {
        "text": "Which data type stores decimal numbers?",
        "explanation": ("DECIMAL, FLOAT, or REAL data types are used to store "
                        "decimal/floating-point numbers. Examples:\n\n"
                        "-- Different decimal types\n"
                        "CREATE TABLE financial_data (\n"
                        "  id INT PRIMARY KEY,\n"
                        "  price DECIMAL(10,2),        -- Fixed precision, 2 decimals\n"
                        "  weight FLOAT,               -- Floating point\n"
                        "  percentage DOUBLE,          -- Double precision\n"
                        "  rate NUMERIC(5,4)          -- 5 digits total, 4 after decimal\n"
                        ");\n\n"
                        "-- Insert decimal data\n"
                        "INSERT INTO financial_data VALUES (\n"
                        "  1, 99.99, 15.75, 0.125, 0.0525\n"
                        ");\n\n"
                        "-- Calculations with decimals\n"
                        "SELECT price * 1.08 as price_with_tax FROM financial_data;"),
        "reference": "https://www.w3schools.com/sql/sql_datatypes.asp",
        "points": 1,
        "answers": [
            {"text": "DECIMAL_NUM", "is_correct": False},
            {"text": "DECIMAL", "is_correct": True},
            {"text": "FRACTION", "is_correct": False},
            {"text": "POINT", "is_correct": False},
        ],
    },
    {
        "text": "What data type is used for storing dates?",
        "explanation": """# Date and Time Data Types

**DATE**, **TIME**, **DATETIME**, and **TIMESTAMP** are used for date/time values.

## Date/Time Types:
```sql
CREATE TABLE events (
    id INT PRIMARY KEY,
    event_date DATE,              -- Date only: '2024-11-04'
    event_time TIME,              -- Time only: '15:30:00'  
    created_at DATETIME,          -- Date + Time: '2024-11-04 15:30:00'
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Examples:
```sql
-- Insert date/time data
INSERT INTO events VALUES (
    1,
    '2024-11-04',                 -- DATE format
    '15:30:00',                   -- TIME format
    '2024-11-04 15:30:00',        -- DATETIME format
    NOW()                         -- Current timestamp
);

-- Query by date
SELECT * FROM events 
WHERE event_date = '2024-11-04';

-- Date range filtering
SELECT * FROM events
WHERE event_date BETWEEN '2024-01-01' AND '2024-12-31';
```

## Common Usage:
- **DATE**: Birth dates, event dates (YYYY-MM-DD)
- **TIME**: Event times, schedules (HH:MM:SS) 
- **DATETIME**: Complete timestamps
- **TIMESTAMP**: Audit trails, created/updated times""",
        "reference": "https://www.w3schools.com/sql/sql_datatypes.asp",
        "points": 1,
        "answers": [
            {"text": "TIME", "is_correct": False},
            {"text": "DATE", "is_correct": True},
            {"text": "CALENDAR", "is_correct": False},
            {"text": "DAY", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used to combine multiple conditions with OR logic?",
        "explanation": "OR operator is used to combine multiple conditions where at least one must be true.",
        "reference": "https://www.w3schools.com/sql/sql_and_or.asp",
        "points": 1,
        "answers": [
            {"text": "||", "is_correct": False},
            {"text": "OR", "is_correct": True},
            {"text": "EITHER", "is_correct": False},
            {"text": "ANY", "is_correct": False},
        ],
    },
    {
        "text": "Which operator combines conditions with AND logic?",
        "explanation": "AND operator is used to combine conditions where all must be true.",
        "reference": "https://www.w3schools.com/sql/sql_and_or.asp",
        "points": 1,
        "answers": [
            {"text": "&&", "is_correct": False},
            {"text": "AND", "is_correct": True},
            {"text": "BOTH", "is_correct": False},
            {"text": "ALL", "is_correct": False},
        ],
    },
    {
        "text": "What does the NOT operator do?",
        "explanation": "NOT operator negates a condition, returning the opposite boolean result.",
        "reference": "https://www.w3schools.com/sql/sql_and_or.asp",
        "points": 1,
        "answers": [
            {"text": "Combines conditions", "is_correct": False},
            {"text": "Negates a condition", "is_correct": True},
            {"text": "Compares values", "is_correct": False},
            {"text": "Sorts results", "is_correct": False},
        ],
    },
    {
        "text": "Which comparison operator means 'not equal to'?",
        "explanation": "<> or != operator means 'not equal to' in SQL.",
        "reference": "https://www.w3schools.com/sql/sql_operators.asp",
        "points": 1,
        "answers": [
            {"text": "!=", "is_correct": True},
            {"text": "==", "is_correct": False},
            {"text": "<=", "is_correct": False},
            {"text": ">=", "is_correct": False},
        ],
    },
    {
        "text": "What does CASE statement do in SQL?",
        "explanation": """# CASE Statement - Conditional Logic

**CASE** statement provides conditional logic in SQL, similar to if-else statements in programming languages.

## Two Types:

### 1. Searched CASE (with conditions)
```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END
```

### 2. Simple CASE (value matching)
```sql
CASE column_name
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE default_result
END
```

## Examples:

### 1. Salary Categories
```sql
SELECT 
    name, 
    salary,
    CASE
        WHEN salary < 30000 THEN 'Low'
        WHEN salary BETWEEN 30000 AND 70000 THEN 'Medium'
        WHEN salary > 70000 THEN 'High'
        ELSE 'Unknown'
    END as salary_category
FROM employees;
```

### 2. CASE in UPDATE Statement
```sql
UPDATE employees
SET bonus = CASE
    WHEN performance = 'Excellent' THEN salary * 0.15
    WHEN performance = 'Good' THEN salary * 0.10
    WHEN performance = 'Average' THEN salary * 0.05
    ELSE 0
END;
```

### 3. Simple CASE (Value Matching)
```sql
SELECT 
    product_name,
    price,
    CASE category
        WHEN 'Electronics' THEN 'Tech'
        WHEN 'Clothing' THEN 'Fashion'
        WHEN 'Books' THEN 'Education'
        ELSE 'Other'
    END as category_group
FROM products;
```

### 4. CASE in Aggregations
```sql
SELECT 
    department,
    COUNT(*) as total_employees,
    COUNT(CASE WHEN salary > 50000 THEN 1 END) as high_earners,
    COUNT(CASE WHEN age < 30 THEN 1 END) as young_employees
FROM employees
GROUP BY department;
```

### 5. Nested CASE
```sql
SELECT 
    name,
    CASE
        WHEN age < 18 THEN 'Minor'
        WHEN age >= 18 AND age < 65 THEN
            CASE
                WHEN salary > 100000 THEN 'High Earner Adult'
                ELSE 'Regular Adult'
            END
        ELSE 'Senior'
    END as category
FROM employees;
```""",
        "reference": "https://www.w3schools.com/sql/sql_case.asp",
        "points": 1,
        "answers": [
            {"text": "Creates new tables", "is_correct": False},
            {"text": "Provides conditional logic", "is_correct": True},
            {"text": "Sorts data", "is_correct": False},
            {"text": "Groups data", "is_correct": False},
        ],
    },
    {
        "text": "Which function converts a value to a different data type?",
        "explanation": "CAST() or CONVERT() functions are used to convert values from one data type to another.",
        "reference": "https://www.w3schools.com/sql/sql_cast.asp",
        "points": 1,
        "answers": [
            {"text": "CHANGE()", "is_correct": False},
            {"text": "CAST()", "is_correct": True},
            {"text": "TRANSFORM()", "is_correct": False},
            {"text": "ALTER()", "is_correct": False},
        ],
    },
    {
        "text": "What is a stored procedure?",
        "explanation": ("A stored procedure is a prepared SQL code that can be "
                        "saved and reused multiple times. Examples:\n\n"
                        "-- Create a simple stored procedure\n"
                        "DELIMITER //\n"
                        "CREATE PROCEDURE GetCustomerOrders(IN customer_id INT)\n"
                        "BEGIN\n"
                        "  SELECT * FROM orders WHERE customer_id = customer_id;\n"
                        "END //\n"
                        "DELIMITER ;\n\n"
                        "-- Stored procedure with parameters\n"
                        "CREATE PROCEDURE AddEmployee(\n"
                        "  IN p_name VARCHAR(100),\n"
                        "  IN p_department VARCHAR(50),\n"
                        "  IN p_salary DECIMAL(10,2)\n"
                        ")\n"
                        "BEGIN\n"
                        "  INSERT INTO employees (name, department, salary)\n"
                        "  VALUES (p_name, p_department, p_salary);\n"
                        "END;\n\n"
                        "-- Execute procedures\n"
                        "CALL GetCustomerOrders(123);\n"
                        "CALL AddEmployee('John', 'IT', 75000);"),
        "reference": "https://www.w3schools.com/sql/sql_stored_procedures.asp",
        "points": 1,
        "answers": [
            {"text": "A type of table", "is_correct": False},
            {"text": "Prepared SQL code that can be reused", "is_correct": True},
            {"text": "A database backup", "is_correct": False},
            {"text": "A data constraint", "is_correct": False},
        ],
    },
    {
        "text": "Which command executes a stored procedure?",
        "explanation": ("EXECUTE or EXEC command is used to run a stored "
                        "procedure. Examples:\n\n"
                        "-- Execute procedure without parameters\n"
                        "EXEC GetAllEmployees;\n"
                        "EXECUTE GetAllEmployees;\n\n"
                        "-- Execute with input parameters\n"
                        "EXEC GetEmployeeByDept 'Sales';\n"
                        "EXECUTE GetEmployeesByDate '2024-01-01', '2024-12-31';\n\n"
                        "-- Execute with output parameters\n"
                        "DECLARE @count INT;\n"
                        "EXEC CountEmployees @dept = 'IT', @total = @count OUTPUT;\n"
                        "SELECT @count as TotalEmployees;\n\n"
                        "-- Execute with return value\n"
                        "DECLARE @result INT;\n"
                        "SET @result = EXEC ValidateEmployee 'john.doe';"),
        "reference": "https://www.w3schools.com/sql/sql_stored_procedures.asp",
        "points": 1,
        "answers": [
            {"text": "RUN", "is_correct": False},
            {"text": "EXECUTE", "is_correct": True},
            {"text": "CALL", "is_correct": False},
            {"text": "START", "is_correct": False},
        ],
    },
    {
        "text": "What is a trigger in SQL?",
        "explanation": ("A trigger is a special stored procedure that "
                        "automatically executes in response to database "
                        "events. Examples:\n\n"
                        "-- BEFORE INSERT trigger\n"
                        "CREATE TRIGGER before_employee_insert\n"
                        "  BEFORE INSERT ON employees\n"
                        "  FOR EACH ROW\n"
                        "BEGIN\n"
                        "  SET NEW.created_date = NOW();\n"
                        "  SET NEW.email = LOWER(NEW.email);\n"
                        "END;\n\n"
                        "-- AFTER UPDATE trigger for audit\n"
                        "CREATE TRIGGER audit_salary_changes\n"
                        "  AFTER UPDATE ON employees\n"
                        "  FOR EACH ROW\n"
                        "BEGIN\n"
                        "  IF OLD.salary != NEW.salary THEN\n"
                        "    INSERT INTO salary_audit (employee_id, old_salary,\n"
                        "                             new_salary, change_date)\n"
                        "    VALUES (NEW.id, OLD.salary, NEW.salary, NOW());\n"
                        "  END IF;\n"
                        "END;"),
        "reference": "https://www.w3schools.com/sql/sql_triggers.asp",
        "points": 1,
        "answers": [
            {"text": "A manual procedure", "is_correct": False},
            {"text": "Automatic procedure that responds to events", "is_correct": True},
            {"text": "A type of index", "is_correct": False},
            {"text": "A database backup", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL feature allows you to create temporary result sets?",
        "explanation": ("Common Table Expressions (CTEs) using WITH clause "
                        "create temporary named result sets. Examples:\n\n"
                        "-- Simple CTE\n"
                        "WITH sales_summary AS (\n"
                        "  SELECT department, SUM(sales) as total_sales\n"
                        "  FROM sales_data\n"
                        "  GROUP BY department\n"
                        ")\n"
                        "SELECT * FROM sales_summary\n"
                        "WHERE total_sales > 100000;\n\n"
                        "-- Multiple CTEs\n"
                        "WITH regional_sales AS (\n"
                        "  SELECT region, SUM(sales) as total\n"
                        "  FROM sales GROUP BY region\n"
                        "),\n"
                        "top_regions AS (\n"
                        "  SELECT region FROM regional_sales\n"
                        "  WHERE total > (SELECT AVG(total) FROM regional_sales)\n"
                        ")\n"
                        "SELECT * FROM sales s\n"
                        "JOIN top_regions tr ON s.region = tr.region;"),
        "reference": "https://www.sqlservertutorial.net/sql-server-basics/sql-server-cte/",
        "points": 1,
        "answers": [
            {"text": "Views", "is_correct": False},
            {"text": "Common Table Expressions (CTEs)", "is_correct": True},
            {"text": "Temporary tables", "is_correct": False},
            {"text": "Stored procedures", "is_correct": False},
        ],
    },
    {
        "text": "What does COALESCE function do?",
        "explanation": ("COALESCE returns the first non-NULL value from a "
                        "list of expressions. Examples:\n\n"
                        "-- Handle NULL values in display\n"
                        "SELECT name,\n"
                        "       COALESCE(phone, email, 'No contact') as contact\n"
                        "FROM customers;\n\n"
                        "-- Default values for calculations\n"
                        "SELECT product_name,\n"
                        "       price * COALESCE(discount_rate, 0) as discount,\n"
                        "       price - (price * COALESCE(discount_rate, 0)) "
                        "as final_price\n"
                        "FROM products;\n\n"
                        "-- Multiple fallback options\n"
                        "SELECT employee_id,\n"
                        "       COALESCE(work_phone, home_phone, mobile_phone,\n"
                        "               'No phone available') as contact_number\n"
                        "FROM employees;"),
        "reference": "https://www.w3schools.com/sql/sql_isnull.asp",
        "points": 1,
        "answers": [
            {"text": "Combines strings", "is_correct": False},
            {"text": "Returns first non-NULL value", "is_correct": True},
            {"text": "Counts NULL values", "is_correct": False},
            {"text": "Removes NULL values", "is_correct": False},
        ],
    },
    {
        "text": "Which clause is used to specify window functions?",
        "explanation": ("OVER clause is used to define the window specification "
                        "for window functions. Examples:\n\n"
                        "-- Row number within each department\n"
                        "SELECT name, department, salary,\n"
                        "  ROW_NUMBER() OVER (PARTITION BY department\n"
                        "                     ORDER BY salary DESC) as dept_rank\n"
                        "FROM employees;\n\n"
                        "-- Running total of sales\n"
                        "SELECT order_date, amount,\n"
                        "  SUM(amount) OVER (ORDER BY order_date\n"
                        "                    ROWS UNBOUNDED PRECEDING) as running_total\n"
                        "FROM orders;\n\n"
                        "-- Compare with previous value\n"
                        "SELECT month, sales,\n"
                        "  LAG(sales) OVER (ORDER BY month) as prev_month,\n"
                        "  sales - LAG(sales) OVER (ORDER BY month) as growth\n"
                        "FROM monthly_sales;"),
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/",
        "points": 1,
        "answers": [
            {"text": "WINDOW", "is_correct": False},
            {"text": "OVER", "is_correct": True},
            {"text": "PARTITION", "is_correct": False},
            {"text": "RANGE", "is_correct": False},
        ],
    },
    {
        "text": "What does ROW_NUMBER() window function do?",
        "explanation": """# ROW_NUMBER() Window Function

**ROW_NUMBER()** assigns a unique sequential number to each row within a partition, starting from 1.

## Syntax:
```sql
ROW_NUMBER() OVER (
    [PARTITION BY column(s)]
    ORDER BY column(s)
)
```

## Examples:

### 1. Number All Employees
```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY hire_date) as emp_num,
    name, 
    hire_date
FROM employees;
```

### 2. Top 3 Salaries per Department
```sql
WITH ranked_employees AS (
    SELECT 
        name, 
        department, 
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department 
            ORDER BY salary DESC
        ) as rn
    FROM employees
)
SELECT name, department, salary
FROM ranked_employees 
WHERE rn <= 3;
```

### 3. Pagination Using ROW_NUMBER
```sql
WITH numbered_products AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY id) as rn,
        product_name, 
        price
    FROM products
)
SELECT product_name, price
FROM numbered_products 
WHERE rn BETWEEN 21 AND 30;  -- Page 3 (rows 21-30)
```

### 4. Deduplication
```sql
WITH duplicates AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY email 
            ORDER BY created_date DESC
        ) as rn
    FROM users
)
DELETE FROM duplicates WHERE rn > 1;
```""",
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-row_number-function/",
        "points": 1,
        "answers": [
            {"text": "Counts total rows", "is_correct": False},
            {"text": "Assigns sequential numbers to rows", "is_correct": True},
            {"text": "Ranks rows by value", "is_correct": False},
            {"text": "Groups rows together", "is_correct": False},
        ],
    },
    {
        "text": "Which function returns the rank of a row within a partition?",
        "explanation": "RANK() function returns the rank of each row within a partition, with gaps for ties.",
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-rank-function/",
        "points": 1,
        "answers": [
            {"text": "ORDER()", "is_correct": False},
            {"text": "RANK()", "is_correct": True},
            {"text": "POSITION()", "is_correct": False},
            {"text": "LEVEL()", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between DENSE_RANK() and RANK()?",
        "explanation": "DENSE_RANK() returns consecutive rank values without gaps, while RANK() leaves gaps when there are ties.",
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-dense_rank-function/",
        "points": 2,
        "answers": [
            {"text": "DENSE_RANK() has no gaps in ranking", "is_correct": True},
            {"text": "RANK() has no gaps in ranking", "is_correct": False},
            {"text": "They are identical functions", "is_correct": False},
            {"text": "DENSE_RANK() only works with numbers", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL clause is used to create a recursive query?",
        "explanation": ("WITH RECURSIVE clause allows creation of recursive "
                        "Common Table Expressions (CTEs). Examples:\n\n"
                        "-- Organizational hierarchy\n"
                        "WITH RECURSIVE employee_hierarchy AS (\n"
                        "  -- Anchor member: top-level managers\n"
                        "  SELECT employee_id, name, manager_id, 0 as level\n"
                        "  FROM employees\n"
                        "  WHERE manager_id IS NULL\n"
                        "  \n"
                        "  UNION ALL\n"
                        "  \n"
                        "  -- Recursive member: subordinates\n"
                        "  SELECT e.employee_id, e.name, e.manager_id, eh.level + 1\n"
                        "  FROM employees e\n"
                        "  JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id\n"
                        ")\n"
                        "SELECT * FROM employee_hierarchy\n"
                        "ORDER BY level, name;\n\n"
                        "-- Generate number series\n"
                        "WITH RECURSIVE numbers AS (\n"
                        "  SELECT 1 as n\n"
                        "  UNION ALL\n"
                        "  SELECT n + 1 FROM numbers WHERE n < 100\n"
                        ")\n"
                        "SELECT * FROM numbers;"),
        "reference": "https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-RECURSIVE",
        "points": 2,
        "answers": [
            {"text": "RECURSIVE", "is_correct": False},
            {"text": "WITH RECURSIVE", "is_correct": True},
            {"text": "CTE RECURSIVE", "is_correct": False},
            {"text": "LOOP WITH", "is_correct": False},
        ],
    },
    {
        "text": "What does the COALESCE function do?",
        "explanation": "COALESCE returns the first non-NULL value from a list of expressions.",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_coalesce.asp",
        "points": 1,
        "answers": [
            {"text": "Combines strings", "is_correct": False},
            {"text": "Returns first non-NULL value", "is_correct": True},
            {"text": "Counts NULL values", "is_correct": False},
            {"text": "Removes NULL values", "is_correct": False},
        ],
    },
    {
        "text": "Which statement correctly uses the CASE expression?",
        "explanation": "CASE WHEN condition THEN result ELSE default_result END is the correct syntax for CASE expressions.",
        "reference": "https://www.w3schools.com/sql/sql_case.asp",
        "points": 1,
        "answers": [
            {"text": "IF condition THEN result END", "is_correct": False},
            {"text": "CASE WHEN condition THEN result END", "is_correct": True},
            {"text": "SWITCH condition THEN result END", "is_correct": False},
            {"text": "WHEN condition CASE result END", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the PARTITION BY clause in window functions?",
        "explanation": "PARTITION BY divides the result set into partitions and applies the window function to each partition separately.",
        "reference": "https://www.postgresql.org/docs/current/tutorial-window.html",
        "points": 2,
        "answers": [
            {"text": "Divides result into partitions", "is_correct": True},
            {"text": "Sorts the entire result set", "is_correct": False},
            {"text": "Limits the number of rows", "is_correct": False},
            {"text": "Groups rows for aggregation", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL function calculates a running total?",
        "explanation": "SUM() with OVER clause and appropriate window frame creates a running total.",
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-sum-function/",
        "points": 2,
        "answers": [
            {"text": "RUNNING_SUM()", "is_correct": False},
            {"text": "SUM() OVER()", "is_correct": True},
            {"text": "CUMULATIVE_SUM()", "is_correct": False},
            {"text": "TOTAL()", "is_correct": False},
        ],
    },
    {
        "text": "What does the LAG() window function do?",
        "explanation": ("LAG() accesses data from a previous row in the same "
                        "result set without using a self-join. Examples:\n\n"
                        "-- Compare current vs previous month sales\n"
                        "SELECT month, sales,\n"
                        "  LAG(sales, 1) OVER (ORDER BY month) as prev_month,\n"
                        "  sales - LAG(sales, 1) OVER (ORDER BY month) as growth\n"
                        "FROM monthly_sales;\n\n"
                        "-- Stock price change analysis\n"
                        "SELECT date, close_price,\n"
                        "  LAG(close_price, 1, 0) OVER (ORDER BY date) as prev_close,\n"
                        "  close_price - LAG(close_price, 1, 0) OVER (ORDER BY date) as change\n"
                        "FROM stock_prices;\n\n"
                        "-- Employee salary history\n"
                        "SELECT employee_id, effective_date, salary,\n"
                        "  LAG(salary, 1) OVER (PARTITION BY employee_id\n"
                        "                       ORDER BY effective_date) as prev_salary\n"
                        "FROM salary_history;"),
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-lag-function/",
        "points": 2,
        "answers": [
            {"text": "Delays query execution", "is_correct": False},
            {"text": "Accesses previous row data", "is_correct": True},
            {"text": "Creates time delays", "is_correct": False},
            {"text": "Slows down queries", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for pattern matching with wildcards?",
        "explanation": "LIKE operator is used with wildcards (% and _) for pattern matching in WHERE clauses.",
        "reference": "https://www.w3schools.com/sql/sql_like.asp",
        "points": 1,
        "answers": [
            {"text": "MATCH", "is_correct": False},
            {"text": "LIKE", "is_correct": True},
            {"text": "SIMILAR", "is_correct": False},
            {"text": "PATTERN", "is_correct": False},
        ],
    },
    {
        "text": "What does the LEAD() function return?",
        "explanation": "LEAD() returns data from the next row in the result set, essentially the opposite of LAG().",
        "reference": "https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-lead-function/",
        "points": 2,
        "answers": [
            {"text": "First row data", "is_correct": False},
            {"text": "Next row data", "is_correct": True},
            {"text": "Last row data", "is_correct": False},
            {"text": "Random row data", "is_correct": False},
        ],
    },
    {
        "text": "Which clause is used to specify the number of rows to return?",
        "explanation": "LIMIT clause (or TOP in some databases) restricts the number of rows returned by a query.",
        "reference": "https://www.w3schools.com/sql/sql_top.asp",
        "points": 1,
        "answers": [
            {"text": "ROWS", "is_correct": False},
            {"text": "LIMIT", "is_correct": True},
            {"text": "COUNT", "is_correct": False},
            {"text": "FETCH", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the OFFSET clause?",
        "explanation": "OFFSET specifies how many rows to skip before starting to return rows from the query.",
        "reference": "https://www.w3schools.com/sql/sql_top.asp",
        "points": 1,
        "answers": [
            {"text": "Skips specified number of rows", "is_correct": True},
            {"text": "Limits result set size", "is_correct": False},
            {"text": "Orders the results", "is_correct": False},
            {"text": "Groups the results", "is_correct": False},
        ],
    },
    {
        "text": "Which function converts a string to uppercase?",
        "explanation": "UPPER() function converts all characters in a string to uppercase.",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_upper.asp",
        "points": 1,
        "answers": [
            {"text": "UCASE()", "is_correct": False},
            {"text": "UPPER()", "is_correct": True},
            {"text": "UPPERCASE()", "is_correct": False},
            {"text": "CAPS()", "is_correct": False},
        ],
    },
    {
        "text": "What does the TRIM() function do?",
        "explanation": "TRIM() removes leading and trailing whitespace (or specified characters) from a string.",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_trim.asp",
        "points": 1,
        "answers": [
            {"text": "Shortens string length", "is_correct": False},
            {"text": "Removes leading/trailing whitespace", "is_correct": True},
            {"text": "Splits strings", "is_correct": False},
            {"text": "Formats strings", "is_correct": False},
        ],
    },
    {
        "text": "Which function extracts a substring from a string?",
        "explanation": "SUBSTRING() function extracts a portion of a string starting from a specified position.",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_substring.asp",
        "points": 1,
        "answers": [
            {"text": "EXTRACT()", "is_correct": False},
            {"text": "SUBSTRING()", "is_correct": True},
            {"text": "SLICE()", "is_correct": False},
            {"text": "PART()", "is_correct": False},
        ],
    },
    {
        "text": "What is a stored procedure?",
        "explanation": "A stored procedure is a precompiled collection of SQL statements stored in the database that can be executed as a unit.",
        "reference": "https://www.w3schools.com/sql/sql_stored_procedures.asp",
        "points": 2,
        "answers": [
            {"text": "A saved query", "is_correct": False},
            {"text": "Precompiled SQL statements", "is_correct": True},
            {"text": "A database backup", "is_correct": False},
            {"text": "A data type", "is_correct": False},
        ],
    },
    {
        "text": "Which command creates a stored procedure?",
        "explanation": "CREATE PROCEDURE is used to create a new stored procedure in the database.",
        "reference": "https://www.w3schools.com/sql/sql_stored_procedures.asp",
        "points": 1,
        "answers": [
            {"text": "NEW PROCEDURE", "is_correct": False},
            {"text": "CREATE PROCEDURE", "is_correct": True},
            {"text": "ADD PROCEDURE", "is_correct": False},
            {"text": "MAKE PROCEDURE", "is_correct": False},
        ],
    },
    {
        "text": "What is a database trigger?",
        "explanation": "A trigger is a special type of stored procedure that automatically executes in response to database events.",
        "reference": "https://www.w3schools.com/sql/sql_triggers.asp",
        "points": 2,
        "answers": [
            {"text": "A scheduled task", "is_correct": False},
            {"text": "Auto-executing procedure", "is_correct": True},
            {"text": "A database constraint", "is_correct": False},
            {"text": "A user permission", "is_correct": False},
        ],
    },
    {
        "text": "Which events can activate a trigger?",
        "explanation": "Triggers can be activated by INSERT, UPDATE, DELETE operations on tables.",
        "reference": "https://www.w3schools.com/sql/sql_triggers.asp",
        "points": 1,
        "answers": [
            {"text": "SELECT operations", "is_correct": False},
            {"text": "INSERT, UPDATE, DELETE", "is_correct": True},
            {"text": "CREATE operations", "is_correct": False},
            {"text": "DROP operations", "is_correct": False},
        ],
    },
    {
        "text": "What is database normalization?",
        "explanation": "Normalization is the process of organizing data to reduce redundancy and improve data integrity.",
        "reference": "https://www.studytonight.com/dbms/database-normalization.php",
        "points": 2,
        "answers": [
            {"text": "Data compression", "is_correct": False},
            {"text": "Reducing redundancy", "is_correct": True},
            {"text": "Data encryption", "is_correct": False},
            {"text": "Performance optimization", "is_correct": False},
        ],
    },
    {
        "text": "What is First Normal Form (1NF)?",
        "explanation": "1NF requires that each table cell contains only atomic (indivisible) values and each record is unique.",
        "reference": "https://www.studytonight.com/dbms/first-normal-form.php",
        "points": 2,
        "answers": [
            {"text": "No duplicate rows", "is_correct": False},
            {"text": "Atomic values only", "is_correct": True},
            {"text": "No null values", "is_correct": False},
            {"text": "Primary key required", "is_correct": False},
        ],
    },
    {
        "text": "What characterizes Second Normal Form (2NF)?",
        "explanation": "2NF requires 1NF plus elimination of partial dependencies on composite primary keys.",
        "reference": "https://www.studytonight.com/dbms/second-normal-form.php",
        "points": 2,
        "answers": [
            {"text": "No transitive dependencies", "is_correct": False},
            {"text": "No partial dependencies", "is_correct": True},
            {"text": "No multivalued dependencies", "is_correct": False},
            {"text": "No join dependencies", "is_correct": False},
        ],
    },
    {
        "text": "What is Third Normal Form (3NF)?",
        "explanation": "3NF requires 2NF plus elimination of transitive dependencies between non-key attributes.",
        "reference": "https://www.studytonight.com/dbms/third-normal-form.php",
        "points": 2,
        "answers": [
            {"text": "No partial dependencies", "is_correct": False},
            {"text": "No transitive dependencies", "is_correct": True},
            {"text": "No multivalued dependencies", "is_correct": False},
            {"text": "All attributes are keys", "is_correct": False},
        ],
    },
    {
        "text": "What is denormalization?",
        "explanation": "Denormalization is the process of adding redundancy to improve performance by reducing the number of joins required.",
        "reference": "https://www.geeksforgeeks.org/denormalization-in-databases/",
        "points": 2,
        "answers": [
            {"text": "Removing all redundancy", "is_correct": False},
            {"text": "Adding redundancy for performance", "is_correct": True},
            {"text": "Creating more tables", "is_correct": False},
            {"text": "Encrypting data", "is_correct": False},
        ],
    },
    {
        "text": "Which SQL function returns the current date and time?",
        "explanation": "NOW() or CURRENT_TIMESTAMP returns the current date and time (varies by database system).",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_current_timestamp.asp",
        "points": 1,
        "answers": [
            {"text": "TODAY()", "is_correct": False},
            {"text": "NOW()", "is_correct": True},
            {"text": "DATETIME()", "is_correct": False},
            {"text": "TIME()", "is_correct": False},
        ],
    },
    {
        "text": "What does the DATEDIFF function calculate?",
        "explanation": "DATEDIFF calculates the difference between two dates, returning the result in specified units (days, months, years, etc.).",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_datediff.asp",
        "points": 1,
        "answers": [
            {"text": "Date formatting", "is_correct": False},
            {"text": "Difference between dates", "is_correct": True},
            {"text": "Date validation", "is_correct": False},
            {"text": "Date conversion", "is_correct": False},
        ],
    },
    {
        "text": "Which function extracts the year from a date?",
        "explanation": "YEAR() function extracts the year component from a date value.",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_year.asp",
        "points": 1,
        "answers": [
            {"text": "GET_YEAR()", "is_correct": False},
            {"text": "YEAR()", "is_correct": True},
            {"text": "EXTRACT_YEAR()", "is_correct": False},
            {"text": "YYYY()", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the HAVING clause?",
        "explanation": "HAVING filters groups created by GROUP BY, while WHERE filters individual rows before grouping.",
        "reference": "https://www.w3schools.com/sql/sql_having.asp",
        "points": 2,
        "answers": [
            {"text": "Filters individual rows", "is_correct": False},
            {"text": "Filters grouped results", "is_correct": True},
            {"text": "Sorts results", "is_correct": False},
            {"text": "Joins tables", "is_correct": False},
        ],
    },
    {
        "text": "Which operator tests for NULL values?",
        "explanation": "IS NULL and IS NOT NULL are the correct operators for testing NULL values; = NULL doesn't work.",
        "reference": "https://www.w3schools.com/sql/sql_null_values.asp",
        "points": 1,
        "answers": [
            {"text": "= NULL", "is_correct": False},
            {"text": "IS NULL", "is_correct": True},
            {"text": "== NULL", "is_correct": False},
            {"text": "NULL()", "is_correct": False},
        ],
    },
    {
        "text": "What does the ISNULL function do?",
        "explanation": "ISNULL replaces NULL values with a specified replacement value.",
        "reference": "https://www.w3schools.com/sql/func_sqlserver_isnull.asp",
        "points": 1,
        "answers": [
            {"text": "Tests for NULL", "is_correct": False},
            {"text": "Replaces NULL values", "is_correct": True},
            {"text": "Counts NULL values", "is_correct": False},
            {"text": "Removes NULL values", "is_correct": False},
        ],
    },
    {
        "text": "Which statement creates a database view?",
        "explanation": "CREATE VIEW statement creates a virtual table based on the result of a SELECT statement.",
        "reference": "https://www.w3schools.com/sql/sql_view.asp",
        "points": 1,
        "answers": [
            {"text": "NEW VIEW", "is_correct": False},
            {"text": "CREATE VIEW", "is_correct": True},
            {"text": "MAKE VIEW", "is_correct": False},
            {"text": "ADD VIEW", "is_correct": False},
        ],
    },
    {
        "text": "What is a materialized view?",
        "explanation": "A materialized view is a physical copy of data that is stored and periodically refreshed from the base tables.",
        "reference": "https://www.postgresql.org/docs/current/rules-materializedviews.html",
        "points": 2,
        "answers": [
            {"text": "A virtual table", "is_correct": False},
            {"text": "Physical copy of data", "is_correct": True},
            {"text": "A temporary table", "is_correct": False},
            {"text": "A system table", "is_correct": False},
        ],
    },
    {
        "text": "Which command removes a table from the database?",
        "explanation": "DROP TABLE permanently removes a table and all its data from the database.",
        "reference": "https://www.w3schools.com/sql/sql_drop_table.asp",
        "points": 1,
        "answers": [
            {"text": "DELETE TABLE", "is_correct": False},
            {"text": "DROP TABLE", "is_correct": True},
            {"text": "REMOVE TABLE", "is_correct": False},
            {"text": "DESTROY TABLE", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between TRUNCATE and DELETE?",
        "explanation": "TRUNCATE removes all rows quickly and resets identity columns, while DELETE can use WHERE clauses and is slower.",
        "reference": "https://www.geeksforgeeks.org/difference-between-delete-drop-and-truncate/",
        "points": 2,
        "answers": [
            {"text": "TRUNCATE is faster and resets identity", "is_correct": True},
            {"text": "DELETE is faster", "is_correct": False},
            {"text": "They are identical", "is_correct": False},
            {"text": "TRUNCATE can use WHERE", "is_correct": False},
        ],
    },
    {
        "text": "What does the MERGE statement do?",
        "explanation": "MERGE performs INSERT, UPDATE, or DELETE operations in a single statement based on matching conditions.",
        "reference": "https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql",
        "points": 2,
        "answers": [
            {"text": "Combines multiple tables", "is_correct": False},
            {"text": "Performs conditional INSERT/UPDATE/DELETE", "is_correct": True},
            {"text": "Merges databases", "is_correct": False},
            {"text": "Joins tables", "is_correct": False},
        ],
    },
    {
        "text": "Which isolation level prevents dirty reads?",
        "explanation": "READ COMMITTED isolation level prevents dirty reads by ensuring only committed data is read.",
        "reference": "https://docs.microsoft.com/en-us/sql/odbc/reference/develop-app/transaction-isolation-levels",
        "points": 2,
        "answers": [
            {"text": "READ UNCOMMITTED", "is_correct": False},
            {"text": "READ COMMITTED", "is_correct": True},
            {"text": "REPEATABLE READ", "is_correct": False},
            {"text": "SERIALIZABLE", "is_correct": False},
        ],
    },
    {
        "text": "What is a deadlock in database systems?",
        "explanation": "A deadlock occurs when two or more transactions wait indefinitely for each other to release locks.",
        "reference": "https://www.geeksforgeeks.org/deadlock-in-dbms/",
        "points": 2,
        "answers": [
            {"text": "System crash", "is_correct": False},
            {"text": "Transactions waiting for each other", "is_correct": True},
            {"text": "Memory overflow", "is_correct": False},
            {"text": "Network timeout", "is_correct": False},
        ],
    },
    {
        "text": "Which command starts a database transaction?",
        "explanation": "BEGIN TRANSACTION (or BEGIN) starts a new database transaction.",
        "reference": "https://www.w3schools.com/sql/sql_transaction.asp",
        "points": 1,
        "answers": [
            {"text": "START TRANSACTION", "is_correct": False},
            {"text": "BEGIN TRANSACTION", "is_correct": True},
            {"text": "OPEN TRANSACTION", "is_correct": False},
            {"text": "NEW TRANSACTION", "is_correct": False},
        ],
    },
    {
        "text": "What does ROLLBACK do in a transaction?",
        "explanation": "ROLLBACK undoes all changes made in the current transaction and returns the database to its previous state.",
        "reference": "https://www.w3schools.com/sql/sql_transaction.asp",
        "points": 1,
        "answers": [
            {"text": "Saves changes permanently", "is_correct": False},
            {"text": "Undoes transaction changes", "is_correct": True},
            {"text": "Pauses the transaction", "is_correct": False},
            {"text": "Restarts the transaction", "is_correct": False},
        ],
    },
]