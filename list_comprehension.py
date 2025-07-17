# [expression for item in iterable if condition]

# list1=[x for x in range(1,11)]
# print(list1)

# # to print the even numbers
# list2=[x for x in range(1,51) if x%2==0]
# print(list2)

# to convert the element in list into uppercase
# list3=['guddu','snehdeep','vilas','ujwala','ramteke']
# result = [x.upper() for x in list3]
# print(result)


# put all negative element after a positive element
list4=[-3,-5,-8,-1,1,4,5,6]
result1=[x for x in list4 if x>0]
result2=[x for x in list4 if x<0]
print(result1 + result2)
