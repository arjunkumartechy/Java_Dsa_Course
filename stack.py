# Procedural implementation of a Stack ADT
# You are NOT allowed to use Python classes or built-in stack structures.

def create_stack():
    """
    Creates and returns an empty stack.

    Returns:
    - stack (dict): A dictionary representing the stack.
    """
    return {
        "data": [],
        "top": -1
    }


def push(stack, value):
    """
    Pushes a value onto the stack.

    Parameter(s):
    - stack (dict): The stack.
    - value: The value to push.
    """
    stack["data"].append(value)
    stack["top"] += 1
    


def pop(stack):
    """
    Removes and returns the top value from the stack.

    Parameter(s):
    - stack (dict): The stack.

    Returns:
    - The value at the top of the stack.
    """
    if not is_empty(stack):
        stack["top"] -= 1
        return stack["data"].pop()


def is_empty(stack):
    """
    Checks whether the stack is empty.

    Parameter(s):
    - stack (dict): The stack.

    Returns:
    - True if the stack is empty, False otherwise.
    """
    return stack["top"] == -1