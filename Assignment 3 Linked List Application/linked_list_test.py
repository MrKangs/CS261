from linked_list import LinkedList
from linked_list import CircularList

if __name__ == '__main__':


	list1 = LinkedList([1,2,3,4,5])
	list2 = CircularList([4,5,6])
	# This place is a tester for the code for linked_list.py
	# If you want to test functions for each section, then write it out below those two statements 
	# or add elements in the array for each statments if you want to have an initital elements inside
	# Check out the pdf file in this folder to know which function does which
	print(list1)
	list1.remove_link(0)
	print(list1)
	print(list2)
	list2.circularListReverse()
	print(list2)


