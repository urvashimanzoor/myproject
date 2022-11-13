#Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
# Especially it plays vital role in the context of multiple inheritance as single method may be found in
# multiple super classes.
#Case 1
# Python constructs the order in which it will look for a method in the hierarchy of classes.
# It uses this order, known as MRO, to determine which method it actually calls.
# It is possible to see MRO of a class using mro() method of the class.
class A:
    def process(self):
        print('A process()')
class B:
    pass
class C(A, B):
    pass
obj = C()
obj.process()
print(C.mro())   # print MRO for class C
#first it goes to super class given first in the list then second super class, from left to right order.
# Then finally Object class, which is a super class for all classes.
class A:
    def process(self):
        print('A process()')
class B:
    def process(self):
        print('B process()')
class C(A, B):
    pass
obj = C()
obj.process()
#In this case, we create D from C and B. Classes C and B have process() method and as expected MRO
# chooses method from C. Remember it goes from left to right. So it searches C first and all its
# super classes of C and then B and all its super classes.
class A:
    def process(self):
        print('A process()')
class B:
    def process(self):
        print('B process()')
class C(A, B):
    def process(self):
        print('C process()')
class D(C,B):
    pass
obj = D()
obj.process()
print(D.mro())

#CAse 4
class A:
    def process(self):
        print('A process()')
class B(A):
    pass
class C(A):
    def process(self):
        print('C process()')
class D(B,C):
    pass
obj = D()
obj.process()
#This is where Python applies a simple rule that says (known as good head question) when in MRO we
# have a super class before subclass then it must be removed from that position in MRO.