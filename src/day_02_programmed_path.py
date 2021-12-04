x,d,step = 0,0,0
with open('data/day_02_input.csv') as file:
# with open('data/temp') as file:
    while True:
        try:
            direction, stepsize = file.readline().split(' ')
        except: 
            break
        step +=1
        stepsize = int(stepsize)
        if direction == 'forward':
            x += stepsize
        elif direction == 'down':
            d += stepsize
        elif direction == 'up':
            d -= stepsize

print('step ', step, ':', direction, 'by', stepsize, ':-----> (', x, ',', d,')')
print('multiplied:', x*d)