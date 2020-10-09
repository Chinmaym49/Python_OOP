class A:

    def __init__(self,a):
        self.a=a

    def display(self):
        print(self.a)

class B:

    def __init__(self,b):
        self.b=b

    def display(self):
        print(self.b)

class C(A,B):

    def __init__(self,a,b,c):
        A.__init__(self,a)              # Calling base class contructors to pass parameters
        B.__init__(self,b)
        self.c=c

    def disp(self):
        A.display(self)                 # Calling base class functions
        B.display(self)
        print(self.a,self.b,self.c)     # Accessing base class data members

if __name__=="__main__":
    c=C("A","B","C")
    c.disp()

# A
# B
# C
# A B C

# Its best to avoid super() because in multiple inheritance, super() can only be used to access members
# from the 1st class (here, class A).
# Moreover, if "x" is a data member of base class, we cannot have another "x" as a data member of
# derived class. If we do so, then self.x will always access base class "x"
