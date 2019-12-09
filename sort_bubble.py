from datetime import datetime
def bubble(data):
    start_time=datetime.now()
    print(f"Start Time: {start_time}")
    swapped=True
    iterations=0
    while(swapped):
        swapped=False
        for x in range(0, len(data)-1):
            first_number = data[x]
            second_number = data[x+1]
            if first_number > second_number:
                data[x] = second_number
                data[x+1] = first_number
                swapped = True
            iterations += 1

    end_time=datetime.now()
    print(f"End Time: {end_time}")
    total_time = end_time - start_time
    print('Time elapsed (hh:mm:ss.ms) {}'.format(total_time))
    print(f"\nIterations: {iterations}")


    return total_time
