from datetime import datetime
def merge_internal(merge_data): 
    
    if len(merge_data) >1: 
        mid = len(merge_data)//2 #Finding the mid of the array 
        L = merge_data[:mid] # Dividing the array elements  
        R = merge_data[mid:] # into 2 halves 
  
        merge_internal(L) # Sorting the first half 
        merge_internal(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                merge_data[k] = L[i] 
                i+=1
            else: 
                merge_data[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            merge_data[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            merge_data[k] = R[j] 
            j+=1
            k+=1
    return merge_data



def mergesort(data): 
    merge_data=data[:]
    start_time=datetime.now()
    print(f"Start Time: {start_time}")
    merge_internal(merge_data)
    end_time=datetime.now()
    print(f"End Time: {end_time}")
    total_time = end_time - start_time
    print("Time elapsed (hh:mm:ss.ms) {}".format(total_time))
    print("\n")
    
    return total_time

