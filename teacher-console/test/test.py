student = []

try:
    locate = student.index("123")
except:
    student.append("123")
    locate = student.index("123")

print(student)
print(locate)