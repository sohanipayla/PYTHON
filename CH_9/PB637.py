import math
class Fraction:
    def __init__(self, n, d):
        self.n, self.d = n, d  # n = numerator, d = denominator
    def __add__(self, other):
        # Formula: (a*d + b*c) / (b*d)
        num = self.n * other.d + self.d * other.n
        den = self.d * other.d
        g = math.gcd(num, den)
        return f"{num//g}/{den//g}"
f1 = Fraction(1, 3)
f2 = Fraction(1, 6) 
print(f1 + f2)     