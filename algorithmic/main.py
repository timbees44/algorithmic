class algos(object):
 

    # insertion sort algorithm
    def insertion_sort(self, lst):
        print("original list")
        print(lst)
        for i in range(0, len(lst)):
            currentVal = lst[i]
            currentPos = i
            
            while currentPos > 0 and lst[currentPos - 1] > currentVal:
                lst[currentPos] = lst[currentPos - 1]
                currentPos = currentPos - 1
            
            lst[currentPos] = currentVal
        print("sorted list")
        print(lst)

array = [20, 42, 12, 65, 45, 63, 72, 14, 25, 74]

algos().insertion_sort(array)
