# Print Simple message Example of single line comment
print("Hello World")

print("Hello", "World")

print("Hello", "World", sep='-')

print("Hello", end="\t")

# print special character
print("Hello\nGuys")
print("Python\tProgramming")

'''
Example of single line comment
Read the inputs from user as two number
print on console
add these numbers 
print that numbers
'''
# inputText = input("Please two numbers: ")
# print("inputText1 =", inputText)
# a, b = inputText.split()
# c = int(a) + int(b)
# print("A =", a)
# print("B =", b)
# print("c =", c)

# Multi-variable assignment
numa="10"
numb="20"
inuma, inumb = int(numa), int(numb)
sum = inuma + inumb
print(sum)


multiLineText = '''
This is a multi-line comment.
It spans multiple lines.
'''
print(multiLineText)

a = "Namaste"
b = "Hello"
c = "Namaskāram"

sentence = f"Sanskrit = {a}; English = {b}; Malayalam = {c}"
print(sentence)