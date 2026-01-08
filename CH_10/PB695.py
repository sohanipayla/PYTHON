import matplotlib.pyplot as plt
emp_ages = [22, 45, 30, 59, 58, 56, 57, 45, 43, 43, 50, 40, 34, 33, 25, 19]
age_bins = [0, 10, 20, 30, 40, 50, 60]
plt.hist(emp_ages, bins=age_bins, color='cyan', edgecolor='black')
plt.xlabel("emplyee ages")
plt.ylabel(" no. of employees")
plt.title("Oracle Corp")
plt.show()