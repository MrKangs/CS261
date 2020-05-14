from bst import Student, BST


if __name__ == '__main__':
	tree = BST([20,10,30,5,15,25,35,2,7,12,16,22,27,33,37])
	print(tree)
	print(tree.pre_order_traversal())
	print(tree.post_order_traversal())
	print(tree.get_first())
	print(tree.contains(25))
	print(tree.contains(15))
	print(tree.contains(17))
	print(tree.contains(16))
	print(tree.contains(13))
	print(tree.contains(999))
	print(tree.contains(35))



	tree2 = BST()
	tree2.add(10)
	tree2.add(10)
	print(tree2)
	tree2.add(-1)
	print(tree2)
	tree2.add(5)
	print(tree2)
	tree2.add(-1)
	print(tree2)


	bst2 = BST()
	bst2.add(Student(88, "Sasha"))
	bst2.add(Student(94, "Rachel"))
	bst2.add(Student(93, "Phil"))
	bst2.add(Student(85, "Mike"))

	in_order = bst2.in_order_traversal()
	for i in in_order:
		print(i)
	
