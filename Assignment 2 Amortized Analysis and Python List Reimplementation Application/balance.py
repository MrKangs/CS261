#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Program Filename: balance.py

# Author: Kenneth Kang

# Date: 4-18-2020

# Description: This program will tell whether or not the parentheses are balanece or not from using stacks

# Input: A string value that contains parentheses.

# Output: Whether or not the parenthese are balances or not. 

# Note: A balancing parentheses will be like: {[({}[]())]}, while unbalanced will be like {[])({})}. 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys

# We need to set up as that with the correct order 
beginning_list = ["[","{","("]
ending_list = ["]","}",")"]

def is_balanced(input_string):
# This function will tell whether the parentheses is balanced or not 

    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:

        # If there is an item that matches the beginning_list, then add into the stack.
        if i in beginning_list:
            stack.append(i)

        # If there is an item that matches the ending_list, then save the position of that value.
        elif i in ending_list:
            position = ending_list.index(i)
            # Since right before value must be the exactly opposite value, which it must be paired with in the beginning_list,
            # If the right before value matches in the beginning_list and the stack length is greather than 0, then it will pop
            # the beginning_list value because we don't care any more.  
            if((len(stack) > 0) and (beginning_list[position] == stack[len(stack) - 1])):
                stack.pop()
            # If it doesn't follow, then that is a flaw, which it is unbalanced. 
            else:
                return False

    # If the length of the stack is 0, since it will all pass the test, the parentheses are balanced.
    if len(stack) == 0:
        return True


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))

# Testing purpose 

#string = "{{(])}}"
#print("This " , string, " is ", is_balanced(string))

#string = "({{[]}})({})"
#print("This " , string, " is ", is_balanced(string))