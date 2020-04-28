from linked_list import LinkedList
from linked_list import CircularList


if __name__ == '__main__':

	list1 = LinkedList([1, 2, 3])
	print(list1)
	list1.add_back(5)
	print(list1)
	list1.remove_front()
	print(list1)
	print(list1.contains(2))

	list2 = LinkedList()
	list2.add_front('A')
	list2.add_front('B')
	list2.add_front('C')
	print(list2)

	list3 = CircularList([1, 2, 3, 3, 4, 5])
	print(list3)
	list3.circularListReverse()
	print(list3)

