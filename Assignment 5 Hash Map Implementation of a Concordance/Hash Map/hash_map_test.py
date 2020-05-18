from hash_map import *


""" EMPTY BUCKETS """
print("\n\n********   EMPTY_BUCKETS()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(100, hash_function_1)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key1', 10)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key2', 20)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key1', 30)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key4', 40)
print(m.empty_buckets(), m.size, m.capacity)

print("--- EXAMPLE 2 ---")
m = HashMap(50, hash_function_1)
for i in range(150):
    m.put('key' + str(i), i * 100)
    if i % 30 == 0:
        print(m.empty_buckets(), m.size, m.capacity)


""" TABLE LOAD """
print("\n\n********   TABLE_LOAD()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(100, hash_function_1)
print(m.table_load())
m.put('key1', 10)
print(m.table_load())
m.put('key2', 20)
print(m.table_load())
m.put('key1', 30)
print(m.table_load())

print("--- EXAMPLE 2 ---")
m = HashMap(50, hash_function_1)
for i in range(50):
    m.put('key' + str(i), i * 100)
    if i % 10 == 0:
        print(m.table_load(), m.size, m.capacity)


""" CLEAR """
print("\n\n********   CLEAR()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(100, hash_function_1)
print(m.size, m.capacity)
m.put('key1', 10)
m.put('key2', 20)
m.put('key1', 30)
print(m.size, m.capacity)
m.clear()
print(m.size, m.capacity)

print("--- EXAMPLE 2 ---")
m = HashMap(50, hash_function_1)
print(m.size, m.capacity)
m.put('key1', 10)
print(m.size, m.capacity)
m.put('key2', 20)
print(m.size, m.capacity)
m.resize_table(100)
print(m.size, m.capacity)
m.clear()
print(m.size, m.capacity)


""" PUT """
print("\n\n********   PUT   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(50, hash_function_1)
for i in range(150):
    m.put('str' + str(i), i * 100)
    if i % 25 == 24:
        print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

print("--- EXAMPLE 2 ---")
m = HashMap(40, hash_function_2)
for i in range(50):
    m.put('str' + str(i // 3), i * 100)
    if i % 10 == 9:
        print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


""" CONTAINS KEY """
print("\n\n********   CONTAINS_KEY()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(50, hash_function_1)
print(m.contains_key('key1'))
m.put('key1', 10)
m.put('key2', 20)
m.put('key3', 30)
print(m.contains_key('key1'))
print(m.contains_key('key4'))
print(m.contains_key('key2'))
print(m.contains_key('key3'))
m.remove('key3')
print(m.contains_key('key3'))

print("--- EXAMPLE 2 ---")
m = HashMap(75, hash_function_2)
keys = [i for i in range(1, 1000, 20)]
for key in keys:
    m.put(str(key), key * 42)
print(m.size, m.capacity)
result = True
for key in keys:
    # all inserted keys must be present
    result = result and m.contains_key(str(key))
    # all NOT inserted keys must be absent
    result = result and not m.contains_key(str(key + 1))
print(result)


""" GET """
print("\n\n********   GET()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(30, hash_function_1)
print(m.get('key'))
m.put('key1', 10)
print(m.get('key1'))

print("--- EXAMPLE 2 ---")
m = HashMap(150, hash_function_2)
for i in range(200, 300, 7):
    m.put(str(i), i * 10)
print(m.size, m.capacity)
for i in range(200, 300, 21):
    print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


""" REMOVE """
print("\n\n********   REMOVE()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(50, hash_function_1)
print(m.get('key1'))
m.put('key1', 10)
print(m.get('key1'))
m.remove('key1')
print(m.get('key1'))
m.remove('key4')


""" RESIZE """
print("\n\n********   RESIZE_TABLE()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(20, hash_function_1)
m.put('key1', 10)
print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
m.resize_table(30)
print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

print("--- EXAMPLE 2 ---")
m = HashMap(75, hash_function_2)
keys = [i for i in range(1, 1000, 13)]
for key in keys:
    m.put(str(key), key * 42)
print(m.size, m.capacity)
for capacity in range(111, 1000, 117):
    m.resize_table(capacity)
    result = True
    for key in keys:
        result = result and m.contains_key(str(key))
        result = result and not m.contains_key(str(key + 1))
    print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))
