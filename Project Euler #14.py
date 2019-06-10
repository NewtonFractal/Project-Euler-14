import time
start = time.time()
def Longest_Collatz_sequence(x,chain,record):
    for x in range(x, 1000000):
        if record == 524:
            print(x-1)
            break
        Loop = True
        while  Loop == True:
            if x % 2 == 0:
                x /= 2
                chain += 1
            else:
                x = 3 * x + 1
                chain += 1
            if x == 1:
                Loop = False
                if chain > record:
                    record = chain
                chain = 0
    print(record)

Longest_Collatz_sequence(2,0,0)
end = time.time()
print(end - start)
