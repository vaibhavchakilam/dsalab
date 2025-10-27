class stack:
  def __init__(self):   
    self.stack = []
  def push(self,data):
    self.stack.append(data)
  def pop(self):
    if not self.stack:
        return 'empty'
   
    self.stack.pop()
  def peek(self):
    if not self.stack:
        return 'empty'
    return self.stack[-1]
  def display(self):  
    print(self.stack)    
st = stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.display()
print(st.pop())
st.display()
print(st.peek())

 