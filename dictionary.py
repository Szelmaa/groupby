from itertools import groupby

# Grouping a dictionary of student grades based on their letter grade
grades = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 80, 'Eve': 95,
          'Frank': 68}

letter_grades = {
    key: 'A' if value >= 90 else 'B' if value >= 80 else 'C' if value >= 70 else 'D'
    for key, value in
    dict(sorted(grades.items(), key=lambda item: item[1])).items()}

groups = groupby(letter_grades, key=lambda x: letter_grades[x])

for key, group in groups:
    print(key, dict((name, grades[name]) for name in group))
