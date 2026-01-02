class A: pass
class B: pass
class C: pass
class D: pass
class E: pass
class K1(C,A,B): pass
class K3(A,D): pass
class K2(B,D,E): pass
class Z(K1,K3,K2): pass
print(Z.mro())