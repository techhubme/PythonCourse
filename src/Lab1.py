# Print Simple message
print("Hello World")

print("Hello","World")

print("Hello","World", sep='-')

inputText = input("Please two numbers: ")
print("Input =",inputText)

a,b = inputText.split()
c = int(a)+int(b)
print("A =",a)
print("B =",b)
print("c =",c)