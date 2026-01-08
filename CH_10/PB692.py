import matplotlib.pyplot as plt
Country = ['USA', 'Canada', 'Germany', 'UK', 'France']
GDP_Per_Capita = [45000, 42000, 52000, 49000, 47000]
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.bar(Country, GDP_Per_Capita, color=colors)
plt.title('GDP Per Capita by Country')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita (USD)')
plt.grid(True)
plt.show()