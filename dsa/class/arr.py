def largest(arr):
    n = len(arr)
    max = arr[i]
  
    for i in range(1,n-1):
       if arr[i]>max:
          max = arr[i] 
       
    return max
   
                
    
    
arr = [1,2,3,4,5]
print(largest(arr))


