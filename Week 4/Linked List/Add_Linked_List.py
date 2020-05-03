class Node:
  def __init__(self, val=None):
    self.next = None
    self.val = val

#This insert function cuts off the list and needs to be fixed
def insert(value, head, index):
  cur = head
  for i in range(index):
    cur = cur.next
  new_node = Node(value)
  new_node.next = cur.next
  cur.next = new_node
# cur.next = Node(value) This was the only statement in, I added line 11 to 13 to make it work


def print_list(head):
  cur = head
  while cur != None:
    cur = cur.next
    if cur != None:
      print(cur.val)
  print("End of list.\n")


#Build a simple list
head = Node()
cur = head

for i in range(5):
  cur.next = Node()
  cur = cur.next
  cur.val = i

print_list(head)
insert("Hi!", head, 3)

#This should print 0, 1, 2, Hi!, 3, 4, End of list. but our insert
#cuts off the tail of the list
print_list(head)
