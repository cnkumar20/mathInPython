import matplotlib as mat
import numpy as np
import scipy as sp

##Arrays,Vectors,List,Matrix - Higlevel all are Same
# Lets begin playing with numpy to solve few mathematical problems or ultimately applied over real world scenario,
# which are in the form
# lets begin to convert the real world problem to a mathematical form f(x) or f(x,y,z,...)
# and then later see if the problem is solved just once or million time on different input and repetitively there comes the thing we are learning here!!
# If you don;t undersatnd anything then you need to work out problems <b>by hand </b>.
#
#And also brush up python and dats structures basics (List,Arrays,Dict,Set,class,)
#numpy library helps to code it python great deal (check : numpy-wiki).
#
#p Refer to my <hl>matplot</hl> lib
#
#
#
ara = np.array([1,2,3,4,5,6])
print(type(ara))
ara = np.arange(10)
print(type(ara))
ara = np.arange(10).reshape(5,2)
print(ara)
print(type(ara))
z = np.ones((3,4))
print(z)
#Matrix returns ndarray
a=np.mat('4 3; 2 1')
b=np.mat('1 2; 3 4')
print(a)
# [[4 3]
#  [2 1]]
print(b)
# [[1 2]
#  [3 4]]
print(a*b)

c=np.array([[4, 3], [2, 1]])
d=np.array([[1, 2], [3, 4]])
print(c@d)

#c*c
#[[4, 3], [2, 1]] * [[4, 3], [2, 1]]
#[[4*4 3*3],[4*4 1*1]]
print(c**2)

#Matix product , or product of vectors with multiple parameters(dimension)
print(np.dot(c,d))

def matrix_multiply(a,b):
    # result is 3x4
    result =    [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    # iterate through rows of X
    for i in range(len(a)):
        # iterate through columns of Y
        for j in range(len(b[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

func = np.vectorize(matrix_multiply)
print(func(c,d))

#Lets start from series of numbers in one dimensional matrix aka Array
# Example 1 : f(x)= x
# When n is a variable or huge number
# for(i in range(0 to n)):
#       f(x)
#
#p
#Solution:
# [f(1),f(2),f(3)...f(n)]
# since f(x)=x
# [1,2,3.....n]
#c
#p
#Code for f(x)=x

#c
# code f(x)=x
def f(x):
    return x

#c
#For n=6
#

arr = np.array([1,2,3,4,5,6])
func = np.vectorize(f)
print(func(arr))
# [3 4 5 6 7 8]

#p
# Now lets move to next step , thats to play with series of numbers , where on each element
# atomic operation is done
#To perform Vector mathematical functions functions
#Examp f1(x) = f1+2
#Then above array should be
#p
#Solution:
# [f(1)+2,f(2)+2,f(3)+2...f(n)+2]
# since f(x)=x
# [1+2,2+2,3+2.....n]
# [3,4,5,...n]
#c

#c
# code f(x)=x
def f(x):
    return x+2

#c
#For n=6
#

arr = np.array([1,2,3,4,5,6])
func = np.vectorize(f)
print(func(arr))
# [3 4 5 6 7 8]



#p Multidimensional or Vectors with multitple coordinates reresentedsas ndArray from Matrix or from the array
# Example 3
# f(x) = a + b
# where a and b are m*m matrix

#c
#Note both array and matrix return ndArray
#
#Solution 1(from array)
aa = np.array([[1,2,3,4], [2,3,4,5], [5,6,7,8], [9,10,11,12]])
bb = np.array([[100,200,300,400], [100,200,300,400], [100,200,300,400], [100,200,300,400]])

#notic : This the function as a mathematician you need to most bother , The library Vectorize performs the defined function on each element of the Vector,array
#note: notic broadcasting of vector fails for the below function if row and clums are not Same
#c
def vec2(bsub, asub):
    return bsub+asub
##img solve by hand

func = np.vectorize(vec2)
print(func(bb, aa))

#Solution 2(from matrix)
aa = np.matrix([[1,2,3,4], [2,3,4,5], [5,6,7,8], [9,10,11,12]])
bb = np.matrix([[100,200,300,400], [100,200,300,400], [100,200,300,400], [100,200,300,400]])

#notic : This the function as a mathematician you need to most bother , The library Vectorize performs the defined function on each element of the Vector,array
#note: notic broadcasting of vector fails for the below function if row and clums are not Same
#c
def vec2(bsub, asub):
    return bsub+asub
##img solve by hand

func = np.vectorize(vec2)
print(func(bb, aa))
# [[101 202 303 404]
#  [102 203 304 405]
#  [105 206 307 408]
#  [109 210 311 412]]
