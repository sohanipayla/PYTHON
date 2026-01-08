import matplotlib.pyplot as plt
wait_times = [43.1, 35.6, 37.6, 36.5, 45.3, 43.5, 40.3, 50.2, 47.3, 31.2, 
              42.2, 45.5, 30.3, 31.4, 35.6, 45.2, 54.1, 45.6, 36.5, 43.1]
plt.hist(wait_times, bins=6, color='skyblue', edgecolor='black')
plt.title('Customer Wait Times Analysis')
plt.xlabel('Wait Time (seconds)')
plt.ylabel('Number of Customers')
plt.show()