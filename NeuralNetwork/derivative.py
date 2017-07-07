import numpy as np

# This function returns a value closer to the limit
def x2(x1): return x1 + (x1 * (10**-10))

# This function calculates de variation when we move x closer to the limit
# It is a good approximation for the derivative
def derivative(f, x): return (f(x2(x))-f(x))/(x2(x)-x)

# Sample and test data

x = np.array([1, 2, 3, 4, 5, 6, 7, 9, 10])

# Test the derivative for x**2
print("Testing x**2 ...")
func = derivative(lambda x: x**2, x)
_derivative = np.round(func, 3)
print(_derivative)
error = (np.sum(np.round(func - 2*x, 3)))
print("PASSED:", error == 0.0, "\n")


# Test the derivative for x**3
print("Testing x**3 ...")
func = derivative(lambda x: x**3, x)
_derivative = np.round(func, 3)
print(_derivative)
error = (np.sum(np.round(func - 3*x**2, 3)))
print("PASSED:", error == 0.0, "\n")


# Test the derivative for sin(x)
print("Testing sin(x) ...")
func = derivative(lambda x: np.sin(x), x)
_derivative = np.round(func, 3)
print(_derivative)
error = (np.sum(np.round(derivative(lambda x: np.sin(x), x) - np.cos(x), 3)))
print("PASSED:", error == 0.0, "\n")