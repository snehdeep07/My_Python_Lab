# python for loop
# for loop is used  when the number of iterations are known
# for i in range (1,11):
#     print(i)
# i is variable here we can use any variable in place of i
# for i in range (1,101,2):
#     print(i)
# for i in range (10,0,-1):
#     print(i)

# write a program in python to print the sum of elements present in list
int_list = [5, 3, 7, 8, -2, 8]
total = 0

for number in int_list:
    total += number

print("The sum of total numbers in the list:", total)


