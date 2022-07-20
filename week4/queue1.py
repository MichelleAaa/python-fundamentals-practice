class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

#self variable is a stand-in for the specific instance of the class that will be made later.
    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node  # Same as above two lines
        else:
            # set the reference of the tail's next value to the new node we just created
            self.tail.next = new_node
            # set the tail to be the new_node
            self.tail = new_node

        self.num_nodes += 1

    def dequeue(self):
        # is None means the queue is empty.
        if self.head is None:
            return None

# if there's something in the queue:
        # dequeue_node = self.head.value
        dequeue_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return dequeue_node_value

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue(4)
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
