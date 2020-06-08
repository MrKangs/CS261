# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
        	key: key of node
        Return:
        	node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets.
    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """
        self._buckets = []
        for i in range(self.capacity):
            self._buckets.append(LinkedList())
        self.size = 0

    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        hashKey = self._hash_function(key) % self.capacity
        target_node = self._buckets[hashKey].contains(key)
        if target_node is not None:
            return target_node.value
        else:
            return None 


    def resize_table(self, capacity):
        """
        Resizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing
        Args:
            capacity: the new number of buckets.
        """

        newBuckets = []
        for i in range(capacity):
            newBuckets.append(LinkedList())

        for i in range(self.capacity):
            if self._buckets[i].head is not None:
                newBuckets[i] = self._buckets[i]
        
        self._buckets = newBuckets
        self.capacity = capacity


    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """

        hashKey = self._hash_function(key) % self.capacity
        # case 1 - put('four', 4)
        # ['four', 4] -> ['one', 1] -> ['two', 2] -> ['three', 3]

        # put('one', 1)    hash_func('one') -> 5 % 6 = 5
        # put('two', 2)    hash_func('two') -> 11 % 6 = 5
        # put('apple', 100)  hash_func('apple') ->  17 % 6 = 5

        # put('two', 150)   hash_func('two') -> 11 % 6 = 5

        # case 2 - put('two', 'abcd')
        # ['one': 1] -> ['two', 'abcd'] -> [ 'three', 3]

        target_node = self._buckets[hashKey].contains(key)

        if target_node is None:
            self.size += 1
            self._buckets[hashKey].add_front(key, value)
        
        else:
            target_node.value = value


    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """
        
        hashKey = self._hash_function(key) % self.capacity

        if self._buckets[hashKey].head is not None:
            self._buckets[hashKey].head = None
        else:
            return None

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """
        hashKey = self._hash_function(key) % self.capacity
        target_node = self._buckets[hashKey].contains(key)
        if target_node is not None:
            return True
        else:
            return False


    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """
        empty = 0

        for i in range(self.capacity):
            if self._buckets[i].size == 0:
                empty += 1

        return empty

    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """
        return self.size / self.capacity

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out
