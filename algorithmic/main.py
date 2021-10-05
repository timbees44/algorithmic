class algos(object):
 

    # insertion sort algorithm
    def insertion_sort(self, lst):
        for i in range(0, len(lst)):
            print(lst[i])
            currentVal = lst[i]
            currentPos = i
            
            while currentPos > 0 and lst[currentPos - 1] > currentVal:
                lst[currentPos] = lst[currentPos - 1]
                currentPos = currentPos - 1
            
            lst[currentPos] = currentVal


array = [20, 42, 12, 65, 45, 63, 72, 14, 25, 74]

algos().insertion_sort(array)
