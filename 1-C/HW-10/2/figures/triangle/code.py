from math import sqrt

a = 7
b = 2
c = 8

def triangle_perimeter(a = a, b = b, c = c):
    return (a+b+c)

def triangle_area(a = a, b = b, c = c):
    P = triangle_perimeter(a, b, c)
    return (sqrt(P*(P-a)*(P-b)*(P-c)))