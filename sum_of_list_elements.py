# So the idea is to add all the digits in a list to find the total
def sum_of_list_elements(digits):
    total = 0
    for value in digits: # This will look for all the numbers in the list "digits"
        total += value # This will add the numbers and place the sum in the variable total
    return total

# So for example, using the following list below
print(sum_of_list_elements([9,5,3,4,23]))

# From writing all the code I have learnt that python/pycharm is space sensitive. For example, my "return total" was not working initially until I had to remove it from under the "for" loop