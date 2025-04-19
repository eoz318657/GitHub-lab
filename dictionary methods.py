# Given dictionary
grades = {'John': 85, 'Alice': 92, 'Bob': 78}

# 1. Add a new student 'David' with a grade of 88
grades['David'] = 88

# 2. Check if 'Alice' exists in the dictionary
if 'Alice' in grades:
    print("Alice exists in the dictionary")
else:
    print("Alice does not exist in the dictionary")

# 3. Print all student names and their grades using a loop
print("\nStudent grades:")
for student, grade in grades.items():
    print(f"{student}: {grade}")