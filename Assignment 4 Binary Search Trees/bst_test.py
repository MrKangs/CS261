from bst import Student, BST


if __name__ == '__main__':
	tree = BST()
	print(tree)
	tree.add(18)
	tree.add(5)
	tree.add(5)
	tree.add(20)
	tree.add(25)
	tree.add(2)
	tree.add(1)
	tree.add(8)
	tree.add(10)
	tree.add(30)
	tree.add(9)
	print(tree)
	tree.add(15)
	tree.add(15)
	print(tree)
	tree.add(5)
	print(tree)
	print(tree.get_first())
	print(tree.contains(18))
	print(tree.contains(100))
	print(tree.contains(25))
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
	
