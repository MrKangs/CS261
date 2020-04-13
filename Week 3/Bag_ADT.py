# Much of this code is taken from https://opendatastructures.org/

class BaseCollection(object):
    """Base class for everything"""
    def __init__(self):
        super(BaseCollection, self).__init__()
    
    # Developers Note: The size and len function are actually not needed here.
    # they were copied in from the ODS code, but really all I wanted was the
    # printing functions.
    def size(self):
        """This implementation works for almost every class in ODS"""
        return self.n
    
    def __len__(self):
        return self.size()
    
    def __str__(self):
        return "[" + ",".join([str(x) for x in self]) + "]"
    
    def __repr__(self):
        return self.__class__.__name__ \
            + "(["+ ",".join([repr(x) for x in self]) +"])"

class Bag(BaseCollection):
  def __init__(self):
    super(Bag, self).__init__()
    # Creating a new empty list that will be the data structure for our bag ADT
    self.__l = [];

  def __iter__(self):
      for i in range(len(self)):
          yield(self.__get(i))

  def __get(self, i):
    return self.__l[i]

  def add(self, item):
    self.__l.append(item);

  def remove(self, item):
    self.__l.remove(item)

  def clear(self):
    self.__l.clear()

  def count(self, item):
    return self.__l.count(item)

  def size(self):
    return len(self.__l)

  def display(self):
    return self.__str__()

print("\nInitilizing bag")
my_bag = Bag()
print(f"The bag contains {my_bag.display()}.")

print("\nAdding an apple and an orage")
my_bag.add("Apple")
my_bag.add("Orange")
print(f"The bag contains {my_bag.display()}.")

print("\nAdding an apple, removing an orange")
my_bag.add("Apple")
my_bag.remove("Orange")
print(f"The bag contains {my_bag.display()}.")

print("\nAdding a T-rex")
my_bag.add("T-rex")
print(f"The bag contains {my_bag.display()}.")

print("\nCounting apples")
print(f"The has {my_bag.count('Apple')} apples.")