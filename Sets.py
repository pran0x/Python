collection = {1,2,3,4,"world" , "world", 3 , 4 , 6 , "Hello"}
print(collection) # Duplicate values are not included .. 
print(type(collection))
print(len(collection)) # Duplicates value will be ignored.

Empty_set = set()

print(Empty_set)
print(type(Empty_set))


collection.add(9)
collection.add(9)
collection.add(9)
collection.add(9)
collection.add((10,12,14,16)) #tuples
print(collection)

collection.remove(9)
print(collection)
print(len(collection))

collection.clear() #clear sets
print(len(collection))

print(collection.pop()) #Random value print..
print(collection.pop())
print(collection.pop())
print(collection.pop())

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) #{1, 2, 3, 4} #all values
print(set1.intersection(set2))  # Common only values