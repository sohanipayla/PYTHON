import matplotlib.pyplot as plt
grades = ['A', 'B', 'C', 'D']
students = [4, 12, 10, 2]
colors = ['blue', 'green', 'yellow', 'red'] # Different colors for each
wedge_effect = [0, 0, 0, 0.2]               # 0.2 pulls the 4th slice (D) out
plt.pie(students, labels=grades, colors=colors, explode=wedge_effect)
plt.title("student's grade history")
plt.show()