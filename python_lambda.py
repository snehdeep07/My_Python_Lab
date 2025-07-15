# lambda function in python
# A lambda function is a small anonymous function that can take 
# any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not needed elsewhere in the code.
# syntax: lambda arguments: expression
# def square(a):
#     result = a*a
#     return result
# a=5
# print(square(a))

# Example of lambda function
# sqaure = lambda a: a*a
# print(square(5))

# def addition(num):
#     result = num + 5
#     return result
# x=7
# print(addition(x))

# # same code in python
# add_of_two_num = lambda a :a + 5
# a = 7
# print(add_of_two_num(a))

# addition = lambda a,b: a+b
# a=(int(input("enter a first number :" )))
# b=(int(input("enter a second number :" )))
# print("sum is :",addition(a , b))

# write a lambda function to concatenate two strings
concate = lambda a,b: a+b
result =concate("Hello,","world! ")
print(result)

# lambda function to calculate maximum of two numbers
max_num = lambda a,b: a if a>b else b
a=25
b=30
print(max_num(a,b))
