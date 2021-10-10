class algos(object):
 
    # indexnsertion sort algorithm
    '''
    - O(n**2) time complexity
    - Good for small arrays and nearly sorted arrays
    - how insertion works
        - each value (n) in array is assessed
        - if n < index(n-1) then all values in array move right
    '''
    def insertion_sort(self, array):
        print("original list")
        print(array)
        for index in range(0, len(array)):
            currentVal = array[index]
            currentPos = index
            
            while currentPos > 0 and array[currentPos - 1] > currentVal:
                array[currentPos] = lst[currentPos - 1]
                currentPos = currentPos - 1
            
            array[currentPos] = currentVal
        print("sorted list")
        print(array)

array = [20, 42, 12, 65, 45, 63, 72, 14, 25, 74]

    

algos().insertion_sort(array)
