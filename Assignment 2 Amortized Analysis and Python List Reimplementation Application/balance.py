# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False

# We need to set up as that with the correct order 
beginning_list = ["[","{","("]
ending_list = ["]","}",")"]

def is_balanced(input_string):
# This function will tell whether the parentheses is balanced or not 

    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:
        if i in beginning_list:
            stack.append(i)
        elif i in ending_list:
            position = ending_list.index(i)
            if((len(stack) > 0) and (beginning_list[position] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True

# Testing purpose 

#string = "{{(])}}"
#print("This " , string, " is ", is_balanced(string))

#string = "({{[]}})({})"
#print("This " , string, " is ", is_balanced(string))


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))