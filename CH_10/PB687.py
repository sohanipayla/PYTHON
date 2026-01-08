import matplotlib.pyplot as plt
labels = ['Engineering', 'Manufacturing', 'Sales', 'Profit']
costs = [1.35, 3.60, 2.25, 1.80]
colors = ['skyblue', 'lightgreen', 'orange', 'pink']
plt.pie(costs, labels=labels, colors=colors,)
plt.title('Cost Breakdown for a $9.00 Microcontroller')
plt.show()