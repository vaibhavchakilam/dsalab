class array:
    def __init__(self,arr):
        self.arr = arr
def first(arr):
        n = len(arr)
        firstlargest = arr[0]  
        for i in arr:
            if i> firstlargest:
                firstlargest = i
        return firstlargest 
arr = [1,2,3,4,58]             
A = array(arr)
print(first(arr))           
        
         