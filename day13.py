from collections import deque

class Stack:
  def __init__(self):
    self.container=deque() 
  def push(self,val):
    self.container.append(val)
    return val #append to right(FIFO)
  def pop(self):
    return self.container.pop() #delete element from right side
  def peek(self):
    return self.container[-1] #first element of stack
  def is_empty(self):
    return len(self.container)==0 #whether stack is empty
  def size(self):
    return len(self.container)  # size of the stack
  def show(self):
    return self.container #display elements present in the stack


s=Stack()
print("\n\n\n")
print(f"the element added is",s.push(3))
print(f"the element added is",s.push(4))
print(f"the element added is",s.push(5))
print(f"the stack : ",s.show())
print("element poped",s.pop())
print(f"the stack : ",s.show())
print(f"the peek element",s.peek())
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")





'''def reverse(val): #reverse the text given
  stack=Stack()
  for word in val:
      stack.push(word)
  return_val=''
  for i in range(len(val)):
    return_val+=stack.pop()
  print(return_val)

reverse("We will conquere COVID-19")'''