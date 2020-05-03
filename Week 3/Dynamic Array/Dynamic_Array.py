import numpy as np

class Dynamic_Array:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])   

    def _upsize(self):
      # This should double the capacity of the numpy array and copy over the old array, but is incomplete
        new_data = np.empty([self._capacity * 2], np.int16)

    def append(self, val):
        # Needs to check if there is room and call _upsize if there isn't
        self._list[self._size] =  val
        self._size = self._size + 1

my_list = Dynamic_Array()

# To begin with this will throw an index out of bounds error until you properly handle the capacity
# doubling.
for i in range(17):
  my_list.append(i)
  print(my_list)
print(my_list)