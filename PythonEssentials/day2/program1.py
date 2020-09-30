#LIST and its default functions

mylist = [8,2,9,1,5]

#adding one element at the end of list
mylist.append(6)
print("After adding one element:",mylist)

#Sorting myList
mylist.sort()
print("Sorted List:", mylist)

#Reversing myList
mylist.reverse()
print("Reversed List:",mylist)

#Adding a list to myList
mylist.extend([25,1,27])
print("Extended list:",mylist)

#Returning count of an element in list
print("1 occurs following times:",mylist.count(1))
