"""Microsoft Power BI Data Analyst Associate Certification"""

CERTIFICATION = {
    "name": "Microsoft Power BI Data Analyst Associate",
    "description": "Design and build scalable data models, clean and transform data, and enable advanced analytic capabilities",
    "slug": "microsoft-power-bi-data-analyst",
    "level": "Associate",
    "duration": 120,
    "questions_count": 60,
    "category_slug": "data-analytics",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary purpose of Power Query in Power BI?",
        "explanation": "Power Query is a data transformation and data preparation engine that allows you to discover, connect, combine, and refine data sources to meet your analysis needs.",
        "reference": "https://docs.microsoft.com/en-us/power-query/power-query-what-is-power-query",
        "points": 1,
        "answers": [
            {"text": "Data transformation and preparation", "is_correct": True},
            {"text": "Creating visualizations", "is_correct": False},
            {"text": "Managing user permissions", "is_correct": False},
            {"text": "Scheduling data refreshes", "is_correct": False}
        ]
    },
    {
        "text": "Which DAX function is used to calculate a running total?",
        "explanation": "The CALCULATE function combined with filters like FILTER or date functions can create running totals by modifying the filter context to include all previous rows or dates.",
        "reference": "https://docs.microsoft.com/en-us/dax/calculate-function-dax",
        "points": 1,
        "answers": [
            {"text": "CALCULATE with appropriate filters", "is_correct": True},
            {"text": "SUM", "is_correct": False},
            {"text": "COUNT", "is_correct": False},
            {"text": "AVERAGE", "is_correct": False}
        ]
    },
    {
        "text": "What is the difference between DirectQuery and Import mode in Power BI?",
        "explanation": "Import mode loads data into Power BI's memory for faster performance, while DirectQuery sends queries directly to the source database in real-time, keeping data fresh but potentially slower.",
        "reference": "https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-directquery-about",
        "points": 1,
        "answers": [
            {"text": "Import loads data into memory; DirectQuery queries source in real-time", "is_correct": True},
            {"text": "They are the same thing", "is_correct": False},
            {"text": "DirectQuery is faster than Import", "is_correct": False},
            {"text": "Import requires more licenses", "is_correct": False}
        ]
    },
    {
        "text": "Which visualization is best for showing correlation between two numeric variables?",
        "explanation": "A scatter chart is the most effective visualization for showing the relationship and correlation between two continuous numeric variables.",
        "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-scatter",
        "points": 1,
        "answers": [
            {"text": "Scatter chart", "is_correct": True},
            {"text": "Bar chart", "is_correct": False},
            {"text": "Pie chart", "is_correct": False},
            {"text": "Line chart", "is_correct": False}
        ]
    },
    {
        "text": "What is row-level security (RLS) in Power BI?",
        "explanation": "Row-level security (RLS) restricts data access for given users by filtering data at the row level based on user roles and filters defined in the data model.",
        "reference": "https://docs.microsoft.com/en-us/power-bi/admin/service-admin-rls",
        "points": 1,
        "answers": [
            {"text": "Restricting data access at the row level based on user roles", "is_correct": True},
            {"text": "Encrypting data in transit", "is_correct": False},
            {"text": "Backing up data rows", "is_correct": False},
            {"text": "Optimizing query performance", "is_correct": False}
        ]
    }
]
