### Example solution for assignment 4 - CISC 121 Fal 2016


##### Task 1
def binarySearch(lst, target):

    ### init low and high at each end of list
    low = 0
    high = len(lst)-1

    ## search until either target found or search list empty
    while high >= low:
        mid = (high + low)//2
        if target < lst[mid]:
           high = mid - 1
        elif target > lst[mid]:
            low = mid + 1
        else:
            return mid      ### return index where target was found
    return -low-1           ### return index where target should be inserted


#### Task 2

def createList(pythonList):
## create a linked list from a Python list and returns the list
    linkedList = None  #create a new, empty list
    for i in range(len(pythonList)-1, -1, -1):        ## iterate through values last to first
        linkedList = addToHead(linkedList, pythonList[i])
    return linkedList  #return the head of the new list

	    
def addToHead(aList, value):
#create a new node to add at begin of list and returns the new list
    newNode = {}  #empty
    newNode['data'] = value
    newNode['next'] = aList    ### attach the rest of the list to the node
    return newNode             ## reference to new list = ref to new node

def printList(aList):
## print list in listy style
    ptr = aList
    while ptr != None:
        print(ptr['data'], "-> ", end=' ')
        ptr = ptr['next']
    print("None")

def bubbleSortLinkedList(aLinkedList):
## sort elements of linked lists with bubble sort
    
    found = True
    while found:     ## while still swapped elements
        found = False
        ptr_prev = aLinkedList   ## one pointer trailing behind
        ptr = aLinkedList['next']  ## pointer to current element
        ptr2 = ptr['next']       ## one pointer ahead
        for i in range(4):   ## length of list is always 5
            if ptr['data'] > ptr2['data']:
                ### swap elements
                ptr['next'] = ptr2['next']
                ptr2['next'] = ptr
                ptr_prev['next'] = ptr2
                found = True
            ## iterate all three pointers to next element
            ptr_prev = ptr_prev['next']   
            ptr = ptr_prev['next']
            ptr2 = ptr['next']


## Task 3

## read the song list file
def readFile(filename):
    myList = list()
    try:
        ein = open(filename, 'r')
        
        for l in ein.readlines():
            l.strip()
            l_list = l.split(',')
            t = l_list[0], int(l_list[1]), int(l_list[2])
            myList.append(t)

        ein.close()
        
    except FileNotFoundError:
        print("File", filename, "not found!")

    return myList

    


## sort the songs with respect to their running time
## sorting using a bubble sort algorithm
def sortTimeWithBubble(aList):

    count = 1
    while count != 0:     ## as long elements are still swapped
        count = 0    ## count number of swapped elements
        for i in range(len(aList)-1):
            if aList[i][1] > aList[i+1][1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
                count += 1
    return aList


## sort the songs with respect to their release year
## sorting using selection sort algorithm
def sortYearWithSelection(aList):
    for i in range(0, len(aList)-1):
        minIndex = i
        for j in range(i+1, len(aList)):
            if (aList[j][2] < aList[minIndex][2]):
                minIndex = j
        aList[i], aList[minIndex] = aList[minIndex], aList[i]
    return aList

### Bonus task

## sort the names with bubble sort in sub-list
def bubbleSortName(aList):
    count=1
    while count != 0:
        count = 0
        for i in range(len(aList)-1):
            if aList[i][0] > aList[i+1][0]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
                count += 1
    return aList

def sortYearWithSelection2(aList):
    ### sort list with respect to released year
    for i in range(0, len(aList)-1):
        minIndex = i
        for j in range(i+1, len(aList)):
            if (aList[j][2] < aList[minIndex][2]):
                minIndex = j
        aList[i], aList[minIndex] = aList[minIndex], aList[i]

    ### separate list into sub-list, all songs in sublist have same release year
    currentYear = aList[0][2]
    minIndex = 0
    maxIndex = 0
    
    for i in range(1, len(aList)):
        if aList[i][2] != currentYear or i == len(aList)-1:
            if i == len(aList)-1:
                maxIndex = i
            else:
                maxIndex = i-1

            ## sort sublist with bubble sort with respect to names
            if minIndex != maxIndex:
                sub_list = aList[minIndex:maxIndex+1]
                n_list = bubbleSortName(sub_list)     ### returns sorted sublist
                ### replace elements in original list with element from sorted list
                for j in range(minIndex, maxIndex+1):
                    aList[j] = n_list[j - minIndex]
            minIndex = i
            maxIndex = i
            currentYear = aList[i][2]   ### next year in list
            
    return aList



        




