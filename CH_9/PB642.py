class Data:
    def __init__(self, value):
        self.value = value
    # Overloading '>' operator using __gt__
    def __gt__(self, other):
        return self.value > other.value
    # Overloading '<' operator using __lt__ 
    def __lt__(self, other):
        return self.value < other.value
d1 = Data(10)
d2 = Data(20)
print(f"Is d1 > d2? {d1 > d2}")  
print(f"Is d1 < d2? {d1 < d2}")  