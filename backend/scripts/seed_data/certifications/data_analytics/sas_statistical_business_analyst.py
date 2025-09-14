"""SAS Certified Statistical Business Analyst Certification"""

CERTIFICATION = {
    "name": "SAS Certified Statistical Business Analyst",
    "description": "Statistical analysis and data manipulation using SAS software for business insights",
    "slug": "sas-certified-statistical-business-analyst",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "data-analytics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which SAS procedure is used for descriptive statistics?",
        "explanation": "PROC MEANS is the primary SAS procedure for calculating descriptive statistics like mean, median, standard deviation, and quartiles for numeric variables.",
        "reference": "https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/proc/p0klmrp4k2a40tn1p72t8nusxhuu.htm",
        "points": 1,
        "answers": [
            {"text": "PROC MEANS", "is_correct": True},
            {"text": "PROC FREQ", "is_correct": False},
            {"text": "PROC SORT", "is_correct": False},
            {"text": "PROC PRINT", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of PROC FREQ in SAS?",
        "explanation": "PROC FREQ generates frequency tables and cross-tabulations, providing counts and percentages for categorical variables and analyzing relationships between categorical variables.",
        "reference": "https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/proc/p0s9ilagbmb4whn1p7nwkn6bthl6.htm",
        "points": 1,
        "answers": [
            {
                "text": "Generate frequency tables and cross-tabulations",
                "is_correct": True,
            },
            {"text": "Calculate correlation coefficients", "is_correct": False},
            {"text": "Perform regression analysis", "is_correct": False},
            {"text": "Sort datasets", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to create a new variable in a SAS DATA step?",
        "explanation": "Assignment statements in the DATA step create new variables by assigning values using expressions, functions, or conditional logic with IF-THEN statements.",
        "reference": "https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/p01hqtzxc2f8e4n1uf9jbaj1lf5c.htm",
        "points": 1,
        "answers": [
            {
                "text": "Assignment statement (variable = expression)",
                "is_correct": True,
            },
            {"text": "PROC statement", "is_correct": False},
            {"text": "FORMAT statement", "is_correct": False},
            {"text": "LABEL statement", "is_correct": False},
        ],
    },
    {
        "text": "What does the BY statement do in SAS procedures?",
        "explanation": "The BY statement groups observations and performs the procedure separately for each unique value of the BY variable(s), requiring the dataset to be sorted by the BY variables first.",
        "reference": "https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/n1c3obcoh7nq5wn1g3r6gzle3vg0.htm",
        "points": 1,
        "answers": [
            {
                "text": "Process data separately for each unique value of specified variables",
                "is_correct": True,
            },
            {"text": "Sort the dataset", "is_correct": False},
            {"text": "Filter observations", "is_correct": False},
            {"text": "Create new variables", "is_correct": False},
        ],
    },
    {
        "text": "Which SAS procedure is used for correlation analysis?",
        "explanation": "PROC CORR calculates Pearson correlation coefficients between numeric variables and can also compute other correlation statistics like Spearman and Kendall correlations.",
        "reference": "https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/proc/p1av6q4b5tmoptn1w0l5ebmzvqqd.htm",
        "points": 1,
        "answers": [
            {"text": "PROC CORR", "is_correct": True},
            {"text": "PROC REG", "is_correct": False},
            {"text": "PROC MEANS", "is_correct": False},
            {"text": "PROC TTEST", "is_correct": False},
        ],
    },
]
