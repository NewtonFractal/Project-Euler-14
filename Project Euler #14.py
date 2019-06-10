record =[]
for x in range(2,1000000):
    chain = 0
    while x != 1:
        if x % 2 == 0:
            x /= 2
            chain += 1
        else:
            x = 3 * x + 1
            chain += 1
        if x == 1:
            record.append(chain)

print(max(record))