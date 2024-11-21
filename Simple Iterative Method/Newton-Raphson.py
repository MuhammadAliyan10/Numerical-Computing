from sympy import symbols, diff

def derivativeEquation(equation):
    x = symbols('x')
    derivative = diff(equation, x)
    return derivative

x = symbols('x')
equation = x**3 - 4*x**2 + x - 10
primeX = derivativeEquation(equation)

def newtonRaphsonMethod(initialGuess, tol=1e-6, maxIter=100):
    x_Val = initialGuess
    for i in range(maxIter):
        fx = equation.subs(x, x_Val).evalf() 
        f_Prime_x = primeX.subs(x, x_Val).evalf() 
        
        print(f"Iteration {i+1}: x = {x_Val}, f(x) = {fx}, f'(x) = {f_Prime_x}")
        
        if f_Prime_x == 0:
            raise ValueError("Derivative is zero. The method fails.")
        
        next_x = x_Val - fx / f_Prime_x
    
        if abs(next_x - x_Val) < tol:
            return next_x, i + 1 
        
        x_Val = next_x
    
    raise ValueError("Maximum iterations reached. The method did not converge.")

try:
    root, iterations = newtonRaphsonMethod(initialGuess=4)
    print(f"Root: {root:.6f}, found in {iterations} iterations")
except ValueError as e:
    print(e)
