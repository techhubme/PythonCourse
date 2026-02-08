# 1. Types of Variables in Python

# studentName = "Ram Niwash"
# age = 23
# feeAmount = 456.3
# profileEnabled = True
# print(f"Student Name = {studentName}, Age = {age}, Fee = {feeAmount}, Profile Enabled = {profileEnabled}")
# print("Type Of Student Name =",type(studentName))
# print("Type Of Student Age =",type(age))
# print("Type Of Student Fee =",type(feeAmount))
# print("Type Of Profile Enabled =",type(profileEnabled))

# 2. Variable Naming Rules

## Invalid Variable
# 1studentName = "Ram Niwash"
# class = "MCA";
# my-variable = 5

## Valid Variable
# _1studentName = "Ram Niwash"
# my_age = 10
# _myAge = "23"
# myage123 = 25
# print(_1studentName)
# print(my_age)
# print(_myAge)
# print(myage123)

# 3. Multiple Ways to use Variables

## Assigning multiple values for multiple variables
# math, science, sanskrit, hindi = 50, 55, 60,70
# print(math)
# print(science)
# print(sanskrit)
# print(hindi)

## Same value for multiple variables
# math = science = sanskrit = hindi = 50
# print(math)
# print(science)
# print(sanskrit)
# print(hindi)
# malayalam, tamil = 50, 60
# print("*** Before Swap ***")
# print("Malayalam =", malayalam)
# print("Tamil =", tamil)
# malayalam, tamil = tamil, malayalam
# print("*** After Swap ***")
# print("Malayalam =", malayalam)
# print("Tamil =", tamil)

# 4. **`Try Out`** Uncomment the section and test

# v1, v2 = 10, 20
# print(v1, v2, v3)
# v1, v2, v3 = 10, 20
# print(v1, v2, v3)
# v1, v2, v3 = 10, "Hello", True
# print(v1, v2, v3)
# v1, v2, v3 = 10, 20,
# print(v1, v2, v3)

# 5. Deleting a Variable eligible for Garbage collection

# v1 = 10
# print(v1)
# del v1
# print(v1)

# 6. How to get the size and address of variable?
import sys

aNum = 123456
print("Size of aNum =", sys.getsizeof(aNum))
print("Address of aNum =", id(aNum))

bStr = "Hello World"
print("Size of bStr =", sys.getsizeof(bStr))
print("Address of bStr =", id(bStr))

cFlt = 6728.98
print("Size of cFlt =", sys.getsizeof(cFlt))
print("Address of cFlt =", id(cFlt))

dBool = True
print("Size of dBool =", sys.getsizeof(dBool))
print("Address of dBool =", id(dBool))

# 7. Constants in Python
PI = 3.14
print("PI = ",PI)
PI = 3.14159
print("PI = ",PI)