# When we say factorial using loop, I found that it is a way to multiply integers together, from 1 to whatever number we give it
def factorial_with_loop(a): # I believe "a" here will be the number we end with.
    start = 1 #This is just to indicate we will begin multiplying from 1
    for b in range(1, a + 1):
        start *= b # This multiplies the successive numbers and stores it in the start variable
    return start # After multiplying all the values and storing it in start, the final answer is returned for display
# Trying it with the number 6 we get...
print(factorial_with_loop(6))