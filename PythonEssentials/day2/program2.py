#Dictionary and its default methods

myDict = {1:'One',2:'Two',3:'Three'}

#Printing all the keys in dictionary
print("Keys:",list(myDict.keys()))

#Printing all the values in dictionary
print("Values:",list(myDict.values()))

#Printing all the key-value pairs in dictionary
print("Items:",list(myDict.items()))


#Removing a given Key from dictionary
print("Value of deleted key:",myDict.pop(2))

#Getting value of a given key
print("Value of given key:",myDict.get(1))