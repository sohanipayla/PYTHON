import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
plt.suptitle('My Subplot for cars', fontsize=18, fontweight='bold')
# --- 1. Scatter Plot ---
plt.subplot(2, 2, 1)
x_scatter = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y_scatter = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x_scatter, y_scatter, marker='*', color='green', s=60)
plt.title('age v/s speed of car')
plt.xlabel('age of car')
plt.ylabel('speed of car')
# --- 2. Horizontal Bar Plot ---
plt.subplot(2, 2, 2)
x_bar = ["A", "B", "C", "D"]
y_bar = [3, 8, 1, 10]
plt.barh(x_bar, y_bar, height=0.1, color='yellow')
plt.title('name v/s selling of car')
plt.xlabel('selling of car')
plt.ylabel('name of car')
# --- 3. Histogram ---
plt.subplot(2, 2, 3)
hist_data = [1, 3, 3, 3, 3, 9, 9, 5, 4, 4, 8, 8, 8, 6, 7]
plt.hist(hist_data, bins=4, orientation='vertical', color='violet', edgecolor='black')
plt.title('histogram of cars')
plt.xlabel('Data Intervals')
plt.ylabel('Frequency')
# --- 4. Pie Chart ---
plt.subplot(2, 2, 4)
y_pie = [35, 25, 25, 15]
mylabels = ['Apple', 'Bananas', 'Cherries', 'Dates']
myexplode = [0.2, 0, 0, 0] 
plt.pie(y_pie, labels=mylabels, explode=myexplode, shadow=True, startangle=90)
plt.title('pie chart')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()