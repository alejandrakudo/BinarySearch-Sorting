'''
Implements the binary search function.
'''
def binarySearch(collection, target):
    low = 0
    high = len(collection) -1
    while high >= low:
        mid = (high + low) //2
        if (target == collection[mid]):
            return mid    #found the item
        if (target < collection[mid]):
            high = mid - 1   #search left half
        else:
            low = mid + 1    #search right half
    return -1   #if not found
	    
'''
Use this to test the function.  What test cases should you run?
'''
def main():
    values = [1, 7, 14, 21, 25, 35, 42, 65, 100, 120, 130]
    foundAt = binarySearch(values, 35)
    print(values[foundAt])


main()
