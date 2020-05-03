class SLNode:
    def __init__(self):
        self.next = None
        self.data = None

class Stack:
    def __init__(self):
        """
        Initializes a stack with a head node with data(None)
        """
        self.head = None
        
        

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head!= None:             
            cur = self.head.next
            out = out + str(self.head.data)
            while cur != None:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def isempty(self): 
        """
        Checks whether the stack is empty or not
        """
        if self.head == None: 
            return True
        else: 
            return False

    def push(self,value): 
        
        """
        adds data at the top of the stack
        """
        newnode = SLNode()
        newnode.data = value

        if self.head == None:
         self.head = newnode   
      
        else: 
         newnode.next = self.head 
         self.head = newnode 

    def pop(self):
        
        """
        removes data from the top of the stack
        """
          
        if self.isempty():
          raise Exception("Stack underflow") 
          return None
              
        else: 
            topofStack = self.head 
            self.head = self.head.next
            return topofStack.data
            
    def peek(self):

        if self.isempty():
          raise Exception("Stack underflow") 
          return None
        else:  
          return self.head.data        

testStack = Stack() 
print(testStack.isempty())
testStack.push(2)    
testStack.push(4) 
testStack.push(8) 
print(testStack.isempty())
print(str(testStack))
print(testStack.pop())
print(testStack.pop())
testStack.peek()
print(testStack.pop())
print(testStack.isempty()) 
print(testStack.pop()) # This will give an error because there is nothing in the stack to use pop    