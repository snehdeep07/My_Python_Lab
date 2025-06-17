# How to use break and continue in Python
# Break statement
# The break statement is used to exit a loop prematurely when a certain condition is met.


# int_list = [2, 3, 4, 7, 8, 10, 9]

# for num in int_list:
#     if num % 2 == 0:
#         print("the even number in the list is:",num)
#         break
        
# for num in int_list:
#     print("the current numbers in the list:",num)
#     if num % 2 == 0:
#         print("the even number in the list is:",num)
#         break

for i in range(1,21):
    if i<10:
        continue
    print("the current numbers in the list:",i) 
        
