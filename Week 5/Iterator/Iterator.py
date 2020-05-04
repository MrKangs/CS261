# Here we implement a very simple linked list class that holds a value and next.

class SimpleLinkedListIterator:
    def __init__(self, head):
        self.head = head
        self.current = head

    # We must define an iter function even it is just returning the same object
    def __iter__(self):
        return self

    # This is the meat of the iterator where we advance and stop when we hit a None node
    def __next__(self):
        if self.current is None:
            raise StopIteration
        cur = self.current
        self.current = self.current.next
        return cur

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Initilizing the list

head = LinkedListNode(1)

prev = head

for i in range(2, 10):
    add_node = LinkedListNode(i)
    prev.next = add_node
    prev = add_node

# Using a whoe loop

print("While loop:")
next_node = head
while next_node is not None:
    print(next_node.val)
    next_node = next_node.next
print("\n\n")

# Using an iterator as intended

print("Using an iterator:")
for i in SimpleLinkedListIterator(head):
    print(i.val)
print("\n\n")

# Directly calling the iterator functions

print("Using iterator functions directly")
demo_iterator = SimpleLinkedListIterator(head)
print(demo_iterator.__next__().val)
print(demo_iterator.__next__().val)
print("now plugging into a for loop:")
for i in demo_iterator:
    print(i.val)
print("\n\n")