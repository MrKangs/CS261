# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out


    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if index < 0:
            return print("Exception: Index out of bounds! The bound is too low!")

        cur = self.head

        for i in range(index):
            cur = cur.next
            if cur is None:
                return print("Exception: Index out of bounds! The bound is too high!")

        new_link.next = cur.next
        cur.next = new_link

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        if self.head.next == self.tail:
            return False

        cur = self.head
        prev = None
        if index < 0:
            return print("Exception: Index out of bounds! The bound is too low!")
        if index == 0:
            self.remove_front()
            return True
        for i in range(index + 1):
            prev = cur          
            cur = cur.next
            if cur is None:
                return print("Exception: Index out of bounds! The bound is too high!")
            if cur.next == self.tail:
                self.remove_back()
                return True

        prev.next = cur.next
      

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        new_link.next = self.head.next
        self.head.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        
        cur = self.head
        while(cur.next != self.tail):
            cur = cur.next
        
        new_link.next = cur.next
        cur.next = new_link
        


    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """
        if self.head.next == self.tail:
            return "No element in the list!"

        return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        if self.head.next == self.tail:
            return "No element in the list!"

        cur = self.head
        while(cur.next != self.tail):
            cur = cur.next
        
        return cur.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """
        if self.head.next == self.tail:
            return False
        cur = self.head
        for i in range(1):
            cur = cur.next
        self.head = cur

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        if self.head.next == self.tail:
            return False       
        else:
            cur = self.head
            prev = None
            while(cur.next.next is not None):
                prev = cur
                cur = cur.next
            cur = prev
            prev.next = self.tail

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        if self.head.next == self.tail:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        if self.head.next == self.tail:
            return "No element in the list!"

        cur = self.head

        while(cur.next != self.tail):
            if cur.data == value:
                return True
            cur = cur.next
        
        return False
        

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        prev = None
        cur = self.head
        while cur:
            if cur.data == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True

            prev = cur
            cur = cur.next
        return False


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:             
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if index < 0:
            return print("Exception: Index out of bounds! The bound is too low!") 
        cur = self.sentinel
        for i in range (index):
            cur = cur.next
            if cur == self.sentinel:
                return print("Exception: Index out of bounds! The bound is too high!")
        
        new_link.next = cur.next
        new_link.prev = cur
        cur.next.prev = new_link
        cur.next = new_link


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        if index < 0:
            return print("Exception: Index out of bounds! The bound is too low!")        
        
        cur = self.sentinel

        for i in range (index):
            cur = cur.next
            if cur == self.sentinel:
                return print("Exception: Index out of bounds! The bound is too high!")

        cur.next.prev = cur.prev
        cur.prev.next = cur.next
        print("Did it work?")
        # FIXME: It is not working somehow....



    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        cur = self.sentinel

        new_link.next = cur.next
        new_link.prev = cur
        cur.next.prev = new_link
        cur.next = new_link


    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        cur = self.sentinel

        cur.prev.next = new_link
        new_link.prev = cur.prev.next
        new_link.next = cur
        cur.prev = new_link



    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        if self.sentinel.next.data is None:
            return "No element in the list!"

        return self.sentinel.next.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        if self.sentinel.prev.data is None:
            return "No element in the list!"

        return self.sentinel.prev.data


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXME: Write this function


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXME: Write this function

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        return self.sentinel.next == self.sentinel.prev is None


    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        if self.sentinel.next == self.sentinel.prev:
            return "No element in the list!"
        
        cur = self.sentinel

        while (cur.next != cur.prev != None):
            cur = cur.next
            if cur.data == value:
                return True
            if cur == self.sentinel:
                return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXME: Write this function

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """

        # FIXME: Write this function

