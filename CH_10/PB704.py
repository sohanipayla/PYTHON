import numpy as np
import matplotlib.pyplot as plt
scores = np.array([[13, 10, 9, 33], [63, 46, 90, 42], [39, 76, 13, 29], [82, 9, 29, 78], [67, 61, 59, 36]])
# (i) Add 5th match as a new column
match_5 = [[41], [87], [72], [36], [92]]
scores = np.append(scores, match_5, axis=1)
# (ii) Add two new batsmen as new rows
b6 = [77, 83, 98, 95, 89]
b7 = [92, 71, 52, 61, 53]
scores = np.append(scores, [b6, b7], axis=0)
# (iii) Add a column for Total Scores
total = np.sum(scores, axis=1).reshape(-1, 1) # Calculate row sums
final_array = np.append(scores, total, axis=1)
print("Final Array:\n", final_array)
# --- GRAPHING (Using Slicing) ---
# (a) Line Chart: Total Scores vs No. of Batsman
plt.figure()
plt.plot(range(1, 8), final_array[:, 5], 'k--', marker='o') 
plt.title("Leader Board", fontweight='bold')
plt.xlabel("No. of Batsman")
plt.ylabel("Scores")
plt.show()
# (b) Bar Chart: Batsman 1 vs Batsman 2 (Matches 1-5)
plt.figure()
x = np.arange(1, 6)
plt.bar(x - 0.2, final_array[0, 0:5], width=0.4, color='purple', label='Batsman 1')
plt.bar(x + 0.2, final_array[1, 0:5], width=0.4, color='darkred', label='Batsman 2')
plt.legend()
plt.show()
# (c) Pie Chart: Total Scores
plt.figure()
plt.pie(final_array[:, 5], labels=[f"B{i}" for i in range(1,8)], 
        explode=[0.1]*7, autopct='%1.1f%%')
plt.title("Total Score Share")
plt.legend()
plt.show()