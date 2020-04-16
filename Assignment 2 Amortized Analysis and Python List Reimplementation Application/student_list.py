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


    '''
    def pop(self):
        # FIXME
    
    def insert(self, index, val):
        # FIXME
    
    def remove(self, val):
        # FIXME
    
    def clear(self):
        # FIXME
    
    def cout(self):
        # FIXME
    
    def get(self,index):
        # FIXME
    
    '''
student_list = StudentList()
print(student_list)
for i in range(17):
  student_list.append(i)
  print(student_list)
print(student_list)


