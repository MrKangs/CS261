from linked_list import LinkedList
from linked_list import CircularList

if __name__ == '__main__':

	list1 = LinkedList([1, 2])
	print(list1)
	list1.remove_back()
	list1.remove_back()
	list1.remove_back()
	print(list1)
	print(list1.get_front())
	print(list1.is_empty())
	list1.add_back(5)
	print(list1.is_empty())
	list1.remove_back()
	list1.add_link_before(4,0)
	list1.add_link_before(3,0)
	list1.add_link_before(5,1)
	list1.add_link_before(3,0)

	print(list1)
	list1.add_link_before(5, 200)
	list1.add_link_before(5, -2)
	
	print(list1.contains(3))
	print(list1.contains(2))
	list1.remove_back()
	list1.remove_back()
	list1.remove_back()
	list1.remove_back()
	print(list1.contains(3))

