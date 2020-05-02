from linked_list import LinkedList
from gradescope_utils.autograder_utils.decorators import weight
import unittest

class SLNode:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

def new_iter(self):
    self.iterator_cur = self.head.next
    return self

def new_next(self):
    if self.iterator_cur == self.tail:
        raise StopIteration
    data = self.iterator_cur.data
    self.iterator_cur = self.iterator_cur.next
    return data

def create_test_list(test_list):
    test_list.head.next = SLNode(0, SLNode(1, SLNode(2, SLNode(3, SLNode(4, test_list.tail)))))

def mock_iteration():
    LinkedList.__iter__ = new_iter
    LinkedList.__next__ = new_next

def generate_list(test_list):
    mock_iteration()
    out = []
    for i in test_list:
        out.append(i)
    return out

class TestStudentSinglyLinkedList(unittest.TestCase):
    def test_init(self):
        new_list = LinkedList()
        self.assertTrue(hasattr(new_list, 'head'))
        self.assertTrue(hasattr(new_list, 'tail'))
        self.assertIsNone(new_list.head.data)
        self.assertIsNone(new_list.tail.data)
    @weight(4)
    def test_insert_before(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.add_link_before(2.5,3)
        self.assertListEqual(generate_list(new_list), [0,1,2,2.5,3,4])
    @weight(4)
    def test_insert_before_empty(self):
        new_list = LinkedList()
        new_list.add_link_before(2.5,0)
        self.assertListEqual(generate_list(new_list), [2.5])
    @weight(2)
    def test_remove_link(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.remove_link(2)
        self.assertListEqual(generate_list(new_list), [0,1,3,4])
    @weight(3)
    def test_remove_link_first(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.remove_link(0)
        self.assertListEqual(generate_list(new_list), [1,2,3,4])
    @weight(3)
    def test_remove_link_last(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.remove_link(4)
        self.assertListEqual(generate_list(new_list), [0,1,2,3])
    @weight(5)
    def test_add_front(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.add_front(-1)
        self.assertListEqual(generate_list(new_list), [-1,0,1,2,3,4])
    @weight(5)
    def test_add_back(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.add_back(5)
        self.assertListEqual(generate_list(new_list), [0,1,2,3,4,5])
    @weight(2)
    def test_get_front(self):
        new_list = LinkedList()
        create_test_list(new_list)
        self.assertEqual(new_list.get_front(),0)
    @weight(2)
    def test_get_back(self):
        new_list = LinkedList()
        create_test_list(new_list)
        self.assertEqual(new_list.get_back(),4)
    @weight(5)
    def test_remove_front(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.remove_front()
        self.assertListEqual(generate_list(new_list), [1,2,3,4])
    @weight(5)
    def test_remove_back(self):
        new_list = LinkedList()
        create_test_list(new_list)
        new_list.remove_back()
        self.assertListEqual(generate_list(new_list), [0,1,2,3])
    @weight(2)
    def test_is_empty(self):
        new_list = LinkedList()
        self.assertTrue(new_list.is_empty())
        new_list.add_front(1)
        self.assertFalse(new_list.is_empty())

    def test_str(self):
        new_list = LinkedList()
        self.assertEqual(str(new_list), "[]")
        create_test_list(new_list)
        self.assertEqual(str(new_list), "[0 -> 1 -> 2 -> 3 -> 4]")
    @weight(2)
    def test_contains(self):
        new_list = LinkedList()
        create_test_list(new_list)
        self.assertTrue(new_list.contains(3))
        self.assertFalse(new_list.contains(42))
    @weight(6)
    def test_remove(self):
        new_list = LinkedList()
        new_list.head.next = SLNode(0, SLNode(1, SLNode(6, SLNode(2, SLNode(3, new_list.tail)))))
        new_list.remove(6)
        self.assertListEqual(generate_list(new_list), [0,1,2,3])


        

if __name__ == '__main__':
    unittest.main()