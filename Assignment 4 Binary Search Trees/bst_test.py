from bst import Student, BST


if __name__ == '__main__':
	tree = BST([20,10,30,5,15,25,35,2,7,12,16,22,23,27,33,37])
	print(tree)
	print(tree.pre_order_traversal())
	print(tree.post_order_traversal()) 
	print(tree.get_first())
	print(tree.left_child(20).val)
	print(tree)


	bst2 = BST()

	student1 = Student(15, "Sasha")
	student2 = Student(0, "Sasha")
	student3 = Student(20, "Sasha")
	student4 = Student(-5, "Sasha")
	student5 = Student(5, "Sasha")
	student6 = Student(17, "Sasha")
	student7 = Student(25, "Sasha")

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

	
