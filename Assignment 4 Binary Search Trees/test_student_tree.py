"""
@@ CS 261 Assignment 4 - Binary Search Tree Tester
@@ Solution Test Script
@author: Martin Edmunds
"""

"""Change this import depending on BST file name"""
from bst import BST, Student
from gradescope_utils.autograder_utils.decorators import weight
import unittest


# Helper function for building BSTs
# Args - Values: Array of values to be added to the BST
# Return - populated BST
def build_BST(values):
    tree = BST()
    for val in values:
        tree.add(val)
    return tree


# Tests the BST to ensure that all values are in the tree
# Helper function for testing remove
# Args
#   values - list of values that SHOULD be in the BST
#   tree   - BST tree to search
def test_contains(tree, values):
    for val in values:
        if not tree.contains(val):
            return False
    return True


# Class for testing the student node methods:
#   __lt__, __gt__, __eq__, __str__
class TestStudentClass(unittest.TestCase):

    @weight(2)
    def test_student_lt(self):
        """Tests to see if the student has a lt method implemented"""
        student1 = Student(10, "lesser_student")
        student2 = Student(12, "greater_student")
        self.assertLess(student1, student2)

    @weight(2)
    def test_student_gt(self):
        """Tests to see if the student has a gt method implemented"""
        student1 = Student(10, "lesser_student")
        student2 = Student(12, "greater_student")
        self.assertGreater(student2, student1)

    @weight(2)
    def test_student_eq(self):
        """Tests to see if the student has a eq method implemented"""
        student1 = Student(10, "student")
        student2 = Student(10, "another_student")
        self.assertEqual(student1, student2)
        student1 = Student(10, "student")
        student2 = Student(15, "student")
        self.assertNotEqual(student1, student2)

    @weight(3)
    def test_student_str(self):
        """Tests to see if the student has a str method implemented"""
        str_method = getattr(Student, "__str__", None)
        # check that it exists
        self.assertIsNotNone(str_method)
        # check that it's callable
        self.assertTrue(callable(str_method))
        # check that it's different from default behavior
        test_student = Student(10, "test_student")
        self.assertNotEqual(str(test_student), repr(test_student))


# Class for testing the student node methods:
#   add(value)
#   pre_order_traversal, post_order_traversal
#   contains(value)
#   left_child()
#   remove(value)
#   remove_first()
class TestStudentBinaryTree(unittest.TestCase):
    def test_init(self):
        """Checks that the list initializes correctly"""
        new_tree = BST()
        self.assertTrue(hasattr(new_tree, 'root'))
        self.assertIsNone(new_tree.root)

    @weight(6)
    def test_add_node_primitives(self):
        """Tests that nodes containing primitive data are added to the binary tree in the correct position"""
        test_values = [15, 0, -5, 5, 20, 25, 17]
        new_tree = build_BST(test_values)
        # Expected Tree:
        #                     15
        #                 0       20
        #              -5   5  17    25

        # test node at root
        self.assertEqual(new_tree.root.val, test_values[0])

        # test node left of root
        self.assertEqual(new_tree.root.left.val, test_values[1])

        # test node right of root
        self.assertEqual(new_tree.root.right.val, test_values[4])

        # test left node left of root
        self.assertEqual(new_tree.root.left.left.val, test_values[2])

        # test node right of left root
        self.assertEqual(new_tree.root.left.right.val, test_values[3])

        # test node right of right root
        self.assertEqual(new_tree.root.right.right.val, test_values[5])

        # test left-most node of right root
        self.assertEqual(new_tree.root.right.left.val, test_values[6])

    @weight(6)
    def test_add_node_student(self):
        """Tests that nodes containing student data are added to the binary tree in the correct position"""
        test_students = [Student(15, "Root"), Student(0, "Root->Left"), Student(-5, "Root->L->L"),
                         Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                         Student(17, "Root->R->L")]
        # Expected Tree (Grades):
        #                     15
        #                 0       20
        #              -5   5  17    25

        student_tree = build_BST(test_students)
        self.assertEqual(student_tree.root.val, test_students[0])
        self.assertEqual(student_tree.root.left.val, test_students[1])
        self.assertEqual(student_tree.root.right.val, test_students[4])
        self.assertEqual(student_tree.root.left.left.val, test_students[2])
        self.assertEqual(student_tree.root.left.right.val, test_students[3])
        self.assertEqual(student_tree.root.right.right.val, test_students[5])
        self.assertEqual(student_tree.root.right.left.val, test_students[6])

    @weight(9)
    def test_pre_order_traversal(self):
        """Tests student pre-order-traversal implementation"""
        test_students = [Student(15, "Root"), Student(0, "Root->Left"), Student(-5, "Root->L->L"),
                         Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                         Student(17, "Root->R->L")]
        # Expected Tree (Grades):
        #                     15
        #                 0       20
        #              -5   5  17    25
        student_tree = build_BST(test_students)

        # 15 -> 0 -> -5 -> 5 -> 20 -> 17 -> 25
        validated_traversal = [Student(15, "Root"), Student(0, "Root->Left"), Student(-5, "Root->L->L"),
                               Student(5, "Root->L->R"), Student(20, "Root->R"), Student(17, "Root->R->L"),
                               Student(25, "Root->R->R")]

        student_traversal = student_tree.pre_order_traversal()
        for i in range(0, len(validated_traversal)):
            self.assertEqual(validated_traversal[i], student_traversal[i])

    @weight(9)
    def test_post_order_traversal(self):
        """Tests student post-order-traversal implementation"""
        test_students = [Student(15, "Root"), Student(0, "Root->Left"), Student(-5, "Root->L->L"),
                         Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                         Student(17, "Root->R->L")]
        # Expected Tree (Grades):
        #                     15
        #                 0       20
        #              -5   5  17    25
        student_tree = build_BST(test_students)

        # -5 -> 5 -> 0 -> 17 -> 25 -> 20 -> 15
        validated_traversal = [Student(-5, "Root->L->L"), Student(5, "Root->L->R"), Student(0, "Root->Left"),
                               Student(17, "Root->R->L"), Student(25, "Root->R->R"), Student(20, "Root->R"),
                               Student(15, "Root")]

        student_traversal = student_tree.post_order_traversal()
        for i in range(0, len(validated_traversal)):
            self.assertEqual(validated_traversal[i], student_traversal[i])

    @weight(8)
    def test_contains_bs_tree(self):
        """Tests that nodes added to the BST can be located"""
        test_values_true = [15, 0, -5, 5, 20, 25, 17, 3, -3, 15]
        test_values_false = [-100, 100, -1, 1, -15]
        new_tree = build_BST(test_values_true)

        # ensure values added are in the tree
        for val in test_values_true:
            self.assertTrue(new_tree.contains(val))
        # ensure values not added are not in the tree
        for val in test_values_false:
            self.assertFalse(new_tree.contains(val))

    @weight(6)
    def test_left_child(self):
        """Tests the left_child implementation of the student tree"""
        test_students = [Student(15, "Root"), Student(0, "Root->Left"), Student(-5, "Root->L->L"),
                         Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                         Student(17, "Root->R->L")]
        # Expected Tree (Grades):
        #                     15
        #                 0       20
        #              -5   5  17    25
        student_tree = build_BST(test_students)
        # start node = root
        self.assertEqual(Student(-5, "Root->L->L"), student_tree.left_child(student_tree.root).val)
        # start node = root.left
        self.assertEqual(Student(-5, "Root->L->L"), student_tree.left_child(student_tree.root.left).val)
        # start node = root.right
        self.assertEqual(Student(17, "Root->R->L"), student_tree.left_child(student_tree.root.right).val)
        # start node = root.right.right
        self.assertEqual(Student(25, "Root->R->R"), student_tree.left_child(student_tree.root.right.right).val)

    @weight(20)
    def test_remove(self):
        """Tests that nodes can be removed from the binary search tree"""
        # test_values = [15, 0, -5, 5, 20, 25, 17]
        test_values = [Student(15, "Root"), Student(0, "Root->L"), Student(-5, "Root->L->L"),
                       Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                       Student(17, "Root->R->L")]
        new_tree = build_BST(test_values)
        # Starting Tree:
        #                     15
        #                 0       20
        #              -5   5  17    25
        #

        # Test 1
        # delete root, replace with left-most node of right child
        new_tree.remove(Student(15, "Root"))
        test_values.remove(Student(15, "Root"))
        # Expected Tree:
        #                     17
        #                 0       20
        #              -5   5        25
        self.assertEqual(new_tree.root.val.grade, 17)
        self.assertEqual(new_tree.root.right.val.grade, 20)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 2
        # delete root, replace with left-most node of right child
        new_tree.remove(Student(17, "Root->R->L"))
        test_values.remove(Student(17, "Root->R->L"))
        # Expected Tree:
        #                     20
        #                 0       25
        #              -5   5
        self.assertEqual(new_tree.root.val.grade, 20)
        self.assertEqual(new_tree.root.right.val.grade, 25)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 3
        # delete root, replace with left-most node of right child
        new_tree.remove(Student(20, "Root->R"))
        test_values.remove(Student(20, "Root->R"))
        # Expected Tree:
        #                     25
        #                 0
        #              -5   5
        self.assertEqual(new_tree.root.val.grade, 25)
        self.assertIsNone(new_tree.root.right)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 4
        # delete 5
        new_tree.remove(Student(5, "Root->L->R"))
        test_values.remove(Student(5, "Root->L->R"))
        # Expected Tree:
        #                    25
        #                 0
        #              -5
        self.assertEqual(new_tree.root.val.grade, 25)
        self.assertIsNone(new_tree.root.right)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        self.assertIsNone(new_tree.root.left.right)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 5
        # delete single child node
        new_tree.remove(Student(0, "Root->L"))
        test_values.remove(Student(0, "Root->L"))
        # Expected Tree:
        #                 25
        #              -5
        self.assertEqual(new_tree.root.val.grade, 25)
        self.assertIsNone(new_tree.root.right)
        self.assertEqual(new_tree.root.left.val.grade, -5)
        self.assertIsNone(new_tree.root.left.right)
        self.assertIsNone(new_tree.root.left.left)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 6
        # delete root when replaced with node that has right child
        test_values = [Student(15, "Root"), Student(0, "Root->L"), Student(-5, "Root->L->L"),
                       Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                       Student(17, "Root->R->L"), Student(19, "Root->R->L->R")]
        new_tree = build_BST(test_values)
        # Starting Tree:
        #                     15
        #                 0       20
        #              -5   5  17    25
        #                        19
        new_tree.remove(Student(15, "Root"))
        test_values.remove(Student(15, "Root"))
        # Expected Tree:
        #                     17
        #                 0       20
        #              -5   5  19    25
        #
        self.assertEqual(new_tree.root.val.grade, 17)
        self.assertEqual(new_tree.root.right.val.grade, 20)
        self.assertEqual(new_tree.root.right.left.val.grade, 19)
        self.assertEqual(test_contains(new_tree, test_values), True)

    @weight(4)
    def test_remove_first(self):
        """Tests the remove_first method"""
        # test_values = [15, 0, -5, 5, 20, 25, 17]
        test_values = [Student(15, "Root"), Student(0, "Root->L"), Student(-5, "Root->L->L"),
                       Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                       Student(17, "Root->R->L")]
        new_tree = build_BST(test_values)
        # Starting Tree:
        #                     15
        #                 0       20
        #              -5   5  17    25
        #

        # Test 1
        # delete root, replace with left-most node of right child
        new_tree.remove_first()
        test_values.remove(Student(15, "Root"))
        # Expected Tree:
        #                     17
        #                 0       20
        #              -5   5        25
        self.assertEqual(new_tree.root.val.grade, 17)
        self.assertEqual(new_tree.root.right.val.grade, 20)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 2
        # delete root, replace with left-most node of right child
        new_tree.remove_first()
        test_values.remove(Student(17, "Root->R->L"))
        # Expected Tree:
        #                     20
        #                 0       25
        #              -5   5
        self.assertEqual(new_tree.root.val.grade, 20)
        self.assertEqual(new_tree.root.right.val.grade, 25)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 3
        # delete root, replace with left-most node of right child
        new_tree.remove_first()
        test_values.remove(Student(20, "Root->R"))
        # Expected Tree:
        #                     25
        #                 0
        #              -5   5
        self.assertEqual(new_tree.root.val.grade, 25)
        self.assertIsNone(new_tree.root.right)
        self.assertEqual(new_tree.root.left.val.grade, 0)
        # ensure the remaining values are in the tree
        self.assertEqual(test_contains(new_tree, test_values), True)

        # Test 4
        # Continue removing until tree is empty
        # remove 25
        new_tree.remove_first()
        # Expected Tree:
        #                 0
        #              -5   5

        # Test 5
        # remove 0
        new_tree.remove_first()
        # Expected Tree:
        #                 5
        #              -5

        # Test 6
        # remove 5
        new_tree.remove_first()
        # Expected Tree:
        #              -5

        # Test 7
        # remove -5
        new_tree.remove_first()
        # Expected Tree:
        #              new_tree.root = None
        self.assertIsNone(new_tree.root)

    @weight(3)
    def test_get_first(self):
        """Tests the get_first method"""
        # test_values = [15, 0, -5, 5, 20, 25, 17]
        test_values = [Student(15, "Root"), Student(0, "Root->L"), Student(-5, "Root->L->L"),
                       Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
                       Student(17, "Root->R->L")]
        new_tree = build_BST(test_values)
        # Starting Tree:
        #                     15
        #                 0       20
        #              -5   5  17    25
        #

        # Test 1
        # get root value of tree
        self.assertEqual(new_tree.get_first(), Student(15, "Root"))

if __name__ == '__main__':
    unittest.main()