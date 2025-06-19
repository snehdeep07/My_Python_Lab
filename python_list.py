# # list in python
# # A list is a collection of items that can be of different types, including numbers, strings, and other lists.
# # Lists are mutable, meaning you can change their content after creation.   
# # l = [1,2,3.4,"snehdeep",False]

# l=[]
# l.append(29)
# l.append("october")
# l.append(2005)
# l.insert(0,"DOB")
# print(l)

# create a list of numbers from 1 to 50
# l=[]
# for i in range(1,51):
#     l.append(i)
#     print(i)

# l = [1,2,3.4,"snehdeep",False]
# print(len(l))

# l = [1,2,3,4]
# l[1]="snehdeep"
# print(l)

# l1=[1,2,3.4,"guddu"]
# l2=[4,5,6.5,"ramteke"]
# result1 = l1.append(l2)
# result2 = l2.extend(l1)
# # print("result of append:",result1)
# # print("result of extend:",result2)
# print("list after append:",l1)
# print("list after extend:",l2)

# Difference between append and extend
# The append() method adds a single element to the end of a list, 
# while the extend() method adds multiple elements from an iterable 
# (like another list) to the end of the list.

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# result_1=l1.append(l2)
# result_2=l2.extend(l1)
# print("list after append:",l2)
# print("list after extend:",l1)


# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# l1.append(l2)
# print("list after append:", l1)
# print("lenght after append:",len(l1))


# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10
# l1.extend(l2)
# print("list after extend:", l1)
# print("lenght after extend:",len(l2))

# list slicing in python
# Slicing allows you to access a portion of a list by specifying a start and end index.
#  syntax: list[start:end:step]
l=[1,2,3,4,5,6,7]
# print("my_list :",l[0 :: 2])
# l[0 :: 2]) any number after second colon will skip
#  the - minus sign before the the element shows and display the 
print("my_list :",l[-2])
