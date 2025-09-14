"""JavaScript Developer Certification"""

CERTIFICATION = {
    "name": "JavaScript Developer Certification",
    "description": "Modern JavaScript and ES6+ features",
    "slug": "javascript-developer-certification",
    "level": "Associate",
    "duration": 3,
    "questions_count": 1,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [{"text": "What is the difference between '==' and '===' operators in JavaScript?",
              "explanation": "'==' performs type coercion and compares values, while '===' compares both value and type without coercion.",
              "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness",
              "points": 1,
              "answers": [{"text": "No difference",
                           "is_correct": False},
                          {"text": "'===' is stricter and doesn't perform type coercion",
                           "is_correct": True,
                           },
                          {"text": "'==' is stricter",
                           "is_correct": False},
                          {"text": "They work only with numbers",
                           "is_correct": False},
                          ],
              }]
