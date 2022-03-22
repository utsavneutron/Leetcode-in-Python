# Recursion
# -------------------------
# A way of solving a problem by having a fuction call itself
# Performing same operation multiple times with different inputs
# 
# Why Recursion?
# Helps you break down big problems with smaller ones and easier to use
# 
# When to choose Recursion?
# If you can divide the problem into similar sub problems like:

# Design an algorithm to compute nth....
# Write a code to list the n..
# Implement a method to compute all
#
# A method calls itself
# Iteration has better time and space complexity than recursion

# When to avoid Recursion?
# Quick Working solution instead of efficient one
# Traverse a tree
# Memoization in recursion
# 
# Avoid When:
# Time and space complexity matters
# Recursion uses more memory
# Recursion can be slow

# 3 Steps to write Recursion
# Recursive case - the flow
# Base case - the stopping criterion
# unintentional case - the constraint
# 
# 

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)

openRussianDoll(3)

# Step 1: Recursive case - The flow: 1+1+2+3+5+8+13+21+.....
# Step 2: Base case: For 1 and 2 return 1 and for any number less than 1 return 0
def fibonacci(num):
    assert num>=0 and int(num) ==num, "The number must be positive integer"
    if(num == 1 or num == 0):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


# def fibonacci(num):
#     sum = 0
#     curr = 1
#     while num > 0:
#         temp = sum
#         sum = sum + curr
#         curr = temp
#         num -= 1
    
#     return sum


print(fibonacci(2))



# def powerOfTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo(n-1)
#         return power *2

# print(powerOfTwo(3))
 
def factorial (n):
    assert n >=0 and int(n) == n, "The number must be positive integer only"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))