# Arithmatic / Numerical operators in python
# + for addition
# - for substraction
# * multiplication
# / float division
# // for integer division
# ** for power calculation
# % modulus

# x=5
# y=3
# print("addition of x+y",x + y)
# print("substraction of x-y",x - y)
# print("multiplication of x*y",x * y)
# print("float division  of x/y",x / y)
# print("integer divison  of x//y",x // y)
# print("power calculation of x**y",x ** y)
# print("modulus of x%y",x % y)

# string operations
# string concatenation
# str_name = "snehdeep"
# full_name = str_name + " " + "vilas" +  " " + "ramteke"
# print("full name is ",full_name)

# multiply_numeric_str = "snehdeep" *5
# print("multiply numeric str = ",multiply_numeric_str)

# assignment operator
# Used to assign values to variables
# Operator	Example	Equivalent To
# =	a = 5	Assign 5 to a
# +=	a += 2	a = a + 2
# -=	a -= 2	a = a - 2
# *=	a *= 2	a = a * 2
# /=	a /= 2	a = a / 2
# //=	a //= 2	a = a // 2
# %=	a %= 2	a = a % 2
# **=	a **= 2	a = a ** 2

# comparison operator
# use to compare values (returns true or false)
# Operator	Description	Example
# ==	Equal to	a == b
# !=	Not equal to	a != b
# >	Greater than	a > b
# <	Less than	a < b
# >=	Greater or equal	a >= b
# <=	Less or equal	a <= b
# a=10
# b=5
# print("result of a==b",a==b)
# print("result of a==b",a!=b)
# print("result of a==b",a>b)
# print("result of a==b",a<b)
# print("result of a==b",a>=b)
# print("result of a==b",a<=b)

# logical operator
# Used to combine conditional statements:

# Operator	Description	Example
# and	Logical AND	a > 5 and b < 10  -> TRUE ,TRUE = TRUE
# or	Logical OR	a > 5 or b < 10   -> SINGLE TRUE = TRUE
# not	Logical NOT	not(a > 5)        -> TRUE = FALSE = TRUE
a=10
b=8
print("a>10 and b<10",a>10 and b<10)
print("a>10 or b<10",a>10 or b<10)
print("a>b", not (a>10 and b<10))
