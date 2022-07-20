class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#The DoublyLinkedClass keeps references to both a head and a tail node, instead of only the head. 
# We can traverse from the head node to the tail node using the next attribute. 
# We can traverse from the tail node to the head node using the prev attribute.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

#If the list is empty: (That means there's nothing in there yet, so our new node becomes both the head and the tail of the list. )
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return
#If the list is not empty, and there is a head:

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)

dllist = DoublyLinkedList() # this creates the doublylinkedlist.
dllist.append("First Node") # this adds the first node.


"""
Check the head and tail values:
dllist.head.value
dllist.tail.value

Check the prev/next values of the head/tail:
dllist.head.next.value
dllist.tail.prev.value
(Note that yo uwill get errors if the value doesn't exdist yet since maybe you only have one item in the list right now, for example.)

You can keep chaining on to move down the list:
dllist.tail.prev.prev.value
dllist.head.next.next.value


"""
