import matplotlib.pyplot as plt
sales_id = [1001, 1003, 1006, 1007, 1009, 1011]
sales_salary = [10000, 23000.50, 18000.33, 16500.5, 12000.75, 9999.99]
purchase_id = [1002, 1004, 1010, 1008, 1014, 1015]
purchase_salary = [5000, 6000, 4500.5, 12000, 9000, 10000]
plt.bar(sales_id, sales_salary, color='skyblue', label='Sales Dept')
plt.bar(purchase_id, purchase_salary, color='orange', label='Purchase Dept')
plt.title("Microsoft Inc.")
plt.xlabel("employee id")
plt.ylabel("Salary")
plt.legend()
plt.show()