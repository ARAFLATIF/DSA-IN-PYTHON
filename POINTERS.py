Snippet 1: Immutable Objects (Integers)

# Assigning an integer value to num1
num1 = 11

# Creating a new reference to the same integer object
num2 = num1

print("Before num2 value  is updated:")
print("num1 =", num1)  # Output: 11
print("num2 =", num2)  # Output: 11

# Printing memory addresses of num1 and num2
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))  # Same as num1's address

# Assigning a new value to num2
num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)  # Still 11
print("num2 =", num2)  # Now 22

# Printing updated memory addresses
print("\nnum1 points to:", id(num1))  # Unchanged
print("num2 points to:", id(num2))  # New address for 22

OUTPUT : 

Before num2 value is updated:
num1 = 11
num2 = 11

num1 points to: 140721189736272
num2 points to: 140721189736272

After num2 value is updated:
num1 = 11
num2 = 22

num1 points to: 140721189736272
num2 points to: 140721189736592


Explanation for Snippet 1:
Initially, num1 and num2 refer to the same integer object (11).
When num2 is assigned a new value (22), it creates a new integer object.
num1 still refers to the original object (11), while num2 now refers to the new object (22).
This demonstrates that integers are immutable in Python. When you "change" an integer, you're actually creating a new object.



Snippet 2: Mutable Objects (Dictionaries)
python
# Creating a dictionary
dict1 = {
    'value': 11
}

# Creating a new reference to the same dictionary object
dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)  # Output: {'value': 11}
print("dict2 =", dict2)  # Output: {'value': 11}

# Printing memory addresses of dict1 and dict2
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))  # Same as dict1's address

# Modifying the dictionary through dict2
dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)  # Output: {'value': 22}
print("dict2 =", dict2)  # Output: {'value': 22}

# Printing memory addresses again
print("\ndict1 points to:", id(dict1))  # Unchanged
print("dict2 points to:", id(dict2))  # Still the same as dict1

OUTPUT : 

Before value is updated:
dict1 = {'value': 11}
dict2 = {'value': 11}

dict1 points to: 140721190591872
dict2 points to: 140721190591872

After value is updated:
dict1 = {'value': 22}
dict2 = {'value': 22}

dict1 points to: 140721190591872
dict2 points to: 140721190591872


Explanation for Snippet 2:
Initially, dict1 and dict2 refer to the same dictionary object.
When we modify the dictionary through dict2, it changes the single object that both variables refer to.
Both dict1 and dict2 reflect the change because they point to the same object in memory.
This demonstrates that dictionaries are mutable in Python. Modifying a dictionary doesn't create a new object; it changes the existing one.


Key Takeaways:
For immutable types (like integers), "modifying" a value creates a new object.
For mutable types (like dictionaries), modifying the object changes it in-place, affecting all references to that object.
The id() function shows the memory address of an object, helping visualize how variables reference objects in memory.
Understanding these concepts is crucial for working with data structures and avoiding unexpected behavior in Python programs.
