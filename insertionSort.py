'''
insertionSort maintains the left portion of the list in sorted order.
For each element, the algorithm locates the position for the current
element within the sorted portion of the list and inserts the value
in its correct position.
'''

def insertionSort(aList):
    for i in range(1, len(aList)):
        #use j to "walk" the list from position i towards position 0
        j = i
        while (j > 0) and (aList[j-1] > aList[j]):
            #if the element on the left is larger, swap the items
            aList[j-1], aList[j] = aList[j], aList[j-1]
            j = j - 1



#test with an empty list
mylist = []
print "before: ", mylist
insertionSort(mylist)
print "after: ", mylist

#test with list of length 1
mylist = [16]
print "before: ", mylist
insertionSort(mylist)
print "after: ", mylist

#test with a longer list (and one that has duplicate values)
mylist = [8, 3, 5, 5, 2, 1, 4]
print "before: ", mylist
insertionSort(mylist)
print "after: ", mylist

#test with a sorted list
mylist = [1, 2, 3, 4]
print "before: ", mylist
insertionSort(mylist)
print "after: ", mylist

#test with a reverse sorted list
mylist = [4, 3, 2, 1]
print "before: ", mylist
insertionSort(mylist)
print "after: ", mylist
