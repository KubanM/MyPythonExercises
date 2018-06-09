
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Comp Sci']}

print student, '\n'
print 'Student name is:', student['name'], '\n'
print 'Courses is', student["courses"], '\n'

# Return None insead of error
print student.get('phone'), '\n'

student['phone'] = 123456789

print student.get('phone', 'Not Found'), '\n'




