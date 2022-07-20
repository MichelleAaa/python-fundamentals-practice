class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#method that allows us to add nodes to a LinkedList object of this class
    def append(self, value):
        new_node = Node(value)
#If the LinkedList object does not yet have any nodes, its head attribute will be empty. In that case, this newly created Node object will be assigned to the head, we'll print a confirmation message, and the method will return (end).
        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        #if there is already a head node, we traverse it until we get to the tail node, which is the first node that has a next attribute of None.
        while node.next is not None:
            node = node.next
#Now that we are at the node that has a next value of none, we set it's node.next value to the new_node value we are adding. new_node is now the tail, as it's got the node.next value of none.
        node.next = new_node
        print("Appended new Node with value:", node.next.value)

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")


