class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

#new node becomes the head
    def push(self, value):
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head

        self.head = new_node
        self.num_nodes += 1
# remove the head:
    def pop(self):
        if self.head is None:
            return None
# saves the current head's value to pop_node
        pop_node = self.head.value
        #sets the next value as self.head, which removes the current head from the stack.
        self.head = self.head.next
        self.num_nodes -= 1
        return pop_node # returns the value that was popped off the stack.

# Instantiate an object from the Stack class, push items to it, then run a few tests to make sure all went well:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.num_nodes == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.num_nodes == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")

