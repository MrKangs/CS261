from bst import Student, BST


if __name__ == '__main__':
	tree = BST([15, 0, -5, 5, 20, 25, 17])
	print(tree)
	print(tree.pre_order_traversal())
	print(tree.post_order_traversal()) 
	print(tree.get_first())
	print(tree.remove(15))
	print(tree)
	print(tree.remove(17))
	print(tree)
	print(tree.remove(20))
	print(tree)
	print(tree.remove(5))
	print(tree)
	print(tree.remove(0))
	print(tree)

	tree2 = BST([15,0,20,-5,5,17,25,19])
	print(tree2)
	print(tree2.remove(15))
	print(tree2)

'''
	bst2 = BST()

	student1 = Student(15, "A")
	student2 = Student(0, "B")
	student3 = Student(20, "C")
	student4 = Student(-5, "D")
	student5 = Student(5, "E")
	student6 = Student(17, "F")
	student7 = Student(25, "G")

	bst2.add(student1)
	bst2.add(student2)
	bst2.add(student3)
	bst2.add(student4)
	bst2.add(student5)
	bst2.add(student6)
	bst2.add(student7)
	print(bst2.left_child(student1).val)
	print(bst2.left_child(student2).val)
	print(bst2.left_child(student6).val)
	print(bst2.left_child(student7).val)
'''
	
