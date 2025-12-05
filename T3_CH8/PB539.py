class SQEmptyError(Exception):
    pass
class SQ:
    def __init__(self, elements=None):
        if elements is None:
            self.data = []
        else:
            self.data = list(elements)
    def shift(self):
        if not self.data:
            raise SQEmptyError("SQ is empty! Cannot shift.")
        return self.data.pop(0)
    def unshift(self, element):
        self.data.insert(0, element)
    def push(self, element):
        self.data.append(element)
    def pop(self):
        if not self.data:
            raise SQEmptyError("SQ is empty! Cannot pop.")
        return self.data.pop()
    def remove(self):
        if not self.data:
            raise SQEmptyError("SQ is empty! Cannot remove max element.")
        max_element = max(self.data)
        self.data.remove(max_element)
        return max_element
    def show(self):
        print(self.data)
sq = SQ([10, 20, 30])
print("Initial SQ:", sq.data)
print("shift:", sq.shift())
sq.show()
sq.unshift(5)
print("After unshift(5):")
sq.show()
sq.push(40)
print("After push(40):")
sq.show()
print("pop:", sq.pop())
sq.show()
print("remove max:", sq.remove())
sq.show()