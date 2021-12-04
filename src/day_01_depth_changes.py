
with open('data/day_01_input.csv') as file:
    num_increasing = 0
    num_decreasing = 0
    num_steps = 1
    previous_depth = int(file.readline())
    while True:
        try:
            current_depth = int(file.readline())
            num_steps += 1
        except: 
            break
        diff = previous_depth - current_depth
        if diff < 0:
            num_increasing +=1
        previous_depth = current_depth

print('read in', num_steps, 'depths and found', num_increasing, 'of them increasing over previous')

