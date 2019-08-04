import time
start = time.time()
numbers = {}

def Longest_Collatz_sequence(chain,record):
    for x in range(3,1000000,2):
        y = x
        if chain > record:
            record = chain
        chain = 0
        while x > 1:
            if x % 2 == 0:
                x /= 2
                chain += 1
            else:
                if x in numbers:
                    chain += numbers[x]
                    break
                x = (3*x+1)/2
                chain += 2
        numbers[y] = chain
    print(record)

Longest_Collatz_sequence(0,0)
end = time.time()
print(end - start)
