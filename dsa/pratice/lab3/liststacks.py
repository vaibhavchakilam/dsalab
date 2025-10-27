stack = []
stack.append('A')
stack.append('b')
stack.append('c')

print(stack)

top = stack[-1]
print(top)

popelement = stack.pop
print(popelement)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))
