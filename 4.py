class A:

    def display(self):
        print("A")

class B:

    def display(self):
        print("B")

class C(A,B):

    def disp(self):
        print("C")

if __name__=="__main__":
    c=C()
    c.disp()
    c.display()

    # In C++, this would have resulted in diamond problem. But here, A's display
    # is called because it comes first in C's declaration. This is called MRO
    # Method Resolution Order
    print(C.__mro__)

# C
# A
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)