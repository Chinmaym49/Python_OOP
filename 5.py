class Complex:

    def __init__(self,r,i):
        self.real=r
        self.imag=i

    # Overloading the print function so it prints something meaningful
    def __str__(self):
        if self.imag>0:
            op="+"
        else:
            op=""
        return "{}{}{}i".format(self.real,op,self.imag)

    # Overloading +. This is how its done in pyth
    def __add__(self,ob):
        r=self.real+ob.real
        i=self.imag+ob.imag
        return Complex(r,i)

    def __eq__(self,ob):
        if self.real==ob.real and self.imag==ob.imag:
            return True
        return False


if __name__=="__main__":
    c1=Complex(6,3)
    print(c1)
    c2=Complex(4,-7)
    print(c2)
    c3=c1+c2
    print(c3)
    if c1==c2:
        print("Equal")
    else:
        print("Not Equal")

# 6+3i
# 4-7i
# 10-4i
# Not Equal 

# Some internal methods

# Print                 print(p)    p.__str__()
# Addition	            p1 + p2	    p1.__add__(p2)
# Subtraction	        p1 - p2	    p1.__sub__(p2)
# Multiplication	    p1 * p2	    p1.__mul__(p2)
# Power	                p1 ** p2	p1.__pow__(p2)
# Division	            p1 / p2	    p1.__truediv__(p2)
# Floor Division	    p1 // p2	p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2	    p1.__mod__(p2)

# Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
# Bitwise AND	        p1 & p2	    p1.__and__(p2)
# Bitwise OR	        p1 | p2	    p1.__or__(p2)
# Bitwise XOR	        p1 ^ p2	    p1.__xor__(p2)
# Bitwise NOT	        ~p1	        p1.__invert__()

# Less than	            p1 < p2	    p1.__lt__(p2)
# Less than equal	    p1 <= p2	p1.__le__(p2)
# Equal to	            p1==p2      p1.__eq__(p2)
# Not equal to	        p1 != p2	p1.__ne__(p2)
# Greater than	        p1 > p2	    p1.__gt__(p2)
# Greater than equal	p1 >= p2	p1.__ge__(p2)