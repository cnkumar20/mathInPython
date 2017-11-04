#Before we start working on advanced math libraries of python like numpy and Scipy
#we will explore the basic math lib provided by base python 3.6 package
#Reddit : @cnkumar20
#Email :cnkumar20@gmail.com

import math as math
from math import pi as pi
from random import randint
import matplotlib.pyplot as pyplot
from decimal import Decimal
from decimal import Decimal
#Addition
2+3
2+(-5)
1000+12




#Subtraction
2-3
2-(-5)
8-3
-8-(-2)

#Multiplication
8*8
8*-1
8*-(-1)
12*0.5
12351231235123*126623456612234

#division
2/3
math.sqrt(4)



#Trignometry
math.sin(0)
math.sin(pi/2)
math.sin(pi)
math.sin(3*pi/2)


math.cos(0)
math.cos(pi/2)
math.cos(pi)
math.cos(3*pi/2)

math.tan(0)
math.tan(pi)
math.tan(pi/2)
math.tan(3*pi/2)
math.tan(2*pi)

num = math.tan(pi)
print(num)
print(int(num))
print(float(num))


#sin^2(x)+cos^2(x)=1
x = randint(-9999,9999)
math.pow(math.sin(x),2)+math.pow(math.cos(x),2)
1 + math.pow(math.tan(x),2)
math.pow(1/math.cos(x),2)
result = ((1 + math.pow(math.tan(x),2))==math.pow(1/math.cos(x),2))
print(result)


#Decimal

Decimal('-3.14').as_integer_ratio()
