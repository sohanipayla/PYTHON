import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12, 15))
plt.suptitle('My Subplot for Cars & Data', fontsize=16, fontweight='bold')
# --- 1. Line Plot ---
plt.subplot(3, 2, 1)
plt.plot([5,10,25,60,80], [5,17,25,40,30], 'g:D') 
plt.title("Line Graph"), plt.xlabel("X"), plt.ylabel("Y")
# --- 2. Grouped Bar Chart ---
plt.subplot(3, 2, 2)
x = np.arange(5)
plt.bar(x - 0.2, [22,30,35,35,26], 0.4, color='green', label='Men')
plt.bar(x + 0.2, [25,32,30,35,29], 0.4, color='red', label='Women')
plt.title(r"$\mathbf{Scores\ by\ Group}$"), plt.legend()
# --- 3. Pie Chart ---
plt.subplot(3, 2, 3)
plt.pie([25,50,30,20,35], labels=['Maruti','Hyundai','Kia','Toyota','Honda'])
plt.title("Car Popularity")
# --- 4. Scatter Plot ---
plt.subplot(3, 2, 4)
m = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
s = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
plt.scatter(range(10), m, color='yellow', marker='o', label='Math')
plt.scatter(range(10), s, color='blue', marker='*', label='Science')
plt.title("Math vs Science"), plt.legend()
# --- 5. Horizontal Bar Chart ---
plt.subplot(3, 2, 5)
langs = ['Java', 'Python', 'PHP', 'JS', 'C', 'C++']
pop = [20, 100, 25, 30, 45, 50]
plt.barh(langs, pop, color=['red', 'blue', 'green', 'yellow', 'purple', 'orange'])
plt.title("Programming Languages"), plt.xlabel("Popularity")
# --- 6. Histogram ---
plt.subplot(3, 2, 6)
data = [10,20,20,30,30,30,40,40,40,40,50,50,50,60,60,70]
plt.hist(data, color='red', edgecolor='black')
plt.title("Frequency Histogram")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()