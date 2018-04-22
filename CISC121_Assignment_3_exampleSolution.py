from linkedList_CISC121 import createList, printList, getLength

def isInList(aLinkedList, value):
## returns True if value is in list, False otherwise
    found = False
    aPtr = aLinkedList
    while(aPtr != None):        ### iterate through list
        if aPtr['data'] == value:
            found = True
        aPtr = aPtr['next']     ## move pointer to next list element
    return found
    
def popFirst(aLinkedList):
## returns first list element and list without this element
    if aLinkedList == None:    ### nothin goin list, return nothing
        return None, None
    ref = aLinkedList                    ## save reference to first element in list       
    aLinkedList = aLinkedList['next']   ### move list reference to second element in list
    return ref['data'], aLinkedList       

def getElement(aLinkedList, ind):
### returns the element with index ind, if ind out of range, returns None
    if aLinkedList == None or ind >= getLength(aLinkedList):
        return None

    ptr = aLinkedList
    for i in range(ind):      ## iterate until ind is reached
        ptr = ptr['next']
    return ptr['data']

def popLast(aLinkedList):
## returns the last element in list and the modified list (last element deleted)
    if aLinkedList == None:     ## nothing in list, nothing to return
        return None, None

    if aLinkedList['next'] == None:       ## list has only one element
        return aLinkedList['data'], None  
        
    if getLength(aLinkedList) == 2:       ## list has two elements
        v = aLinkedList['next']['data']
        aLinkedList['next'] = None
        return v, aLinkedList
    
    ptr = aLinkedList        
    for i in range(getLength(aLinkedList)-2):    ## iterate through list until second last node
        ptr = ptr['next']

    a = ptr['next']['data']          ## save last node value
    ptr['next'] = None               ## disconnect last node fromn list
    
    return (a, aLinkedList)



#####################################################
    #### Task 2
    
def sumSequence(n):
    if n == 0:    ### base case 
        return 0
    return n + sumSequence(n-1)   


        
def binaryToDecimal(w):
### returns the corresonding decimal value to the binaryString (w)
    if len(w) == 1:      ### base case binary string of 1 length 
        return int(w[0])    ### return 0 or 1   

    d = int(w[0])      ### take first element
    w = w[1:len(w)]    ### remove first element from string
    return (2**(len(w)) * d) + binaryToDecimal(w)






