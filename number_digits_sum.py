# Here, the code is to add the digits in a given number together. So if I have 768 it should give the value of 7+6+8
def number_digits_sum(digits):
    final = 0
    while digits > 0: # This line will loop the below code unless "digits" equals to 0
        final += digits % 10 # This takes the final digit in the number and adds it to the variable final which was initially 0. It will then continue for all the remaining digits
        digits //= 10 #This code on the other hand ensures digits will reach 0 so that the loop ends
    return final
# An example:
print(number_digits_sum(2222))