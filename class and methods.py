# Define a class named Cookie
class Cookie:
    # Constructor method to initialize the object with a 'color' attribute
    def __init__(self, color):
        self.color = color  # Assign the passed 'color' value to the object's 'color' attribute
        
    # Method to get the current color of the cookie
    def get_color(self):
        return self.color  # Return the value of the 'color' attribute
        
    # Method to set or change the color of the cookie
    def set_color(self, color):
        self.color = color  # Update the object's 'color' attribute with the new value
        
# Create an instance of the Cookie class with an initial color of 'green'
cookie_one = Cookie('green')

# Create another instance of the Cookie class with an initial color of 'blue'
cookie_two = Cookie('blue')

# Print the color of cookie_one using the get_color() method
print('Cookie one is', cookie_one.get_color())

# Print the color of cookie_two using the get_color() method
print('Cookie two is', cookie_two.get_color())

# Change the color of cookie_one to 'yellow' using the set_color() method
cookie_one.set_color('yellow')

# Print the updated color of cookie_one
print('Cookie one is', cookie_one.get_color())

# Print the color of cookie_two again to show that it remains unchanged
print('Cookie two is', cookie_two.get_color())




Detailed Explanation:

1. Class Definition

class Cookie:
  
A class in Python is a blueprint for creating objects. Here, we define a class named Cookie.
The Cookie class will allow us to create objects (cookies) that have a specific color and methods to interact with that color.

2. Constructor Method (__init__)

def __init__(self, color):
    self.color = color
  
The __init__ method is called automatically whenever a new object (instance) of the class is created.
It initializes an object by setting its attributes. In this case, it sets an attribute called color.
self refers to the specific instance of the class being created. For example, when cookie_one is created, self refers to cookie_one.
  
3. Getter Method (get_color)

def get_color(self):
    return self.color
  
This method allows us to access (or "get") the value of an object's color attribute.
It returns self.color, which is the current value of the color attribute for a particular object.

4. Setter Method (set_color)

def set_color(self, color):
    self.color = color
  
This method allows us to modify (or "set") the value of an object's color attribute.
It updates self.color with a new value passed as an argument.

5. Creating Objects

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

These lines create two separate instances (objects) of the Cookie class:
cookie_one is initialized with a color of 'green'.
cookie_two is initialized with a color of 'blue'.
Each object has its own independent copy of attributes and methods.

6. Accessing Object Attributes

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

These lines use the get_color() method to retrieve and print the colors of both cookies:
For cookie_one, it prints 'green'.
For cookie_two, it prints 'blue'.

7. Modifying Object Attributes

cookie_one.set_color('yellow')
This line uses the set_color() method to change the color of cookie_one from 'green' to 'yellow'.

8. Printing Updated Attributes

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

The first line prints 'yellow', showing that cookie_one's color has been updated.
The second line still prints 'blue', demonstrating that modifying one object does not affect other objects.




Key Concepts Illustrated in This Code: 

Object-Oriented Programming:
The code demonstrates how classes and objects work in Python.
Each object (e.g., cookie_one, cookie_two) is an independent instance of the class.

Encapsulation:
The attributes (color) are encapsulated within each object.
They can only be accessed or modified through methods like get_color() and set_color().

Constructor (__init__):
The constructor initializes each object with specific values (e.g., 'green', 'blue').

Instance Methods:
Methods like get_color() and set_color() operate on specific instances (e.g., they act on either cookie_one or cookie_two, depending on which object calls them).

Object Independence:
Each object maintains its own state (attributes). Changing one object's state does not affect others.  


output of the code : 

Cookie one is green
Cookie two is blue
Cookie one is yellow
Cookie two is blue


This output shows:
Initially, each cookie has its own unique color (green and blue).
After modifying cookie_one, its color changes to 'yellow', but this does not affect cookie_two.
