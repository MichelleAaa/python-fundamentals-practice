class Stack:
    def __init__(self):
        self.items = []

# These three methods are wrappers around the built-in Python list methods called append() and pop(), and Python's built-in len() function.

#push an item to the top of the stack
    def push(self, value):
        self.items.append(value)

#pop an item off the end
    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()
# Note that you could write the above also like this:
# def pop(self):
    #if len(self.items) == 0:
        #return None
    #return self.items.pop()

# find the size of the stack
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.size() == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.size() == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")
