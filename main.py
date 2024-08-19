 PROBLEM : 

LL: Constructor
You are tasked with implementing a basic data structure: a singly linked list.

To accomplish this, you will create two classes, Node and LinkedList.

The Node class will represent an individual node within the linked list, while the LinkedList class will manage the overall list structure.

Your implementation should satisfy the following requirements:
1. Create a Node class with the following features:
1. A constructor that takes a value as an argument and initializes the value attribute of the node.
2. A next attribute, initialized to None, which will store a reference to the next node in the list.
2. Create a LinkedList class with the following features:
1. A constructor that takes a value as an argument, creates a new Node with that value, and initializes the head and tail attributes of the linked list to point to the new node.
2. A length attribute, initialized to 1, which represents the current number of nodes in the list.



** SOLUTION :

class Node:
    # Constructor for the Node class
    def __init__(self, value):
        # Set the value attribute for the Node
        self.value = value
        # Initialize the next attribute to None
        self.next = None

class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self, value):
        # Create a new Node with the given value
        new_node = Node(value)
        # Set the head attribute to the new Node
        self.head = new_node
        # Set the tail attribute to the new Node
        self.tail = new_node
        # Initialize the length attribute to 1
        self.length = 1




** DETAILED EXPLANATION : 

FOR PART 1 :

Line 2: class Node:

This line defines a class named Node. In Python, classes are used to create objects with specific properties and methods.
Line 4: def __init__(self, value):

The __init__ method is a special method in Python known as the constructor. It is automatically called when an object of the class is created.
The self parameter refers to the instance of the class being created, and value is the data that will be stored in the node.

Line 6: self.value = value
This line assigns the value passed to the constructor (value) to the value attribute of the Node instance. This value attribute will store the data of the node.

Line 8: self.next = None
This line initializes the next attribute of the node to None. 
The next attribute will be used to reference the next node in the linked list. Initially, it is set to None because the node is not connected to any other node when it is first created.


FOR PART-2 : 


Line 11: class LinkedList:

This line defines a class named LinkedList. The LinkedList class will manage the overall structure of the linked list, including operations such as adding, removing, and traversing nodes.
Line 13: def __init__(self, value):

The constructor for the LinkedList class. It initializes a new linked list with a single node containing the value passed as an argument.
Line 15: new_node = Node(value)

This line creates a new instance of the Node class by passing the value to the Node constructor. This new_node will be the first node in the linked list.
Line 17: self.head = new_node

The head attribute of the linked list is set to the new_node. The head points to the first node in the linked list.
Line 19: self.tail = new_node

The tail attribute of the linked list is also set to the new_node. The tail points to the last node in the linked list. Since the list currently contains only one node, the head and tail both point to this single node.
Line 21: self.length = 1

The length attribute is initialized to 1, representing the current number of nodes in the linked list.



** KEY CONCEPTS : 

Classes and Objects:

A class is like a blueprint for creating objects. The Node and LinkedList are classes that define the structure and behavior of the nodes and the linked list, respectively.
An object is an instance of a class. For example, new_node is an object of the Node class.
Constructor (__init__):

The __init__ method is a special method in Python that is used to initialize objects. It sets up the initial state of the object by assigning values to its attributes.
Attributes:

Attributes are variables that belong to an object. In the Node class, value and next are attributes. In the LinkedList class, head, tail, and length are attributes.
Linked List:

A linked list is a data structure consisting of a sequence of elements, where each element (node) contains data and a reference (or pointer) to the next element in the sequence.
Head and Tail:

The head is the first node in the linked list, and the tail is the last node. In a linked list with a single node, both the head and tail point to the same node.
Summary
The Node class is used to create individual nodes with a value and a pointer to the next node.
The LinkedList class manages the linked list, starting with a single node (both head and tail point to this node) and keeps track of the number of nodes with the length attribute.
This implementation is the foundation for more complex operations like adding, removing, and traversing nodes in a linked list.
