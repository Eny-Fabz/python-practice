# So what I understood is with recursion, the function calls itself.
def recursive_factorial(x):
    if x == 0 or x == 1:
        return 1 #This code will stop the recursion
    else:
        return x * recursive_factorial(x - 1) # This will keep on multiplying x by a number less than it until x reaches 1. It does this by calling itself again and again thus recursion
# An example
print(recursive_factorial(8))