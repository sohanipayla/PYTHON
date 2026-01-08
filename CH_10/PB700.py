import matplotlib.pyplot as plt
discounts = [10, 20, 30, 40, 50]
sales = []
print("Enter sales for 5 weeks:")
for i in range(5):
    val = float(input(f"Enter sales for {discounts[i]}% discount: "))
    sales.append(val)
plt.scatter(discounts, sales, color='blue', marker='*')
plt.xlabel("Discount Offered (%)")
plt.ylabel("Sales (in Rupees)")
plt.title("Discount vs Sales Relationship")
plt.show()