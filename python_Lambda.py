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
# concate = lambda a,b: a+b
# result =concate("Hello,","world! ")
# print(result)

# # lambda function to calculate maximum of two numbers
# max_num = lambda a,b: a if a>b else b
# a=25
# b=30
# print(max_num(a,b))

# how map(), reduce(), filter() function works
# list1 =[1,2,3,4,5,6,7,8,9,10,11,12]
# square_num=lambda x:x*x
# square_list=list(map(square_num, list1))
# print(square_list)


# list2 =[1,2,3,4,5,6,7]
# list3=[7,6,5,4,3,2,1]
# sum_of_lists=lambda x,y:x+y
# result=list(map(sum_of_lists,list2,list3))
# print(result)
# # ouput [8, 8, 8, 8, 8, 8, 8]


# # reduce () in python
# import functools
# multiplication_of_lists =lambda x,y:x*y
# result=functools.reduce(multiplication_of_lists, list2)
# print(result)


# filter () in python
# filter() is used to filter elements from an iterable based on a condition.
list2 =[1,2,3,4,5,6,7]
odd_numbers=lambda x :x%2 != 0
print(list(filter(odd_numbers,list2)))

list2 =[1,2,3,4,5,6,7]
even_numbers=lambda x :x%2 == 0
print(list(filter(even_numbers,list2)))
