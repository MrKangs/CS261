"""
@@ CS 261 Assignment 5 - HashMap Tester
@@ Solution Test Script
@author: Martin Edmunds
"""

"""Change this import depending on HashMap file name"""
from hash_map import HashMap, hash_function_1, hash_function_2
from gradescope_utils.autograder_utils.decorators import weight
import unittest
import random
import string


# Function that returns a key, value pair that can be added to the HashMap
# Arg: None
# Return: random (key, value) tuple
def create_random_tuple():
    low_limit = 5
    high_limit = 15
    key_length = random.randrange(low_limit, high_limit)
    key = ""
    for i in range(key_length):
        # add random characters to the key
        key += random.choice(string.ascii_letters)
    return key, key_length


# Function that iterates through the map's buckets adding all the keys to the list
# Arg: Student HashMap
# Returns: []: List of keys from the HashMap (without using HashMap functions)
def get_keys_from_map(map):
    to_return = []
    for bucket in map._buckets:
        cur_node = bucket.head
        while cur_node is not None:
            to_return.append(cur_node.key)
            cur_node = cur_node.next
    return to_return


# checks that a tuple control list is equal to a list of keys from a map
# Helper function for testing map removal
# Arg:  control_list = validated list with nodes removed
#       map_key_list = key list generated with get_keys_from_map function
# Return:
#   True - if control_list matches map_key_list
#   False - otherwise
def check_lists_are_equals(control_list, map_key_list):
    if len(control_list) != len(map_key_list):
        return False
    for val in control_list:
        if val[0] not in map_key_list:
            return False
    return True


# Class for testing the student node methods:
#   clear()
#   get(key)
#   resize_table(capacity)
#   put(key, value)
#   remove(self, key)
#   contains_key(key)
#   empty_buckets()
#   table_load()
class TestStudentHashMap(unittest.TestCase):
    def test_init(self):
        """Checks that the hash_table initializes correctly, if __init__ is provided, ignore"""
        student_map = HashMap(10, hash_function_1)
        self.assertEqual(10, student_map.capacity)
        self.assertEqual(0, student_map.size)
        self.assertEqual(hash_function_1, student_map._hash_function)
        for bucket in student_map._buckets:
            self.assertIsNone(bucket.head)

    @weight(10)
    def test_put(self):
        """Tests that HashMap put method"""
        first_node = ("test_val", 5)
        collision_node = ("test_5", 5)
        # these values give a good distribution of collisions and non-collisions
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]
        # Expected distribution with hf1
        #[]
        #[(test_5_, 5) -> (test_ - 5, -5)]
        #[(completely_different, 5) -> (anotha_one, -7) -> (set, 10) -> (another_word, 20)]
        #[]
        #[]
        #[(getting_there, -1)]
        #[(test_5, 5)]
        #[]
        #[(diff_word, 15)]
        #[]

        student_map = HashMap(10, hash_function_1)
        student_map_func2 = HashMap(10, hash_function_2)

        # add a single key/val pair to the table
        self.assertEqual(student_map.size, 0)
        self.assertEqual(student_map.capacity, 10)

        # add the value to both the maps
        student_map.put(first_node[0], first_node[1])
        student_map_func2.put(first_node[0], first_node[1])
        self.assertEqual(student_map.size, 1)

        # hash_function_1 expected location = bucket[6], head
        self.assertEqual(student_map._buckets[6].contains(first_node[0]).key, first_node[0])
        self.assertEqual(student_map._buckets[6].contains(first_node[0]).value, first_node[1])

        # hash_function_2 expected location = bucket[3], head
        self.assertEqual(student_map_func2._buckets[3].contains(first_node[0]).key, first_node[0])
        self.assertEqual(student_map_func2._buckets[3].contains(first_node[0]).value, first_node[1])

        # test same key update
        student_map.put(first_node[0], -5)
        self.assertEqual(student_map.size, 1)
        self.assertEqual(student_map._buckets[6].contains(first_node[0]).key, first_node[0])
        self.assertEqual(student_map._buckets[6].contains(first_node[0]).value, -5)

        # test collision add
        student_map.put(collision_node[0], collision_node[1])
        self.assertEqual(student_map._buckets[6].size, 2)
        self.assertEqual(student_map._buckets[6].contains(first_node[0]).key, first_node[0])
        self.assertEqual(student_map._buckets[6].contains(collision_node[0]).key, collision_node[0])

        # expected location = bucket[6], head
        self.assertIsNotNone(student_map._buckets[6].contains(first_node[0]))

        # add all key value pairs to the table
        for key, val in test_values:
            student_map.put(key, val)

        # check that cap didnt change
        self.assertEqual(student_map.capacity, 10)

        # check that the 10 unique values were added
        self.assertEqual(student_map.size, len(test_values) + 1)
        for key, val in test_values:
            found = False
            for bucket in student_map._buckets:
                if bucket.contains(key):
                    found = True
            self.assertTrue(found)

    @weight(5)
    def test_get(self):
        """Tests the HashMap get method"""
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]

        collision_values = [("completely_different", 5), ("anotha_one", -7), ("set", 10), ("another_word", 20)]
        head_node = collision_values[0]
        tail_node = collision_values[3]
        student_map = HashMap(10, hash_function_1)

        # add all key value pairs to the table
        for key, val in test_values:
            student_map.put(key, val)

        # test get at linked_list head
        self.assertEqual(student_map.get(head_node[0]), head_node[1])

        # test get at linked_list tail
        self.assertEqual(student_map.get(tail_node[0]), tail_node[1])

        # test get at > 2 collision bucket
        for node in collision_values:
            self.assertEqual(student_map.get(node[0]), node[1])

        # test get with no collision
        self.assertEqual(student_map.get("getting_there"), -1)

        # test that all values are in the list
        for node in test_values:
            self.assertEqual(student_map.get(node[0]), node[1])

    @weight(6)
    def test_contains_key(self):
        """Tests the HashMap contains_key method"""
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]

        student_map = HashMap(10, hash_function_1)

        # simple check to test that all values are in the list
        for key, val in test_values:
            student_map.put(key, val)
            found = False
            for bucket in student_map._buckets:
                if bucket.contains(key):
                    found = True
            self.assertEqual(found, student_map.contains_key(key))


    @weight(5)
    def test_table_load(self):
        """Tests HashMap table_load method"""
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20)]
        init_capacity = 10
        student_map = HashMap(init_capacity, hash_function_1)
        student_map_d = HashMap(init_capacity * 2, hash_function_1)
        # 0 / 10 = 0, 0 / 20 = 0
        self.assertEqual(student_map.table_load(), student_map_d.table_load())

        for key, val in test_values:
            student_map.put(key, val)
            student_map_d.put(key, val)

        # test known load ( 5 / 10 = 0.5 ),  ( 5 / 20 = 0.25 )
        self.assertEqual((len(test_values) / init_capacity), student_map.table_load())
        self.assertEqual((len(test_values) / (init_capacity * 2)), student_map_d.table_load())

        student_map = HashMap(init_capacity, hash_function_1)
        student_map_d = HashMap(init_capacity * 2, hash_function_1)

        # test high table load
        random_cases = 1000
        # add random key, value pairs to the table
        for i in range(random_cases):
            key, value = create_random_tuple()
            student_map.put(key, value)
            student_map_d.put(key, value)

        self.assertAlmostEqual(student_map.table_load(), student_map_d.table_load()*2)

    @weight(8)
    def test_remove(self):
        """Tests the HashMap remove method with both hash functions"""
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 12), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("tes", 8), ("anotha_one", -7), ("completely_different", 13), ("getting_there", -1)]
        student_map = HashMap(10, hash_function_1)
        student_map_hf2 = HashMap(10, hash_function_2)

        # get all keys from the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        self.assertEqual(len(sm_values), len(smhf2_values))
        self.assertEqual(0, len(sm_values))

        # add test values to the map
        for key, val in test_values:
            student_map.put(key, val)
            student_map_hf2.put(key, val)

        # get all keys from the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)

        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test1 - remove size 1 linked list bucket node (bucket 6)
        value_to_remove = ("test_5", 5)
        # remove the tuple from the control list
        test_values.remove(value_to_remove)
        # Remove the value from the maps
        student_map.remove(value_to_remove[0])
        student_map_hf2.remove(value_to_remove[0])
        # update keys found in the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test2 - remove size >1 linked list bucket node HEAD POSITION (bucket 2)
        value_to_remove = ("completely_different", 13)
        # remove the tuple from the control list
        test_values.remove(value_to_remove)
        # Remove the value from the maps
        student_map.remove(value_to_remove[0])
        student_map_hf2.remove(value_to_remove[0])
        # update keys found in the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test3 - remove size >1 linked list bucket node TAIL POSITION (bucket 2)
        value_to_remove = ("another_word", 20)
        # remove the tuple from the control list
        test_values.remove(value_to_remove)
        # Remove the value from the maps
        student_map.remove(value_to_remove[0])
        student_map_hf2.remove(value_to_remove[0])
        # update keys found in the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test4 - remove size >1 linked list bucket node MID POSITION (bucket 2)
        value_to_remove = ("tes", 8)
        # remove the tuple from the control list
        test_values.remove(value_to_remove)
        # Remove the value from the maps
        student_map.remove(value_to_remove[0])
        student_map_hf2.remove(value_to_remove[0])
        # update keys found in the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test5 - remove size >1 linked list bucket node
        value_to_remove = ("anotha_one", -7)
        # remove the tuple from the control list
        test_values.remove(value_to_remove)
        # Remove the value from the maps
        student_map.remove(value_to_remove[0])
        student_map_hf2.remove(value_to_remove[0])
        # update keys found in the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test6 - remove size >1 linked list bucket node
        value_to_remove = ("set", 10)
        # remove the tuple from the control list
        test_values.remove(value_to_remove)
        # Remove the value from the maps
        student_map.remove(value_to_remove[0])
        student_map_hf2.remove(value_to_remove[0])
        # update keys found in the map
        sm_values = get_keys_from_map(student_map)
        smhf2_values = get_keys_from_map(student_map_hf2)
        # check that all keys that are in test_values are in the map
        self.assertTrue(check_lists_are_equals(test_values, sm_values))
        self.assertTrue(check_lists_are_equals(test_values, smhf2_values))

        # test7 - remove value not in map (should do nothing)
        before_size_sm = student_map.size
        before_size_smhf2 = student_map_hf2.size
        student_map.remove("key_not_in_list")
        student_map_hf2.remove("key_not_in_list")
        self.assertEqual(before_size_sm, student_map.size)
        self.assertEqual(before_size_smhf2, student_map_hf2.size)


    @weight(6)
    def test_empty_buckets(self):
        """Checks the empty_buckets method"""
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]

        empty_buckets = initial_capacity = 10
        student_map = HashMap(initial_capacity, hash_function_1)
        self.assertEqual(empty_buckets, student_map.empty_buckets())

        empty_buckets = initial_capacity = 20
        student_map = HashMap(initial_capacity, hash_function_1)
        self.assertEqual(empty_buckets, student_map.empty_buckets())

        student_map.put("first_value", 5)
        self.assertEqual(empty_buckets - 1, student_map.empty_buckets())

        student_map = HashMap(10, hash_function_1)
        student_map_hf2 = HashMap(10, hash_function_2)
        for key, val in test_values:
            student_map.put(key, val)
            student_map_hf2.put(key, val)
        # should have 5 empty buckets with hash_function_1
        self.assertEqual(5, student_map.empty_buckets())
        # 4 with hash_function_2
        self.assertEqual(4, student_map_hf2.empty_buckets())


    @weight(15)
    def test_resize_table(self):
        """Tests the resize_table method: checks that links are not changed and properties are updated"""
        test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]
        student_map = HashMap(10, hash_function_1)
        for key, value in test_values:
            student_map.put(key, value)
        self.assertEqual(10, student_map.capacity)

        # get before resize state
        keys_before_resize = get_keys_from_map(student_map)
        size_before_resize = student_map.size

        # Test 1
        # resize the table smaller -> bigger
        student_map.resize_table(50)
        self.assertEqual(50, student_map.capacity)

        # get after resize state
        keys_after_resize = get_keys_from_map(student_map)
        size_after_resize = student_map.size

        # test that no nodes were lost in the resize
        self.assertEqual(len(keys_before_resize), len(keys_after_resize))
        self.assertEqual(size_before_resize, size_after_resize)
        for key in keys_before_resize:
            self.assertTrue(key in keys_after_resize)
        for key in keys_after_resize:
            self.assertTrue(key in keys_before_resize)

        # Test 2
        student_map = HashMap(10, hash_function_1)
        for key, value in test_values:
            student_map.put(key, value)
        self.assertEqual(10, student_map.capacity)

        # get before resize state
        keys_before_resize = get_keys_from_map(student_map)
        size_before_resize = student_map.size

        # resize the table bigger -> smaller
        student_map.resize_table(5)
        self.assertEqual(5, student_map.capacity)

        # get after resize state
        keys_after_resize = get_keys_from_map(student_map)
        size_after_resize = student_map.size

        # test that no nodes were lost in the resize
        self.assertEqual(len(keys_before_resize), len(keys_after_resize))
        self.assertEqual(size_before_resize, size_after_resize)
        for key in keys_before_resize:
            self.assertTrue(key in keys_after_resize)
        for key in keys_after_resize:
            self.assertTrue(key in keys_before_resize)


if __name__ == '__main__':
    unittest.main()