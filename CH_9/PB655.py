class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for i in range(cols)] for j in range(rows)]
    def display_info(self):
        print(f"Matrix created with {self.rows} rows and {self.cols} columns.")
m1 = Matrix(3, 4)
m1.display_info()