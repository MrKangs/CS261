#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Program Filename: student_list.py

# Author: Kenneth Kang

# Date: 4-18-2020

# Description: This program rewrite append, remove, clear, insert, get, count, and pop functions for the dynamic arrays.

# Input: For append, it will be a value from the user. For remove, it will be value that the user wants to remove. 
#        For clear, it will clear the array. For insert, it will add the value that the user input in the certain position by the user input.
#        For pop, it will take the last data value in the array and remove it from the array. For count, it will count how many data values is in the array.
#        And for get, it will get the data value in a certain position by the user input.  

# Output: There will be no output unless the user remove the comments below from the following message: Testing (To test this, remove the comments).
#         If the user removes it, it will return the following output from each functions: description from either the function comments or in the input part. 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import numpy as np
class StudentList:
    def __init__(self):
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def append(self, val):
        # This function will add an item into the list
        
        # If somehow it size counter leaders to 0, then reset the list 
        # (This happens when you pop all the items from the list).
        if self._size == 0:
            self.__init__()

        # If the size counter is the max of the list size, then go to _upsize()
        # that will expand the list by double.
        if self._size == self._capacity:
            self._upsize()

        # Add the item in the list and increase the counter by 1.
        self._list[self._size] = val
        self._size = self._size + 1

    def insert(self, index, val):
        # This function will add an element in the index position of data of val.

        # Same as append function, if the size and cap is equal to each other, 
        # then increase the list size.
        if self._size == self._capacity:
            self._upsize()
        
        # This will insert the item of val from the user input in the list, 
        # where the user index position is.
        self._list = np.insert(self._list, index, val)

        # As the user enter a new value into the list, the size counter will increase by 1. 
        self._size = self._size + 1

    def _upsize(self):
        # If the array hits the limits, it will expand the size of the array by double.

        # We first set the counter of capacity double from previous.
        self._capacity = self._capacity * 2

        # We reset a new list with the new capacity value in the list.
        new_List = np.empty([self._capacity], np.int16)

        # We copy all the old data value from the old list into the new list.
        for k in range(self._size):
            new_List[k] = self._list[k]

        # Once copying is complete, then we declare that the new list will be the current list.
        self._list = new_List


    def remove(self, val):
        # This function will remove one element that is equal to val, not the position of it

        # First we set up an indicator whether if there is a 
        # data value from the user input, val, exist in the list.
        i = 0

        # This will run a cycle of all the list item value until it finds one, then delete it.
        for k in range(self._size):
            if self._list[k] == val:
                self._list = np.delete(self._list, k)
                # Once the item is deleted, then it will go to the reorganize function. 
                self.reorganize()
                # This will tell that there was an element in the list. 
                i = 1
                break
        # If there is no element that is in the list, then it will return a message as the following.
        if i == 0:
            print("There is no element in the array that is equal to ", val)
    
    def pop(self):
        # This function will do the pop function, which take the last element value and remove it from the list

        # If there is no element in the list, it is impossible to execute pop, 
        # so it will return the following message. 
        if self._size == 0:
            return print("There is no element in the array to use pop")
        
        # We set that the last_Element is equal from the last element value in the list.         
        last_Element = self._list[self._size - 1]

        # Once we set the last_Element value, it will go to the reorganize function. 
        self.reorganize()

        # It will return the last_Element value. 
        return last_Element

    def reorganize(self):
        # This function exsits because when you print it you get an random value of the end of the array which will remove it

        # Set the size counter -1 from the previous value.
        self._size = self._size - 1

        # Same idea but opposite from _upsize function. It will have a -1 from the previous cap value. 
        new_List = np.empty([self._size ], np.int16)

        # We copy all the old data value from the old list into the new list.
        for k in range(self._size ):
            new_List[k] = self._list[k]

        # Once copying is complete, then we declare that the new list will be the current list.
        self._list = new_List

    def clear(self):
        # This function will clear the list and return an empty list: basically resetting the list.
        
        # Setting the size counter to 0 will reset the list.
        self._size = 0

        # This is a message to the user that the list is clear. 
        return print("The list is clear!")

    def count(self):
        # This function will count how many element is in the list.

        # Letting the user know that how many elements are in the list.
        print("There are total of ", self._size, " of element(s) in the list!")
        
        # Return the value of the number of elements in the list. 
        return self._size

    def get(self, index):
        # This funcion will give the element value in that index position.

        # This will tell the user the value in that index position.
        print("In that position, the value of the element is ", self._list[index])

        # Return the value from that position of index that user input to the function. 
        return self._list[index]

# Testing (To test this, remove the comments)
#my_list = StudentList()

#my_list.append(1)
#print(my_list)
#print(my_list.count())

# And so on for more testing, type it by yourself.