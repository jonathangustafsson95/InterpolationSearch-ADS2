from Algorithms import BinarySearch
from Input import input_gen


key = 3
n = [1,2,13,15,64,75,76,81,84,86,91,93,95,100,150,200,210,221,222,230,240,250,266]


data, cr_op = BinarySearch.binary_search(n, key)

if not data:
    print("Key not found in array, %d critical ops." % cr_op)

else:
    print("Key found at index %s" % data)
    print("%s: critical operations" % cr_op)