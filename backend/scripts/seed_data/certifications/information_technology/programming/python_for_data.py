"""Python for Data Engineering Certification"""

CERTIFICATION = {
    "name": "Python for Data Engineering",
    "description": "Python Data Engineering Professional Certificate",
    "slug": "python-for-data",
    "level": "Professional",
    "duration": 90,
    "questions_count": 50,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": """## Pandas DataFrame Operations

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = df.sum().sum()
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Pandas DataFrame Aggregation

DataFrames support hierarchical aggregation operations for data analysis.

## Code Analysis:
1. Create DataFrame with columns A and B
2. `df.sum()` sums each column: A=6, B=15
3. Second `.sum()` sums the column totals: 6 + 15 = 21

## DataFrame Aggregation Examples:
```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(df.sum())      # Series: A=6, B=15
print(df.sum().sum()) # Scalar: 21
print(df.mean())     # Series: A=2, B=5
print(df.std())      # Standard deviation per column
```

Essential for data summarization and analysis.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html",
        "points": 2,
        "answers": [
            {"text": "21", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "15", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "Which method is used to handle missing values in a pandas DataFrame?",
        "explanation": """# Missing Data Handling in Pandas

Pandas provides several methods to detect and handle missing data effectively.

## Main Methods:
- `dropna()` - Remove rows/columns with missing values
- `fillna()` - Fill missing values with specified data
- `isna()` - Detect missing values (returns boolean)
- `notna()` - Detect non-missing values

## Examples:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})

# Remove rows with any missing values
df.dropna()

# Fill missing values
df.fillna(0)                    # Fill with 0
df.fillna({'A': 0, 'B': -1})   # Different values per column
df.fillna(method='ffill')       # Forward fill
df.fillna(method='bfill')       # Backward fill

# Check for missing values
df.isna()      # Boolean DataFrame
df.isna().sum() # Count missing per column
```

Critical for data cleaning and preprocessing.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html",
        "points": 2,
        "answers": [
            {"text": "dropna() and fillna()", "is_correct": True},
            {"text": "remove_na()", "is_correct": False},
            {"text": "clean_data()", "is_correct": False},
            {"text": "handle_missing()", "is_correct": False},
        ],
    },
    {
        "text": """## NumPy Array Operations

**What is the output of the following code?**

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
result = np.sum(arr, axis=1)
print(result)
```

*Choose the correct output:*""",
        "explanation": """# NumPy Array Axis Operations

Understanding axis parameters is crucial for array operations in data analysis.

## Axis Explanation:
- `axis=0`: Operations along rows (column-wise)
- `axis=1`: Operations along columns (row-wise)
- `axis=None`: Operations on flattened array

## Code Analysis:
```python
arr = np.array([[1, 2], 
                [3, 4]])
# axis=1 sums along columns (each row)
# Row 0: 1 + 2 = 3
# Row 1: 3 + 4 = 7
# Result: [3, 7]
```

## Common Axis Operations:
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.sum(axis=0))    # [5, 7, 9] - column sums
print(arr.sum(axis=1))    # [6, 15] - row sums
print(arr.mean(axis=1))   # [2., 5.] - row means
```

Essential for data aggregation and statistical analysis.""",
        "reference": "https://numpy.org/doc/stable/reference/generated/numpy.sum.html",
        "points": 2,
        "answers": [
            {"text": "[3 7]", "is_correct": True},
            {"text": "[4 6]", "is_correct": False},
            {"text": "10", "is_correct": False},
            {"text": "[[1 2] [3 4]]", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between pandas Series and DataFrame?",
        "explanation": """# Pandas Data Structures: Series vs DataFrame

Understanding the fundamental data structures is key to effective data analysis.

## Series:
- One-dimensional labeled array
- Can hold any data type
- Has an index
- Similar to a column in a spreadsheet

## DataFrame:
- Two-dimensional labeled data structure
- Collection of Series with shared index
- Similar to a spreadsheet or SQL table

## Examples:
```python
import pandas as pd

# Series - 1D
series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(type(series))  # <class 'pandas.core.series.Series'>

# DataFrame - 2D
df = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [4, 5, 6]
})
print(type(df))      # <class 'pandas.core.frame.DataFrame'>

# Converting between them
series_from_df = df['col1']    # Extract Series from DataFrame
df_from_series = series.to_frame()  # Convert Series to DataFrame
```

DataFrames are collections of Series sharing the same index.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html",
        "points": 1,
        "answers": [
            {"text": "Series is 1D, DataFrame is 2D", "is_correct": True},
            {"text": "Series is faster than DataFrame", "is_correct": False},
            {"text": "DataFrame cannot have missing values", "is_correct": False},
            {"text": "No difference", "is_correct": False},
        ],
    },
    {
        "text": "Which library is commonly used for data visualization in Python?",
        "explanation": """# Python Data Visualization Libraries

Multiple powerful libraries exist for creating visualizations from data.

## Major Libraries:

### Matplotlib
- Low-level plotting library
- Foundation for other libraries
- Highly customizable

### Seaborn
- High-level statistical visualization
- Built on matplotlib
- Beautiful default styles

### Plotly
- Interactive visualizations
- Web-based plotting
- Great for dashboards

### Bokeh
- Interactive visualizations
- Large dataset handling
- Web applications

## Examples:
```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Matplotlib
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Seaborn
sns.scatterplot(data=df, x='col1', y='col2')

# Plotly
fig = px.scatter(df, x='col1', y='col2')
fig.show()
```

Choose based on your needs: static (matplotlib/seaborn) or interactive (plotly/bokeh).""",
        "reference": "https://matplotlib.org/stable/tutorials/introductory/pyplot.html",
        "points": 1,
        "answers": [
            {"text": "Matplotlib, Seaborn, Plotly", "is_correct": True},
            {"text": "NumPy", "is_correct": False},
            {"text": "Pandas only", "is_correct": False},
            {"text": "TensorFlow", "is_correct": False},
        ],
    },
    {
        "text": """## DataFrame Filtering

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 
                   'age': [25, 30, 35]})
result = df[df['age'] > 28]
print(len(result))
```

*Choose the correct output:*""",
        "explanation": """# DataFrame Boolean Indexing

Boolean indexing allows filtering DataFrames based on conditions.

## Code Analysis:
1. Create DataFrame with names and ages
2. `df['age'] > 28` creates boolean Series: [False, True, True]
3. `df[boolean_series]` filters rows where condition is True
4. Bob (30) and Charlie (35) meet the condition
5. `len(result)` returns number of filtered rows: 2

## Boolean Indexing Examples:
```python
# Single condition
adults = df[df['age'] >= 18]

# Multiple conditions
young_adults = df[(df['age'] >= 18) & (df['age'] <= 30)]

# String conditions
names_with_a = df[df['name'].str.contains('a')]

# Using isin()
specific_ages = df[df['age'].isin([25, 35])]
```

Parentheses are important for multiple conditions due to operator precedence.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing",
        "points": 2,
        "answers": [
            {"text": "2", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "1", "is_correct": False},
            {"text": "0", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the GroupBy operation in pandas?",
        "explanation": """# Pandas GroupBy Operations

GroupBy enables split-apply-combine operations for data analysis.

## GroupBy Process:
1. **Split**: Divide data into groups based on criteria
2. **Apply**: Perform operation on each group
3. **Combine**: Merge results into final output

## Examples:
```python
import pandas as pd

df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B'],
    'value': [1, 2, 3, 4]
})

# Basic groupby
grouped = df.groupby('category')['value'].sum()
# Result: category A=3, B=7

# Multiple aggregations
result = df.groupby('category').agg({
    'value': ['sum', 'mean', 'count']
})

# Transform operations
df['value_normalized'] = df.groupby('category')['value'].transform(
    lambda x: x / x.mean()
)

# Custom functions
def custom_agg(group):
    return group.max() - group.min()

df.groupby('category')['value'].apply(custom_agg)
```

Essential for data summarization and aggregation.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html",
        "points": 2,
        "answers": [
            {"text": "Split-apply-combine operations for data aggregation", "is_correct": True},
            {"text": "Sort data alphabetically", "is_correct": False},
            {"text": "Create new columns", "is_correct": False},
            {"text": "Remove duplicates", "is_correct": False},
        ],
    },
    {
        "text": """## Data Merging

**What is the output of the following code?**

```python
import pandas as pd
df1 = pd.DataFrame({'key': ['A', 'B'], 'value1': [1, 2]})
df2 = pd.DataFrame({'key': ['A', 'C'], 'value2': [3, 4]})
result = pd.merge(df1, df2, on='key', how='inner')
print(len(result))
```

*Choose the correct output:*""",
        "explanation": """# Pandas DataFrame Merging

Merging combines DataFrames based on common columns or indices.

## Merge Types:
- `inner`: Keep only matching records (intersection)
- `left`: Keep all records from left DataFrame
- `right`: Keep all records from right DataFrame
- `outer`: Keep all records from both DataFrames (union)

## Code Analysis:
```python
df1: key=['A', 'B'], value1=[1, 2]
df2: key=['A', 'C'], value2=[3, 4]

# Inner merge on 'key'
# Only 'A' exists in both DataFrames
# Result: one row with key='A', value1=1, value2=3
```

## Merge Examples:
```python
# Different join types
inner_result = pd.merge(df1, df2, on='key', how='inner')   # 1 row
left_result = pd.merge(df1, df2, on='key', how='left')     # 2 rows
outer_result = pd.merge(df1, df2, on='key', how='outer')   # 3 rows

# Multiple keys
df.merge(other_df, on=['key1', 'key2'])

# Different column names
df.merge(other_df, left_on='id', right_on='user_id')
```

Similar to SQL JOIN operations.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html",
        "points": 2,
        "answers": [
            {"text": "1", "is_correct": True},
            {"text": "2", "is_correct": False},
            {"text": "3", "is_correct": False},
            {"text": "0", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between loc and iloc in pandas?",
        "explanation": """# Pandas Indexing: loc vs iloc

Understanding indexing methods is crucial for data manipulation.

## loc - Label-based indexing:
- Uses row and column labels
- Includes both endpoints in slicing
- Can use boolean arrays

## iloc - Integer position-based indexing:
- Uses integer positions
- Excludes right endpoint in slicing (like Python lists)
- Zero-based indexing

## Examples:
```python
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# loc - label-based
print(df.loc['x', 'A'])        # 1
print(df.loc['x':'y', 'A'])    # Includes both x and y
print(df.loc[df['A'] > 1])     # Boolean indexing

# iloc - position-based
print(df.iloc[0, 0])           # 1 (first row, first column)
print(df.iloc[0:2, 0])         # Excludes row 2
print(df.iloc[-1, :])          # Last row, all columns
```

Use loc for labels, iloc for positions.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html",
        "points": 2,
        "answers": [
            {"text": "loc uses labels, iloc uses integer positions", "is_correct": True},
            {"text": "iloc is faster than loc", "is_correct": False},
            {"text": "loc is for columns, iloc is for rows", "is_correct": False},
            {"text": "No difference", "is_correct": False},
        ],
    },
    {
        "text": """## NumPy Broadcasting

**What is the output of the following code?**

```python
import numpy as np
a = np.array([[1], [2], [3]])
b = np.array([10, 20])
result = a + b
print(result.shape)
```

*Choose the correct output:*""",
        "explanation": """# NumPy Broadcasting

Broadcasting allows operations between arrays of different shapes without explicit reshaping.

## Code Analysis:
```python
a.shape = (3, 1)  # 3 rows, 1 column
b.shape = (2,)    # 1D array with 2 elements

# Broadcasting rules:
# a: (3, 1) 
# b: (2,) becomes (1, 2) conceptually
# Result: (3, 2)
```

## Broadcasting Result:
```
a = [[1],     b = [10, 20]
     [2],
     [3]]

result = [[1+10, 1+20],    = [[11, 21],
          [2+10, 2+20],      [12, 22],
          [3+10, 3+20]]      [13, 23]]
```

## Broadcasting Rules:
1. Arrays are aligned from the rightmost dimension
2. Dimensions of size 1 can be stretched
3. Missing dimensions are assumed to be 1

Shape: (3, 2)""",
        "reference": "https://numpy.org/doc/stable/user/basics.broadcasting.html",
        "points": 2,
        "answers": [
            {"text": "(3, 2)", "is_correct": True},
            {"text": "(3, 1)", "is_correct": False},
            {"text": "(2,)", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of data normalization in data engineering?",
        "explanation": """# Data Normalization in Data Engineering

Normalization scales data to a common range, improving analysis and model performance.

## Why Normalize?
1. **Different scales**: Features might have vastly different ranges
2. **Algorithm sensitivity**: Many ML algorithms are sensitive to scale
3. **Convergence**: Helps optimization algorithms converge faster
4. **Comparison**: Makes features comparable

## Common Normalization Techniques:

### Min-Max Scaling
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
normalized = scaler.fit_transform(data)
# Result: values between 0 and 1
```

### Z-Score Normalization
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
normalized = scaler.fit_transform(data)
# Result: mean=0, std=1
```

### Manual Normalization
```python
# Min-Max manually
normalized = (data - data.min()) / (data.max() - data.min())

# Z-score manually  
normalized = (data - data.mean()) / data.std()
```

Essential for machine learning and statistical analysis.""",
        "reference": "https://scikit-learn.org/stable/modules/preprocessing.html",
        "points": 2,
        "answers": [
            {"text": "Scale data to a common range for better analysis", "is_correct": True},
            {"text": "Remove duplicate data", "is_correct": False},
            {"text": "Sort data alphabetically", "is_correct": False},
            {"text": "Convert data types", "is_correct": False},
        ],
    },
    {
        "text": """## Data Cleaning

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6]})
result = df.drop_duplicates()
print(len(result))
```

*Choose the correct output:*""",
        "explanation": """# Pandas Duplicate Removal

`drop_duplicates()` removes duplicate rows based on all or specified columns.

## Code Analysis:
```python
Original DataFrame:
   A  B
0  1  4
1  2  5
2  2  5  # Duplicate of row 1
3  3  6

After drop_duplicates():
   A  B
0  1  4
1  2  5  # Row 2 removed (duplicate)
3  3  6
```

Result has 3 rows (one duplicate removed).

## Drop Duplicates Options:
```python
# Remove duplicates based on all columns
df.drop_duplicates()

# Remove based on specific columns
df.drop_duplicates(subset=['A'])

# Keep last occurrence instead of first
df.drop_duplicates(keep='last')

# Keep all duplicates (mark for removal)
df.drop_duplicates(keep=False)

# Check for duplicates
df.duplicated()  # Boolean Series
df.duplicated().sum()  # Count duplicates
```

Critical for data cleaning and quality assurance.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html",
        "points": 2,
        "answers": [
            {"text": "3", "is_correct": True},
            {"text": "4", "is_correct": False},
            {"text": "2", "is_correct": False},
            {"text": "1", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between wide and long format data?",
        "explanation": """# Data Format: Wide vs Long

Understanding data formats is crucial for analysis and visualization.

## Wide Format:
- Each variable has its own column
- Each observation has its own row
- More readable for humans
- Common in spreadsheets

## Long Format:
- Variables are in rows, not columns
- More normalized structure
- Better for analysis and visualization
- Preferred by many plotting libraries

## Examples:

### Wide Format:
```
Name    Math  Science  English
Alice   85    90       88
Bob     92    85       90
```

### Long Format:
```
Name    Subject   Score
Alice   Math      85
Alice   Science   90
Alice   English   88
Bob     Math      92
Bob     Science   85
Bob     English   90
```

## Pandas Conversion:
```python
# Wide to Long
long_df = wide_df.melt(id_vars=['Name'], 
                       value_vars=['Math', 'Science', 'English'],
                       var_name='Subject', 
                       value_name='Score')

# Long to Wide
wide_df = long_df.pivot(index='Name', 
                        columns='Subject', 
                        values='Score')
```

Choose format based on your analysis needs.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html",
        "points": 2,
        "answers": [
            {"text": "Wide has variables as columns, long has variables as rows", "is_correct": True},
            {"text": "Wide format is always better", "is_correct": False},
            {"text": "Long format takes more memory", "is_correct": False},
            {"text": "No practical difference", "is_correct": False},
        ],
    },
    {
        "text": """## Data Type Conversion

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({'A': ['1', '2', '3'], 'B': ['4.5', '5.5', '6.5']})
df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)
print(df.dtypes['A'])
```

*Choose the correct output:*""",
        "explanation": """# Pandas Data Type Conversion

Converting data types is essential for proper analysis and memory efficiency.

## Code Analysis:
1. Create DataFrame with string columns
2. Convert column 'A' from string to integer using `astype(int)`
3. Convert column 'B' from string to float using `astype(float)`
4. `df.dtypes['A']` returns the data type of column 'A': int64

## Data Type Conversion Methods:
```python
# Using astype()
df['col'] = df['col'].astype(int)
df['col'] = df['col'].astype('float32')

# Using to_numeric() - safer, handles errors
df['col'] = pd.to_numeric(df['col'], errors='coerce')

# Using to_datetime()
df['date'] = pd.to_datetime(df['date_string'])

# Check data types
print(df.dtypes)
print(df.info())

# Memory usage optimization
df['category_col'] = df['category_col'].astype('category')
```

Proper data types improve performance and prevent errors.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html",
        "points": 2,
        "answers": [
            {"text": "int64", "is_correct": True},
            {"text": "object", "is_correct": False},
            {"text": "float64", "is_correct": False},
            {"text": "string", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of indexing in pandas DataFrames?",
        "explanation": """# Pandas DataFrame Indexing

Indexes provide fast data access, alignment, and meaningful labels for data.

## Benefits of Indexing:
1. **Fast data access**: O(1) lookup time
2. **Data alignment**: Automatic alignment in operations
3. **Meaningful labels**: Human-readable row identifiers
4. **Time series support**: DatetimeIndex for time-based data

## Index Types:
- **RangeIndex**: Default integer index (0, 1, 2, ...)
- **Index**: Custom labels
- **DatetimeIndex**: Time-based index
- **MultiIndex**: Hierarchical indexing

## Examples:
```python
import pandas as pd

# Setting custom index
df = pd.DataFrame({'value': [1, 2, 3]}, 
                  index=['A', 'B', 'C'])

# Setting index from column
df.set_index('column_name', inplace=True)

# Resetting index
df.reset_index(inplace=True)

# MultiIndex
df.set_index(['col1', 'col2'], inplace=True)

# DatetimeIndex
dates = pd.date_range('2023-01-01', periods=3)
df = pd.DataFrame({'value': [1, 2, 3]}, index=dates)

# Fast access
result = df.loc['A']  # Much faster with proper index
```

Indexes are the foundation of efficient pandas operations.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html",
        "points": 1,
        "answers": [
            {"text": "Fast data access and automatic alignment", "is_correct": True},
            {"text": "Sort data automatically", "is_correct": False},
            {"text": "Store data types", "is_correct": False},
            {"text": "Handle missing values", "is_correct": False},
        ],
    },
    {
        "text": """## Data Aggregation

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B'],
    'value': [10, 20, 30, 40]
})
result = df.groupby('category')['value'].agg(['sum', 'mean'])
print(result.iloc[0, 0])
```

*Choose the correct output:*""",
        "explanation": """# Pandas Aggregation with Multiple Functions

`agg()` allows applying multiple functions to grouped data.

## Code Analysis:
1. GroupBy 'category': A group=[10, 20], B group=[30, 40]
2. Apply 'sum' and 'mean' to each group's 'value' column
3. Result is DataFrame with MultiColumn: ('sum', 'mean')
4. `iloc[0, 0]` gets first row, first column (A group's sum)

## Result Structure:
```
         sum  mean
category           
A         30  15.0
B         70  35.0
```

`result.iloc[0, 0]` = 30 (sum of A group: 10 + 20)

## Aggregation Examples:
```python
# Single function
df.groupby('category')['value'].sum()

# Multiple functions
df.groupby('category')['value'].agg(['sum', 'mean', 'count'])

# Different functions for different columns
df.groupby('category').agg({
    'value1': 'sum',
    'value2': ['mean', 'std']
})

# Custom functions
df.groupby('category')['value'].agg(lambda x: x.max() - x.min())
```

Powerful for data summarization and reporting.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html",
        "points": 2,
        "answers": [
            {"text": "30", "is_correct": True},
            {"text": "15.0", "is_correct": False},
            {"text": "70", "is_correct": False},
            {"text": "35.0", "is_correct": False},
        ],
    },
    {
        "text": "What is ETL in data engineering?",
        "explanation": """# ETL: Extract, Transform, Load

ETL is a fundamental data integration process in data engineering.

## ETL Components:

### Extract
- Retrieve data from various sources
- APIs, databases, files, web scraping
- Handle different formats (JSON, CSV, XML, etc.)

### Transform
- Clean and standardize data
- Apply business rules
- Data validation and quality checks
- Aggregations and calculations

### Load
- Store processed data in target system
- Data warehouse, database, data lake
- Ensure data integrity and performance

## Python ETL Example:
```python
import pandas as pd
import requests

# EXTRACT
def extract_data():
    # From API
    response = requests.get('https://api.example.com/data')
    api_data = response.json()
    
    # From file
    file_data = pd.read_csv('data.csv')
    
    return api_data, file_data

# TRANSFORM
def transform_data(data):
    df = pd.DataFrame(data)
    
    # Clean data
    df = df.dropna()
    df['email'] = df['email'].str.lower()
    
    # Apply business rules
    df['age_group'] = df['age'].apply(lambda x: 'adult' if x >= 18 else 'minor')
    
    return df

# LOAD
def load_data(df):
    # To database
    df.to_sql('users', connection, if_exists='append')
    
    # To file
    df.to_parquet('processed_data.parquet')
```

Foundation of modern data pipelines.""",
        "reference": "https://en.wikipedia.org/wiki/Extract,_transform,_load",
        "points": 2,
        "answers": [
            {"text": "Extract, Transform, Load data processing", "is_correct": True},
            {"text": "Error, Test, Log operations", "is_correct": False},
            {"text": "Encrypt, Transfer, Lock data", "is_correct": False},
            {"text": "Export, Translate, Link files", "is_correct": False},
        ],
    },
    {
        "text": """## DataFrame Concatenation

**What is the output of the following code?**

```python
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})
result = pd.concat([df1, df2], ignore_index=True)
print(result.shape)
```

*Choose the correct output:*""",
        "explanation": """# Pandas Concatenation

`concat()` combines DataFrames along a particular axis.

## Code Analysis:
```python
df1:     df2:     
   A        A     
0  1     0  3     
1  2     1  4     

# concat with ignore_index=True
result:
   A
0  1
1  2  
2  3
3  4
```

Shape: (4, 1) - 4 rows, 1 column

## Concatenation Options:
```python
# Vertical concatenation (default)
pd.concat([df1, df2])                # Keep original indexes
pd.concat([df1, df2], ignore_index=True)  # Reset index

# Horizontal concatenation
pd.concat([df1, df2], axis=1)

# Handle missing columns
df3 = pd.DataFrame({'B': [5, 6]})
pd.concat([df1, df3])  # Creates NaN for missing values

# Add keys for identification
pd.concat([df1, df2], keys=['first', 'second'])
```

Essential for combining data from multiple sources.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html",
        "points": 2,
        "answers": [
            {"text": "(4, 1)", "is_correct": True},
            {"text": "(2, 1)", "is_correct": False},
            {"text": "(2, 2)", "is_correct": False},
            {"text": "(1, 4)", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of data validation in data engineering?",
        "explanation": """# Data Validation in Data Engineering

Data validation ensures data quality, accuracy, and reliability in pipelines.

## Why Validate Data?
1. **Data Quality**: Ensure accuracy and consistency
2. **Business Rules**: Enforce domain-specific constraints
3. **Error Prevention**: Catch issues early in pipeline
4. **Compliance**: Meet regulatory requirements
5. **Debugging**: Identify data source problems

## Validation Types:

### Schema Validation
```python
import pandas as pd
from pandas.api.types import is_numeric_dtype

def validate_schema(df, expected_columns):
    # Check column presence
    missing_cols = set(expected_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    # Check data types
    if not is_numeric_dtype(df['age']):
        raise TypeError("Age column must be numeric")
```

### Business Rule Validation
```python
def validate_business_rules(df):
    # Age validation
    if (df['age'] < 0).any() or (df['age'] > 150).any():
        raise ValueError("Invalid age values")
    
    # Email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not df['email'].str.match(email_pattern).all():
        raise ValueError("Invalid email format")
```

### Statistical Validation
```python
def validate_statistics(df):
    # Check for outliers
    Q1 = df['salary'].quantile(0.25)
    Q3 = df['salary'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df['salary'] < Q1 - 1.5*IQR) | 
                  (df['salary'] > Q3 + 1.5*IQR)]
    
    if len(outliers) > len(df) * 0.05:  # More than 5% outliers
        print(f"Warning: {len(outliers)} potential outliers detected")
```

Critical for maintaining data pipeline reliability.""",
        "reference": "https://en.wikipedia.org/wiki/Data_validation",
        "points": 2,
        "answers": [
            {"text": "Ensure data quality and enforce business rules", "is_correct": True},
            {"text": "Compress data for storage", "is_correct": False},
            {"text": "Encrypt sensitive information", "is_correct": False},
            {"text": "Sort data alphabetically", "is_correct": False},
        ],
    },
    {
        "text": """## Data Pivot Operations

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({
    'name': ['Alice', 'Alice', 'Bob', 'Bob'],
    'subject': ['Math', 'Science', 'Math', 'Science'],
    'score': [85, 90, 92, 88]
})
result = df.pivot(index='name', columns='subject', values='score')
print(result.shape)
```

*Choose the correct output:*""",
        "explanation": """# Pandas Pivot Operations

`pivot()` reshapes data from long to wide format based on column values.

## Code Analysis:
Original data (long format):
```
    name  subject  score
0  Alice     Math     85
1  Alice  Science     90
2    Bob     Math     92
3    Bob  Science     88
```

After pivot (wide format):
```
subject  Math  Science
name              
Alice      85       90
Bob        92       88
```

Shape: (2, 2) - 2 rows (names), 2 columns (subjects)

## Pivot vs Other Reshape Operations:
```python
# pivot() - simple reshape, requires unique combinations
df.pivot(index='name', columns='subject', values='score')

# pivot_table() - handles duplicate combinations with aggregation
df.pivot_table(index='name', columns='subject', 
               values='score', aggfunc='mean')

# melt() - opposite of pivot (wide to long)
wide_df.melt(id_vars=['name'], 
             value_vars=['Math', 'Science'])
```

Essential for data analysis and reporting.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html",
        "points": 2,
        "answers": [
            {"text": "(2, 2)", "is_correct": True},
            {"text": "(4, 3)", "is_correct": False},
            {"text": "(2, 3)", "is_correct": False},
            {"text": "(4, 2)", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between SQL and NoSQL databases in data engineering?",
        "explanation": """# SQL vs NoSQL Databases

Understanding database types is crucial for choosing the right storage solution.

## SQL Databases (Relational):

### Characteristics:
- Structured data with fixed schema
- ACID properties (Atomicity, Consistency, Isolation, Durability)
- SQL query language
- Vertical scaling

### Examples:
- PostgreSQL, MySQL, SQL Server, Oracle

### Use Cases:
- Financial transactions
- Complex queries and joins
- Data integrity is critical

## NoSQL Databases (Non-relational):

### Types:
1. **Document**: MongoDB, CouchDB
2. **Key-Value**: Redis, DynamoDB
3. **Column-family**: Cassandra, HBase
4. **Graph**: Neo4j, Amazon Neptune

### Characteristics:
- Flexible schema
- Horizontal scaling
- Eventually consistent
- Various data models

## Python Examples:

### SQL (PostgreSQL):
```python
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="user",
    password="password"
)

df = pd.read_sql("SELECT * FROM users", conn)
```

### NoSQL (MongoDB):
```python
from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['users']

# Insert document
collection.insert_one({'name': 'Alice', 'age': 25})

# Query and convert to DataFrame
cursor = collection.find()
df = pd.DataFrame(list(cursor))
```

Choose based on data structure, scalability, and consistency needs.""",
        "reference": "https://en.wikipedia.org/wiki/NoSQL",
        "points": 2,
        "answers": [
            {"text": "SQL has fixed schema, NoSQL has flexible schema", "is_correct": True},
            {"text": "SQL is always faster than NoSQL", "is_correct": False},
            {"text": "NoSQL cannot handle complex queries", "is_correct": False},
            {"text": "SQL databases are only for small data", "is_correct": False},
        ],
    },
    {
        "text": """## Time Series Data

**What is the output of the following code?**

```python
import pandas as pd
dates = pd.date_range('2023-01-01', periods=3, freq='D')
df = pd.DataFrame({'value': [10, 20, 30]}, index=dates)
result = df.resample('M').sum()
print(len(result))
```

*Choose the correct output:*""",
        "explanation": """# Pandas Time Series Resampling

`resample()` changes the frequency of time series data with aggregation.

## Code Analysis:
```python
Original data (daily frequency):
2023-01-01    10
2023-01-02    20  
2023-01-03    30

# resample('M') - Monthly frequency with sum()
# All dates are in January 2023, so one month total
Result:
2023-01-31    60  # Sum of all January values
```

Length: 1 (one month)

## Resampling Examples:
```python
# Different frequencies
df.resample('W').mean()    # Weekly mean
df.resample('H').ffill()   # Hourly with forward fill
df.resample('Q').sum()     # Quarterly sum

# Multiple aggregations
df.resample('M').agg(['sum', 'mean', 'count'])

# Upsampling (increase frequency)
daily_data.resample('H').interpolate()

# Downsampling (decrease frequency)  
hourly_data.resample('D').mean()
```

## Common Frequency Aliases:
- 'D': Daily
- 'W': Weekly  
- 'M': Monthly
- 'Q': Quarterly
- 'A': Annual
- 'H': Hourly

Essential for time series analysis and forecasting.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html",
        "points": 2,
        "answers": [
            {"text": "1", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "12", "is_correct": False},
            {"text": "31", "is_correct": False},
        ],
    },
    {
        "text": "What is data partitioning and why is it important?",
        "explanation": """# Data Partitioning in Data Engineering

Partitioning divides large datasets into smaller, manageable chunks for better performance.

## Benefits of Partitioning:
1. **Query Performance**: Only scan relevant partitions
2. **Parallel Processing**: Process partitions concurrently
3. **Maintenance**: Easier backup, archival, and updates
4. **Scalability**: Handle larger datasets efficiently
5. **Cost Optimization**: Store older partitions in cheaper storage

## Partitioning Strategies:

### Range Partitioning
```python
# Partition by date ranges
partition_by_date = {
    '2023-Q1': df[(df['date'] >= '2023-01-01') & (df['date'] < '2023-04-01')],
    '2023-Q2': df[(df['date'] >= '2023-04-01') & (df['date'] < '2023-07-01')],
}
```

### Hash Partitioning
```python
# Partition by hash of customer ID
import hashlib

def get_partition(customer_id, num_partitions=4):
    hash_value = int(hashlib.md5(str(customer_id).encode()).hexdigest(), 16)
    return hash_value % num_partitions

df['partition'] = df['customer_id'].apply(lambda x: get_partition(x))
```

### List Partitioning
```python
# Partition by discrete values
partitions = {
    'North': df[df['region'].isin(['NY', 'MA', 'VT'])],
    'South': df[df['region'].isin(['FL', 'GA', 'TX'])],
    'West': df[df['region'].isin(['CA', 'WA', 'OR'])]
}
```

## File-based Partitioning:
```python
# Parquet partitioning
df.to_parquet('/data/partitioned/', 
               partition_cols=['year', 'month'])

# Results in structure:
# /data/partitioned/year=2023/month=01/file.parquet
# /data/partitioned/year=2023/month=02/file.parquet
```

Critical for big data processing and analytics.""",
        "reference": "https://en.wikipedia.org/wiki/Partition_(database)",
        "points": 2,
        "answers": [
            {"text": "Dividing large datasets for better performance", "is_correct": True},
            {"text": "Encrypting data for security", "is_correct": False},
            {"text": "Compressing data to save space", "is_correct": False},
            {"text": "Converting data formats", "is_correct": False},
        ],
    },
    {
        "text": """## Data Sampling

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({'value': range(100)})
sample = df.sample(n=5, random_state=42)
print(len(sample))
```

*Choose the correct output:*""",
        "explanation": """# Pandas Data Sampling

`sample()` randomly selects rows from a DataFrame for analysis or testing.

## Code Analysis:
- `df.sample(n=5)` selects exactly 5 random rows
- `random_state=42` ensures reproducible results
- `len(sample)` returns the number of sampled rows: 5

## Sampling Methods:
```python
# Fixed number of rows
df.sample(n=10)

# Percentage of data
df.sample(frac=0.1)  # 10% of data

# Sampling with replacement
df.sample(n=50, replace=True)

# Stratified sampling
df.groupby('category').apply(lambda x: x.sample(n=5))

# Weighted sampling
weights = [0.1, 0.2, 0.3, 0.4]  # Must match DataFrame length
df.sample(n=2, weights=weights)
```

## Use Cases:
- **Exploratory Analysis**: Quick data overview
- **Testing**: Subset for development
- **Machine Learning**: Train/validation splits
- **A/B Testing**: Random user selection

## Random State:
- Ensures reproducible results
- Important for consistent testing
- Use same random_state for same results

Length: 5""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html",
        "points": 2,
        "answers": [
            {"text": "5", "is_correct": True},
            {"text": "100", "is_correct": False},
            {"text": "42", "is_correct": False},
            {"text": "Random number", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of data lineage in data engineering?",
        "explanation": """# Data Lineage in Data Engineering

Data lineage tracks the flow and transformation of data through systems.

## What is Data Lineage?
- Complete journey of data from source to destination
- Documentation of transformations and dependencies
- Visual representation of data flow
- Metadata about data processing

## Benefits:

### 1. Debugging and Troubleshooting
```python
# Example lineage tracking
def log_transformation(source, target, operation):
    lineage_log = {
        'timestamp': datetime.now(),
        'source': source,
        'target': target,
        'operation': operation,
        'user': getuser()
    }
    # Store in lineage database
    save_lineage(lineage_log)

def clean_data(df):
    log_transformation('raw_data', 'cleaned_data', 'remove_nulls')
    return df.dropna()
```

### 2. Impact Analysis
- Understand downstream effects of changes
- Identify affected reports and dashboards
- Plan maintenance windows effectively

### 3. Compliance and Auditing
- Track data for regulatory requirements
- Document data handling for audits
- Ensure data governance policies

### 4. Data Quality
- Identify data quality issues at source
- Track quality metrics through pipeline
- Root cause analysis for data problems

## Implementation Tools:

### Apache Atlas
```python
from pyatlasclient.client import Atlas

atlas = Atlas('http://localhost:21000', ('admin', 'admin'))

# Create data lineage
lineage = {
    'typeName': 'DataSet',
    'attributes': {
        'name': 'customer_data',
        'path': '/data/customers.csv'
    }
}
atlas.entity_post(entity=lineage)
```

### Great Expectations
```python
import great_expectations as ge

# Document data expectations
df_ge = ge.from_pandas(df)
df_ge.expect_column_values_to_not_be_null('customer_id')
df_ge.expect_column_values_to_be_unique('email')

# Generate documentation
df_ge.save_expectation_suite()
```

Essential for enterprise data management and governance.""",
        "reference": "https://en.wikipedia.org/wiki/Data_lineage",
        "points": 2,
        "answers": [
            {"text": "Track data flow and transformations through systems", "is_correct": True},
            {"text": "Sort data in linear order", "is_correct": False},
            {"text": "Create data backups automatically", "is_correct": False},
            {"text": "Compress data for storage", "is_correct": False},
        ],
    },
    {
        "text": """## Data Profiling

**What is the output of the following code?**

```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, None, 5], 'B': [10, 10, 30, 40, 50]})
profile = df.describe()
print(profile.shape)
```

*Choose the correct output:*""",
        "explanation": """# Pandas Data Profiling with describe()

`describe()` generates descriptive statistics for numerical columns.

## Code Analysis:
```python
df has 2 columns: 'A' (with 1 NaN) and 'B'
describe() returns statistics for both numerical columns

Standard statistics returned:
- count (non-null values)
- mean
- std (standard deviation)  
- min
- 25% (first quartile)
- 50% (median)
- 75% (third quartile)
- max
```

Shape: (8, 2) - 8 statistical measures, 2 columns

## Describe Output Example:
```
              A          B
count  4.000000   5.000000
mean   2.750000  28.000000
std    1.707825  18.547237
min    1.000000  10.000000
25%    1.750000  10.000000
50%    2.500000  30.000000
75%    3.500000  40.000000
max    5.000000  50.000000
```

## Data Profiling Extensions:
```python
# Include object columns
df.describe(include='all')

# Specific percentiles
df.describe(percentiles=[.1, .3, .5, .7, .9])

# Custom profiling
def custom_profile(df):
    profile = {
        'missing_count': df.isnull().sum(),
        'unique_count': df.nunique(),
        'memory_usage': df.memory_usage(deep=True)
    }
    return pd.DataFrame(profile)
```

Foundation for data exploration and quality assessment.""",
        "reference": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html",
        "points": 2,
        "answers": [
            {"text": "(8, 2)", "is_correct": True},
            {"text": "(5, 2)", "is_correct": False},
            {"text": "(2, 8)", "is_correct": False},
            {"text": "(7, 2)", "is_correct": False},
        ],
    },
]