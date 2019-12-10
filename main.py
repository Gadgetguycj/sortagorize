from datetime import datetime
from sort_selection import selection
from sort_mergesort import mergesort
from sort_bubble import bubble
from sort_insertion import *
import data
results = []

print("Starting Test\n\n\n")

for x in range(0,24):
    blank=datetime.now()
    results.append(blank-blank)


for x in range(1, 4):
    print(f"\nTEST {x}: \n")
    print("\nBubble: ")
    results[0]+=bubble(data.random_small)
    results[1]+=bubble(data.random_medium)
    #results[2]+=bubble(data.random_large)
    results[3]+=bubble(data.random_slight_small)
    results[4]+=bubble(data.random_slight_medium)
    #results[5]+=bubble(data.random_slight_large)

    print("\nSelection: ")
    results[6]+=selection(data.random_small)
    results[7]+=selection(data.random_medium)
    results[8]+=selection(data.random_large)
    results[9]+=selection(data.random_slight_small)
    results[10]+=selection(data.random_slight_medium)
    results[11]+=selection(data.random_slight_large)

    print("\nInsertion: ")
    results[12]+=insertion(data.random_small)
    results[13]+=insertion(data.random_medium)
    results[14]+=insertion(data.random_large)
    results[15]+=insertion(data.random_slight_small)
    results[16]+=insertion(data.random_slight_medium)
    results[17]+=insertion(data.random_slight_large)
    
    print("\nMergesort: ")
    results[18]+=mergesort(data.random_small)
    results[19]+=mergesort(data.random_medium)
    results[20]+=mergesort(data.random_large)
    results[21]+=mergesort(data.random_slight_small)
    results[22]+=mergesort(data.random_slight_medium)
    results[23]+=mergesort(data.random_slight_large)


print("\n\n\nFinished:\n\n")

for x in range(0, 23):
    if x <= 5:
        print("Bubble Sort:")
    elif x <= 11:
        print("Selection Sort:")
    elif x <= 17:
        print("Insertion Sort:")
    elif x <= 23:
        print("Merge Sort:")
    
    print(f"{results[x]/3}\n")
    

