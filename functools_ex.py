from functools import reduce

l = [1, 2, 3, 4, 5]



from functools import partial

# Example: Fix the first argument of a multiplication function
def multiply(x, y, z):
    return x * y * z
# Create a new function with x fixed at 2
double = partial(multiply, 2)
print(double(3, 4))  # Output: 24 (2 * 3 * 4)

# https://rajansahu713.medium.com/fuctools-python-package-every-developer-should-know-276a1f9e884f

# def f(p1, p2,/, p3, *, p4):
#     pass

l  = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x : x % 2 == 0, l))
print(even)


square = list(map(lambda x : x ** 2, l))
print(square)

#https://python.plainenglish.io/supercharge-your-python-functions-with-these-10-functools-tricks-e44270b79436

