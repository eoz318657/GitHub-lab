# Create the dictionary
student = {
    'name': 'Alice',
    'age': 21,
    'major': 'Computer Science'
}

# Print the student's name
print("Student's name:", student['name'])

# Update the age to 22
student['age'] = 22

# Add a new key-value pair: 'GPA': 3.8
student['GPA'] = 3.8

# Remove the 'major' key and print the updated dictionary
removed_major = student.pop('major')
print("Updated student dictionary:", student)