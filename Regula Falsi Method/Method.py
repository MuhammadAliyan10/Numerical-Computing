def flasiMethod(f, a, b):
    z = a - (f(a) * (a - b)) / (f(a) - f(b))
    return z

def method(f, a, b, tol=1e-6, maxItr=100):
    if f(a) * f(b) > 0:
        print("The regula falsi method cannot be applied. f(a) and f(b) must have opposite signs.")
        return None

    for _ in range(maxItr):
        z = flasiMethod(f, a, b)
        
        if abs(f(z)) < tol or abs(b - a) < tol:
            return z

        if f(a) * f(z) < 0:
            b = z
        else:
            a = z
    
    print("Maximum iterations reached. The method did not converge.")
    return None

def f(x):
    return x**3 - x - 2

root = method(f, 1, 2)
if root is not None:
    print(f"The root is approximately: {root}")
