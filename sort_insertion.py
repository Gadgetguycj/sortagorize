from datetime import datetime
def insertion(data):
    insertion_data=data[:]
    start_time=datetime.now()
    print(f"Start Time: {start_time}")
    iterations=0

    for index in range(1, len(insertion_data)):
        current = insertion_data[index]
        position = index

        while position > 0 and insertion_data[position-1] > current:
            insertion_data[position] = insertion_data[position-1]
            position -= 1
        iterations+=1
        insertion_data[position] = current

    end_time=datetime.now()
    print(f"End Time: {end_time}")
    total_time = end_time - start_time
    print("Time elapsed (hh:mm:ss.ms) {}".format(total_time))
    print(f"Iterations: {iterations}\n")


    return total_time