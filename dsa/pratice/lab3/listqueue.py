queue = []
queue.append('A')
queue.append('b')
queue.append('c')

print(queue)

top = queue[0]
print(top)

popelement = queue.pop(0)
print(popelement)
print("Queue after Dequeue: ", queue)

isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(queue))
