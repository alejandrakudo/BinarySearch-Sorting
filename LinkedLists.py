# CISC 121; lecture 22 - weel 8
# Starting to Code Linked Lists 

def createNode(value):
    node = {}
    node['data'] = value
    node['next'] = None
    return node 

# add value, create new node to add to the head 
def addtoHead(aList, value):
    newnode = createNode(value)
    newnode['next'] = aList # put the new node as the first node in the list
    return newnode          # always want to keep a pointer at the beginning of the new node

    # def main()
    # node1 = createNode(10)
    #print(node1)
    #node2 = createNode(20)
    #print(node2)
    #node1['next'] = node2
    #print(node1)            # not the result, of a linked list, not the proper way 

def printList(aList):
    ptr = aList
    while ptr != None:
        print(ptr['data'], "->", end = '')
        ptr = ptr['next']  # this is to move the pointer, in order to stop loop
    print("None")

def generateList(aList, pythonList):
    # pythonList might look like [10,20,30,40,83]
    for i in pythonList:
        aList = addtoHead(aList, i)
    return aList 

def concatenateLists(aList, bList):
    # find the end of aList
    ptr = aList
    if ptr == None:
        return bList
    while ptr['next'] != None:
        ptr = ptr['next']

    #pointer now points to the last node in list aList
    ptr['next'] = bList
    return aList


def sumNodes(aList):
    summation = 0
    ptr = aList
    while ptr != None:
        summation = summation + ptr['data']
        ptr = ptr['next']
    return summation 

# you're going to need two lists to keep track of everything, for assignment
def main():
    myList = None
    myList = addtoHead(myList, 20)
    myList = addtoHead(myList, 30)
    myList = addtoHead(myList, 40)
    printList(myList)
    myfirstList = None 
    mysecondList = None
    mysecondList = generateList(mysecondList, [100,200,400,450,600])
    printList(mysecondList)
    concatenateLists(myList, mysecondList)
    printList(myList)
    printList(mysecondList)
    concatenateLists(myfirstList, mysecondList)
    print("The sum is:",sumNodes(mysecondList))
    

    
main()
