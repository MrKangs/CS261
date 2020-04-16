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
        
        #FIXME: If the capacity is 4 ,8, 16, 32, ..., then it returns an error

        for k in range(self._size):
            if self._list[k] == val:
                self._list = np.delete(self._list, k)
                print(self._list)
        
        self._removeRandomValue()

    def clear(self):
        # This function will clear the list and return an empty array
        
        #FIXME: Both Methods are not working...

        #for k in range(self._size):
         #   self._list = np.delete(self._list, k)
          #  self._removeRandomValue()
           # print(self._list)

        self._list = np.empty([self._capacity], np.int16)
        for k in range (self._capacity):
            self._removeRandomValue()

    '''
    def pop(self):
        # FIXME
    
    def insert(self, index, val):
        # FIXME
    
    def cout(self):
        # FIXME
    
    def get(self,index):
        # FIXME
    
    '''
student_list = StudentList()
print(student_list)
for i in range(8):
  student_list.append(i)
  print(student_list)

#student_list.remove(0)
#print(student_list)

student_list.clear()
print(student_list)


