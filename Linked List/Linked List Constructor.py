Class Node: 
def __init__(self, value):
  self.value = value
  self.next = None

Class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)

EXPLANATION : 

Node Class
Purpose: Represents an individual node in the linked list.
  
Attributes:
self.value: Stores the data value of the node.
self.next: Points to the next node in the list (initialized as None, meaning this is the last node by default).

LinkedList Class
Purpose: Manages the linked list by tracking its head, tail, and length.

Attributes:
self.head: Points to the first node of the list.
self.tail: Points to the last node of the list.
self.length: Tracks the number of nodes in the list.

Constructor:
Takes an initial value, creates a new Node with that value, and sets it as both the head and tail of the list.
Initializes the list with a length of 1 since it contains one node.
  
Example
my_linked_list = LinkedList(4):
Creates a linked list with one node (value=4).
Both head and tail point to this node.
Length is 1.
print(my_linked_list.head.value):
Accesses the value of the head node and prints 4.
