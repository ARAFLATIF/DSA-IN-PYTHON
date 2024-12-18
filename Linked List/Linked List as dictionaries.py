# Linked list representation as nested dictionaries
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# Print the value 23
print(head["next"]["next"]["value"])


Explanation:
Each node in the linked list is represented as a dictionary with two keys:
"value" stores the node's value.
"next" points to the next node (or None if it's the last node).
To access the value 23, you follow the chain of "next" references:
head["next"] gives the second node.
head["next"]["next"] gives the third node.
head["next"]["next"]["value"] gives the value 23.
