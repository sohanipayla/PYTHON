class Data:
    def __init__(self, *args):
        if args:
            self.status = True
        else:
            self.status = False
    def check(self):
        return self.status
obj1 = Data()         
obj2 = Data("Hello")   
print(f"No argument passed: {obj1.check()}")    
print(f"Argument passed: {obj2.check()}")      