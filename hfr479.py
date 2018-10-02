from math import *
from scipy.integrate import quad
def integration(a,b):
    def f(x):
        return 3*x**2
    approximate,error = quad(f,b,a)
    return  approximate 
#N = int(input('Enter the number of polygons'))
#a = int(input('Enter the upper bound'))
#b = int(input('Enter the lower bound'))
def integrate(N,a,b):
    def f(x):
        return 3*x**2
    h = float(a-b)/N
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, N):
        result += f(b + i*h)
    result *= h
    return result
def enter():
    N = int(input('Enter the number of polygons ='))
    a = int(input('Enter the upper bound ='))
    b = int(input('Enter the lower bound ='))
    error = abs(integration(a,b)-integrate(N,a,b))
    print ('The numerical answer will be %f' %integration(a,b)) 
    #print (integration(a,b))
    print ('The trapezoidal answer will be %.16f' %integrate(N,a,b)) 
    #print (integrate(N,a,b))
    print ('Error is %.16f' % error)
    #return integration(a,b),integrate(N,a,b),error
    #return abs(integration(a,b)-integrate(N,a,b))
    #return integrate(N,a,b)
enter()