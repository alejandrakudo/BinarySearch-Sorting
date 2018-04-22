# CISC 121 - Assignment 3
# Net ID: 13aak15, Student ID: 10136014
# The following code was written by Alejandra Kudo 

def createList(pythonList):
## create a linked list from a Python list 
    linkedList = None  #create a new, empty list
    for i in range(len(pythonList)-1, -1, -1):        ## iterate through values last to first
        linkedList = addToHead(linkedList, pythonList[i])
    return linkedList  #return the head of the new list

'''This function takes a single-xlinked list and a value as input arguments
and returns True is the value is in the linked list, and false if not'''
def isInList(aLinkedList, value):
    aLinkedList = ['a','b',0,[1,2]]
    myLinkedList = createList(aLinkedList)
    if value in aLinkedList:
        return True
    else:
        return False 

def getLength(aList):
## returns the length (number of elements) of the linked list aList
    count = 0         
    ptr = aList
    while ptr != None:    
        count += 1
        ptr = ptr['next']
    return count

'''This function takes a single-linked list and an index as input argument
and returns the value of the element. if index is negative or too big
for the list the function returns None'''
def getElement(aLinkedList, index):
    length = getLength(aLinkedList)
    if index > length-1:
        return None
    if index < 0:
        return None
    for i in range(len(aLinkedList)):
        if index == i:
            return ptr['data']
        else:
            ptr = ptr['next']

# add element in the beginning of the list 
def addToHead(aList, value):
    newNode = {}
    newNode['data'] = value
    newNode['next'] = aList
    return newNode 

'''This function takes as an argument a single-linked list and returns
a two element tuple. The first element in the tuple is the first element
in the list (head of list) and the second element in the tuple
is a linked list with this element deleted'''
def popFirst(aLinkedList):
    aLinkedList[0] = head_list
    if ind == 0:        ## remove first element
        return aLinkedList['next']
    if aList == None:   ## if list is empty, nothing to delete
        return aLinkedList
    
    ptr_before = aLinkedList             ## keep reference of two adjacent nodes
    ptr = aLinkedList['next']
    for i in range(1, ind):          ## iterate to element to be deleted
        ptr_before = ptr           ## keep a reference to the previous element
        ptr = ptr['next']
    ptr_before['next'] = ptr['next']     ## link previous element to next element
    return aLinkedList 

    return head_list, aLinkedList

def addToTail(aList, value):
#create a new node to add at end of list
    newNode = {}  #empty
    newNode['data'] = value
    newNode['next'] = None
    ptr = aList
    if ptr == None:
        return newNode
    while ptr["next"] != None:
        ptr = ptr["next"]
    ptr["next"] = newNode
    return aList

'''This function takes as ab argument a single-linked list and returns
a two elemen tuple. The first element in the tuple is the last element
(tail of list) and the second element in the tuple is a linked list
in which this element is deleted from the list'''
def popLast(aLinkedList):
    aLinkedList[-1] = tail_list
    
    if ind == 0:        ## remove first element
        return aLinkedList['next']
    if aList == None:   ## if list is empty, nothing to delete
        return aLinkedList
    
    ptr_before = aLinkedList             ## keep reference of two adjacent nodes
    ptr = aLinkedList['next']
    for i in range(1, ind):          ## iterate to element to be deleted
        ptr_before = ptr           ## keep a reference to the previous element
        ptr = ptr['next']
    ptr_before['next'] = ptr['next']     ## link previous element to next element
    return aLinkedList

    return tail_list, aLinkedList
# returns the first element of the tuple, which is the tail of the list
# and returns the second element of the list which is deleted 

'''Recursive function which takes a non-negative integer number
as an input argument and returns
f(n) --> formula/function provided by PROF'''
def sumSequence(n):
    if n == 0:
        return 0
    else:
        return (n + sum(n-1))

''' Recursive function that parses a binary number as a
string(input argument)and returns the corresponding decimal integer.
The length of the input binary number is variable. Input string only
contains the characters '0' and '1' '''
def binaryToDecimal(binaryString):
    number = eval(binaryString[0] * (2**(len(binaryString)-1)) + binaryToDecimal[1:]) 
    return number

# confused about this question... this was another i tried converting
# binary to decimal recursively... 
##    if binaryString == '0':
##        return int(binaryString * (2**(len(binaryString-1))) )
##    if binaryString == '1':
##        return int(binaryString * (2**len(binaryString-1)))

