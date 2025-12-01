position = 50

zeroCount = 0

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            position = (position + distance) % 100
        else:
            position = (position - distance % 100 + 100) % 100
        
        if position == 0:
            zeroCount = zeroCount + 1

print(zeroCount)
