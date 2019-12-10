from datetime import datetime
def selection(data):
    selection_data=data[:]
    start_time=datetime.now()
    print(f"Start Time: {start_time}")
    iterations=0
    for y in range(0, len(selection_data)):
        minimum = selection_data[y]
        minimum_location = y

        #Find min
        for x in range(y, len(selection_data)):
            if selection_data[x] < minimum:
                minimum = selection_data[x]
                minimum_location = x
        iterations+=1

        selection_data[minimum_location] = selection_data[y]
        selection_data[y]=minimum

    end_time=datetime.now()
    print(f"End Time: {end_time}")
    total_time = end_time - start_time
    print('Time elapsed (hh:mm:ss.ms) {}'.format(total_time))
    print(f"Iterations: {iterations}\n")


    return total_time
