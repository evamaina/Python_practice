def extremes(nums):
    return(min(nums), max(nums))


# returns maximum magnitude
def max_magnitude(nums):
    return max(abs(num) for num in nums)

# returns the sum of all arguments that are divisible by two
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)



# returns the sum of all parameters that are floats
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)