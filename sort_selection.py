from datetime import datetime
def selection(data):
    start_time=datetime.now()
    print(f"Start Time: {start_time}")
    iterations=0
    for y in range(0, len(data)):
        minimum = data[y]
        minimum_location = y

        #Find min
        for x in range(y, len(data)):
            if data[x] < minimum:
                minimum = data[x]
                minimum_location = x
        iterations+=1

        data[minimum_location] = data[y]
        data[y]=minimum

    end_time=datetime.now()
    print(f"End Time: {end_time}")
    total_time = end_time - start_time
    print('Time elapsed (hh:mm:ss.ms) {}'.format(total_time))
    print(f"\nIterations: {iterations}")


    return total_time
