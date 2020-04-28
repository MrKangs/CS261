class SLNode:
    def __init__(self):
        self.next = None
        self.data = None

class Queue:
    def __init__(self):
        """
        Initializes a Queue with a head node and a tail node
        """
         
        self.head = self.tail = None

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
        Checks whether the queue is empty or not
        """
        if self.head == None: 
            return True
        else: 
            return False

    def enQueue(self,value): 
        
        """
        adds data to the end of the queue
        """
        newnode =  SLNode()
        newnode.data = value
        
        if self.tail == None:
         self.head = self.tail = newnode 
        else: 
         self.tail.next = newnode
         self.tail = newnode
         newnode.next = None

    def deQueue(self):
        
        """
        removes data from the front of the queue
        """
          
        if self.isempty():
          raise Exception("Queue underflow") 
          return None

            
        elif(self.head.next == self.tail): 
            self.head = self.tail
          
        else: 
            self.head = self.head.next    

testQueue = Queue() 
print(testQueue.isempty())
testQueue.enQueue(1)  
testQueue.enQueue(3) 
print(testQueue.isempty())
testQueue.enQueue(5) 
testQueue.enQueue(7)
print(str(testQueue))
testQueue.deQueue()
testQueue.deQueue()
testQueue.deQueue()
print(testQueue.isempty())
testQueue.deQueue()
print(str(testQueue))
print(testQueue.isempty())
testQueue.deQueue() # This will return an error because there is nothing to remove from the queue