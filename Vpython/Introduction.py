GlowScript 3.1 VPython
                     
from vpython import *

# Definition of vectors

a = vec(4, 3, 2)
b = vec(4**2, 3**2, 2**2)
c = vec(sqrt(4.6), 3.14**2, 3.14**(1/2))
print('a, b, c', a, b, c)

# Lineartiy of vectors

alpha = 2.5
beta = 3.2

c = alpha * a + beta * b
d = alpha * a - beta * b
print('c: ',c,'d: ',d)

# Refer to components

a1 = vec(4.6, -3.2, 2.9)
b1 = vec(-5.4, 4.6, 3.1)

print('a1: ', a1, 'b1: ', b1)
print('components: ', a1.x, a1.y, a1.z, b1.x, b1.y, b1.z)

# Magnitude and Magnitude^2

print('Magnitude: ', mag(a1), a1.mag, sqrt(a1.x**2 + a1.y**2 + a1.z**2))

print('magnitude^2: ', mag2(a), a.mag2, a.x**2 + a.y**2 + a.z**2)

# Norm of vectors

print('a: ', a)
print('norm: ', norm(a), a.norm(), a/mag(a))
print( mag( norm( a ) ) )
print('unit vector: ', hat(a), a.hat, a/mag(a), mag(a.hat))

# Dot and cross products

a = vec(2.5, -2, 5)
b = vec(-3, 2, -1.2)

print('a & b: ', a, b)

print('a * b: ', dot(a, b), a.dot(b))
print('b * a: ', dot(b, a), b.dot(a))

print('a x b: ', cross(a,b), a.cross(b))
print('b x a: ', cross(b,a), b.cross(a))

# Orthogonality 

c = a.cross(b) # c orthogonal to a and b

print('c = a x b: ', c, dot(a,c), dot(b,c))
print('angle a-b: ', diff_angle(a,b), a.diff_angle(b))
print('angle a-c: ', diff_angle(a,c), a.diff_angle(c), pi/2)
print('angle b-c: ', diff_angle(b,c), b.diff_angle(c), pi/2)

# Projection of a along b

print('projection', proj(a,b), a.dot(b.hat)*b.hat)

# Rotate a vector

v2 = rotate(a, angle = pi, axis = vec(0,0,1))

print('a rotated by pi around z axis: ', a, v2)

# Angle between vectors

print('a, b, c', a, b, c)
print('angle (a, b)', a.diff_angle(b))
print('angle (b, a)', b.diff_angle(a))
print('angle (a, c)', a.diff_angle(c))
print('angle (b, c)', b.diff_angle(c))


##################################

# graphs

gr2 = graph(title='Functions', xtitle = 'x', ytitle = 'f(x)')

def silly(x):               # user defined function
    y = sqrt(x**2 + 9)
    return y
print('result of function at x = 5: ', silly(5))

g1 = gcurve(graph = gr2, color = color.red)
g2 = gcurve(graph = gr2, color = color.green)

for x in arange(0, 8.005, 0.01):        # x from 0 to 8.005 with a step 0.01
    g1.plot(x, silly(x))
    g2.plot(x, sin(x))
    
# creating loops 

# adding up integers up to  nn

# while construction

nn = 100
x = 1
ss = 0 
while  x <= nn:
    ss += x
    x += 1

print('sum from 1 to ',nn,': ',ss,nn*(nn+1)/2)

# arange construction

nn = 100
ss = 0
for x in arange(1, nn+1, 1):
    ss += x
#for x in arange(1, nn+1, 1):
    #ss += x
    
print('sum from 1 to',nn,': ',ss)


# using sum function

print('sum from 1 to ', nn, ': ', sum(arange(1, nn + 1, 1)), sum(range(1, nn + 1, 1)))

# Unit vector

xu = (x/(sqrt((x^2)+(y^2)+(z^2))
yu = (y/(sqrt((x^2)+(y^2)+(z^2))
zu = (z/(sqrt((x^2)+(y^2)+(z^2))

# momentum vector

p = 1/(sqrt(1-(mag(v)/c)**2)) * m * v
