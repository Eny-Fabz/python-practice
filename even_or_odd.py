def even_or_odd(value):
    if value % 2 == 0: # So I learnt this function will divide the number by 2 in order to check if it is even or odd
        return "Even" # When the number I supply is divisible by 2, this is the text that will display
    else:
        return "Odd" # So when the number I supply is not divisible by 2, now this is the text that will display
# So I tested the value of 57 to check if the code works
print(even_or_odd(57))