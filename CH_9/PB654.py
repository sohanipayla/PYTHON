# 1. Base Class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
# 2. Derived Class (Child)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak() 
        print(f"{self.name} is a {self.breed} and he barks!")
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.speak()