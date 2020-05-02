from linked_list import CircularList
import unittest

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None

def forward_iter(self):
    self.iterator_cur = self.sentinel.next
    return self

def forward_next(self):
    if self.iterator_cur == self.sentinel:
        raise StopIteration
    data = self.iterator_cur.data
    self.iterator_cur = self.iterator_cur.next
    return data

def backward_iter(self):
    self.iterator_cur = self.sentinel.prev
    return self

def backward_next(self):
    if self.iterator_cur == self.sentinel:
        raise StopIteration
    data = self.iterator_cur.data
    self.iterator_cur = self.iterator_cur.prev
    return data

def create_test_list(test_list):
    prev = test_list.sentinel
    for i in range(5):
        cur = DLNode()
        cur.data = i
        cur.prev = prev
        prev.next = cur
        prev = cur
    cur.next = test_list.sentinel
    test_list.sentinel.prev = cur

def mock_iteration_forward():
    CircularList.__iter__ = forward_iter
    CircularList.__next__ = forward_next

def mock_iteration_backward():
    CircularList.__iter__ = backward_iter
    CircularList.__next__ = backward_next

def generate_student_lists(test_list):
    forward = []
    backward = []
    mock_iteration_forward()
    for i in test_list:
        forward.append(i)
    mock_iteration_backward()
    for i in test_list:
        backward.append(i)
    return [forward, backward]

def generate_solution_lists(list):
    return([list, list[::-1]])

class TestStudentCircularDoublyLinkedList(unittest.TestCase):
    def test_init(self):
        new_list = CircularList()
        self.assertTrue(hasattr(new_list, 'sentinel'))
        self.assertIsNone(new_list.sentinel.data)
    def test_insert_before(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.add_link_before(2.5,3)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([0,1,2,2.5,3,4]))
    def test_insert_before_empty(self):
        new_list = CircularList()
        new_list.add_link_before(2.5,0)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([2.5]))
    def test_remove_link(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.remove_link(2)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([0,1,3,4]))
    def test_remove_link_first(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.remove_link(0)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([1,2,3,4]))
    def test_remove_link_last(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.remove_link(4)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([0,1,2,3]))
    def test_add_front(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.add_front(-1)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([-1,0,1,2,3,4]))
    def test_add_back(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.add_back(5)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([0,1,2,3,4,5]))
    def test_get_front(self):
        new_list = CircularList()
        create_test_list(new_list)
        self.assertEqual(new_list.get_front(),0)
    def test_get_back(self):
        new_list = CircularList()
        create_test_list(new_list)
        self.assertEqual(new_list.get_back(),4)
    def test_remove_front(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.remove_front()
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([1,2,3,4]))
    def test_remove_back(self):
        new_list = CircularList()
        create_test_list(new_list)
        new_list.remove_back()
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([0,1,2,3]))
    def test_is_empty(self):
        new_list = CircularList()
        self.assertTrue(new_list.is_empty())
        new_list.add_front(1)
        self.assertFalse(new_list.is_empty())

    def test_str(self):
        new_list = CircularList()
        self.assertEqual(str(new_list), "[]")
        create_test_list(new_list)
        self.assertEqual(str(new_list), "[0 <-> 1 <-> 2 <-> 3 <-> 4]")
    def test_contains(self):
        new_list = CircularList()
        create_test_list(new_list)
        self.assertTrue(new_list.contains(3))
        self.assertFalse(new_list.contains(42))
    def test_remove(self):
        new_list = CircularList()
        prev = new_list.sentinel
        for i in reversed(range(5)):
            cur = DLNode()
            cur.data = i
            cur.prev = prev
            prev.next = cur
            prev = cur
        cur.next = new_list.sentinel
        new_list.sentinel.prev = cur
        new_list.remove(3)
        self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([4,2,1,0]))
    def test_reverse_list(self):
            new_list = CircularList()
            create_test_list(new_list)
            new_list.circularListReverse()
            self.assertListEqual(generate_student_lists(new_list), generate_solution_lists([4,3,2,1,0]))
   

        

if __name__ == '__main__':
    unittest.main()