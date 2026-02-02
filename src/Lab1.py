# Print Simple message Example of single line comment
print("Hello World")

print("Hello","World")

print("Hello","World", sep='-')

'''
Example of single line comment
Read the inputs from user as two number
print on console
add these numbers 
print that numbers
'''
inputText = input("Please two numbers: ")
print("inputText1 =",inputText)
a,b = inputText.split()
c = int(a)+int(b)
print("A =",a)
print("B =",b)
print("c =",c)
