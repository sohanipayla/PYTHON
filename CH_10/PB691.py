import matplotlib.pyplot as plt
data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35}
courses = list(data.keys())
students = list(data.values())
plt.bar(courses, students, color='green')
plt.xlabel("Course Name")
plt.ylabel("No. of Students")
plt.title("Course v/s No. of Students")
plt.show()