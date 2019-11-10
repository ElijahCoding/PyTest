class A:
    def method(self):
        print("A method")

class B(A):
    pass

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

# obj = D()
# # obj.method()
# # print(D.mro())

for cls in [A, B, C ,D]:
    print(cls.__name__ + ": ", cls.mro())