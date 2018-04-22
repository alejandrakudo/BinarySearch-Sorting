'''
Reverse a string
eg. given "animal" the function will return "lamina"
The problem is broken down into smaller identical problems by
removing the last character and reversing the rest of the string.
eg: "cat"
first call: return "t" + reverseString("ca")
second call: return "a" + reverseString("c")
third call:  return "c"
'''
def reverseString(str):
    if len(str) == 0 or len(str) == 1:
        return str
    return str[-1] + reverseString(str[0:-1])

'''
Find the factorial of a given number.
eg.  5! = 5 * 4 * 3 * 2 * 1 = 120
Note:  5! = 5 * 4!   (n * (n-1)!)
'''

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


'''
Counts the number of 5s that appear in a list.
Checks the first number then checks the remainder of the list.
'''

def countfives(aList):
    if len(aList) == 0:
        return 0
    if aList[0] == 5:
        return 1 + countfives(aList[1:])
    else:
        return 0 + countfives(aList[1:])

'''
Finds the maximum value in a list.  The list is split (roughly) in half and
the function is called recursively on each half to find the maximum of each half.
'''
def findMax(aList):
    if len(aList) == 1:
        return aList[0]
    mid = len(aList)//2
    maxright = findMax(aList[mid:])
    maxleft = findMax(aList[0:mid])
    if maxright > maxleft:
        return maxright
    return maxleft



