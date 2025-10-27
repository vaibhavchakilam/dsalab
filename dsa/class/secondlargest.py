class array:
    def __init__(self,arr):
        self.arr = arr
      
def second(arr):
 firstlarge = max(arr)  
 secondlarge = arr[0]
 for i in  arr:
     if i!=firstlarge and i>secondlarge:
         secondlarge = i
 return secondlarge
arr = [1,2,3,4,5,6,7,88]
a = array(arr)
print(second(arr))
        
         
     
            
        