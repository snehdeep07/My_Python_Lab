#  set in python
# empty set
# A set is an unordered collection of unique elements.
# sets are mutable and does not support indexing
# sets are used to store multiple items in a single variable

# set1 = set()
# print(type(set1))

# # type dictionary
# s={}
# print(type(s))

# set2 = {1,1,2,3,4,5,6,6,7}
# # print(set2)

# how to iterate element in set
# set2 = {1,2,3,4,5,2,3,2,1,4,5,6}
# for i in set2:
#     print(i)

# # covert ouput of set into list
# list1 = [1,2,3,2,3,2,4,4,5,5,7,6,8]
# set3 = set(list1)
# print(set3)

# to insert element in a set
# # # .add()
# set4 = set()
# set4.add(1)
# set4.add(2)
# set4.add(2)
# set4.add(3)
# set4.add(4)
# print(set4)

# # to update element in a set
# tmp = [1,2,3,4,5,5,6,7,8]
# set4.update(tmp)
# print(set4)

# # to calculate the lenght of the set
# print(len(set4))

# union operator
# set_a={1,2,3,4,5}
# set_b={4,5,6,7,8}
# print(set_a | set_b)

# intersection operator
# print(set_a & set_b)

# #  difference in set
# print(set_a - set_b)
# print(set_b - set_a)

# set comparison
set_b={1,2,3,4,5}
set_c={1,2,3,4,5}
print(set_b == set_c)
