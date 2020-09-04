#SETS and its default methods

mySet1={1,2,3,4,5,6}
mySet2={3,4,5,8,9,10}

#Print common elements in both sets
print("Common elemnts:", mySet1.intersection(mySet2))

#Print union elements in both sets
print("Union of elemnts:", mySet1.union(mySet2))

#Print elements that are in one set but not in both
print("Symmetric diff:",mySet1.symmetric_difference(mySet2))

#Updating a set with another set elements
mySet1.update({7,3,2,10})
print("Updated set1:",mySet1)

#Removing all elements from a set
mySet2.clear()
print("Cleared set2:",mySet2)