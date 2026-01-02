class A:
    def __init__(self):
        print("A's init called")
        self.name = "Parent A"
class B:
    def __init__(self):
        print("B's init called")
        self.age = 40
class C(A, B):
    def __init__(self):
        print("C's init called")
        A.__init__(self)  
obj = C()
print(obj.name) 