import math
class Fraction:
    def __init__(self, n, d):
        self.n, self.d = n, d
    def __mul__(self, other):
        # Cross multiplication logic: (a/b + c/d)
        new_n = self.n * other.d + self.d * other.n
        new_d = self.d * other.d
        common = math.gcd(new_n, new_d)
        return f"{new_n//common}/{new_d//common}"
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1 * f2)  