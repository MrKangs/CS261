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
        if self._size == self._capacity:
            self._upsize()

        self._list[self._size] =  val
        self._size = self._size + 1

    def _upsize(self):
        # If the array hits the limits, it will expand the size of the array by double

        new_List = np.empty([self._capacity * 2], np.int16)

        for k in range(self._size):
            new_List[k] = self._list[k]
        
        self._list = new_List
        self._capacity = self._capacity * 2


    def _removeRandomValue(self):
        # This function exsits because when you print it you get an random value of the end of the array which will remove it
        
        new_List = np.empty([self._size - 1], np.int16)

        for k in range(self._size -1):
            new_List[k] = self._list[k]
        
        self._list = new_List

    def remove(self, val):
        # This function will remove the element that is equal to val, not the position of it

        for k in range(self._size - 1):
            if self._list[k] == val:
                self._list = np.delete(self._list, k)
        
        self._removeRandomValue()

    def clear(self):
        # This function will clear the list and return an empty array: basically resetting the array 
        self._size = 0
        new_List = np.empty([self._capacity], np.int16)
        self._list = new_List

    def count(self):
        # This function will count how many element is in the list
        return self._size

    def get(self,index):
        # This funcion will give the element value in that index position
        return self._list[index]

    def pop(self):
        last_Element = self._list[self._size]
        self._removeRandomValue()
        return last_Element
    '''
    def insert(self, index, val):
        # FIXME
    
    '''
student_list = StudentList()
print(student_list)
for i in range(4):
  student_list.append(i* 50)
  print(student_list)

print(student_list.count())
print(student_list.get(1))

student_list.remove(0)
print(student_list)

student_list.clear()
print(student_list)

for i in range(4):
  student_list.append(i)
  print(student_list)

print(student_list.pop())
print(student_list)

