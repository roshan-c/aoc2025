def is_invalid(number):
    s = str(number)
    
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half


def solve():
    with open('input.txt', 'r') as f:
        line = f.read().strip()
    
    ranges = line.split(',')
    
    total = 0
    
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        
        for number in range(start, end + 1):
            if is_invalid(number):
                total += number
    
    return total


result = solve()
print(result)