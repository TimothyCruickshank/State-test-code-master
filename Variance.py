import os 
from statistics import mean, stdev
os.system ('cls')

h = 1
while h < 6:
    print(f"Grill_{h}:")
    num = [int(line) for line in open (f'Grill_{h}.txt', 'r')]
    min_num, max_num, mean_num, dev_num = min(num), max(num), mean(num), stdev(num)

    print(f"Min: {min_num}")
    print(f"Max: {max_num}")
    print(f"Mean: {mean_num}")
    print(f"Standard Deviation of temp is {dev_num}")

    if min_num <= 342 and max_num >= 358:
        print('''Too Hot and Too Cold: Fail!
        ''')
    elif min_num <= 342:
        print('''Too Cold!: Fail
        ''')
    elif max_num >= 358:
        print('''Too Hot!: Fail
        ''')
    else:
        print('''Pass
            ''')

    h += 1