import math
def method(f, a, b, tol=1e-6, maxIter=100):

    if f(a) * f(b) > 0:
        print("The bisection method cannot be applied. f(a) and f(b) must have opposite signs.")
        return None
    

    for i in range(maxIter):

        c = (a + b) / 2
        fc = f(c)
        print(f"c = {fc} when a ={a} , b = {b} and c = {c}")


        if abs(fc) < tol:
            print(f"Root found: {c} after {i+1} iterations.")
            return c
        

        if f(a) * fc < 0:
            b = c  
        else:
            a = c  
    

    print("Maximum iterations reached.")
    return None

def f(x):
    return math.sin(x) - 5*x + 2

root = method(f, 0.4, 0.6)
print(f"Root: {root}")
