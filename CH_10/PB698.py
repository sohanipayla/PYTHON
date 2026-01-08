import matplotlib.pyplot as plt
X = [2012, 2013, 2014, 2015, 2016, 2017]
y = [9, 10, 10.5, 8.8, 10.9, 9.75]
plt.plot(X, y, linestyle='dashed')
plt.xlabel("Years")
plt.ylabel("Profits (in Millions)")
plt.title("XYZ Company")
plt.show()