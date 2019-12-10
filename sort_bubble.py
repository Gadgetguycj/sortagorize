from datetime import datetime
def bubble(data):
    bubble_data=data[:]
    start_time=datetime.now()
    print(f"Start Time: {start_time}")
    swapped=True
    iterations=0


    #Main loop
    while(swapped):
        swapped=False
        #Iterate over set of data
        for x in range(0, len(bubble_data)-1):
            first_number = bubble_data[x]
            second_number = bubble_data[x+1]
            #Finding min value
            if first_number > second_number:
                bubble_data[x] = second_number
                bubble_data[x+1] = first_number
                swapped = True
            iterations += 1

    end_time=datetime.now()
    print(f"End Time: {end_time}")
    total_time = end_time - start_time
    print('Time elapsed (hh:mm:ss.ms) {}'.format(total_time))
    print(f"Iterations: {iterations}\n")
    return total_time
