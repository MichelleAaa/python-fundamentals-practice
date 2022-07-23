class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("1st Node") #	This instantiates an object of the Node class as the value for the variable named head.  -- Note that when this is created, the default value of self.next is none. We change that later, in the next line, when we instantiate the second node and set the head's next value to the 2nd node.
head.next = Node("2nd Node") # instantiates a second object of the Node class as the value for the head object's instance attribute head.next. This effectively creates a link from the first Node object to the second. 
head.next.next = Node("3rd Node") # instantiates a third object of the Node class as the value for the instance attribute head.next.next. This creates a link from the first Node object, to the second, to the third. 

print(head.value)
print(head.next.value)
print(head.next.next.value)

