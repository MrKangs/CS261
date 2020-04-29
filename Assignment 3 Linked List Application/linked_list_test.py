from linked_list import LinkedList
from linked_list import CircularList

if __name__ == '__main__':

	list1 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ])
	print(list1)

	list1.remove_link(3)
	print(list1)


