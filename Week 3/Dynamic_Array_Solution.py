import numpy as np

class Dynamic_Array:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        # The initial code was [4] for empty list, capacity = 4.
        # By running the initial code, it will return an error after getting up to [0 1 2 3]
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0
        # By changing to 17 or higher for [17] and capacity, it will return no error. 
        # But the code should not to do it without returning an error I believe.

    def __str__(self):
        return str(self._list[:self._size])   

    def append(self, val):
        if self._size == self._capacity:
            self._upsize()

        # Needs to check if there is room and call _upsize if there isn't
        self._list[self._size] =  val
        self._size = self._size + 1

    def _upsize(self):

        new_List = np.empty([self._capacity * 2], np.int16)

        for k in range(self._size):
            new_List[k] = self._list[k]
        
        self._list = new_List
        self._capacity = self._capacity * 2

my_list = Dynamic_Array()

# To begin with this will throw an index out of bounds error until you properly handle the capacity
# doubling.
for i in range(17):
  my_list.append(i)
  print(my_list)
print(my_list)