from linked_list import LinkedList
from linked_list import CircularList

if __name__ == '__main__':

	list1 = CircularList([1,2,3,4,5,5,6,6,7])
	print(list1)
	list1.add_link_before(5,100)
	print(list1.get_front())
	print(list1.get_back())
	print(list1.is_empty())
	print(list1.contains(1))
	print(list1.contains(6))
	print(list1.contains(8))



