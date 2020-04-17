# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================
# Stacks are a very commonly used abstract data type. 
# Applications of stacks include implementation of reverse Polish notation expression evaluation and undo buffers. 
# Stacks can also be used to check whether an expression has balanced parentheses, braces, and brackets (,{,[or not. 
# For example, expressions with balanced parentheses are "(x + y)", "{x + (y + z)}" and with unbalanced are "(x+y", "[x + (y+ z])".

# In this section, you will use a stack to implement a program that checks if a string is balanced. 
# Use the skeleton code provided below to accept inputs via command line arguments. 
# Do not modify how the inputs are accepted as this is how we will test your code. 
# Be sure you handle a NULL input string; you can either consider a NULL string as balanced or ensure that the input string cannot be empty.

# You are to fill in the missing code for is_balanced() which must be implemented with a stack (no counter integers or string functions are allowed). 
# If you use a counter or string operation of any kind, you will not receive credit for completing this part of the assignment. 
# You may use Python's implementation of a list and you may add additional functions as you see fit. 

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False

def is_balanced(input_string):

    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:

        # FIXME: You will write this function

        return False


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))