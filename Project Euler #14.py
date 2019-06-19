import time
start = time.time()
chains = []

def Longest_Collatz_sequence(chain):
    for x in range(3,1000000,2):
        chains.append(chain)
        chain = 0
        while x > 1:
            if x % 2 == 0:
                x /= 2
                chain += 1
            else:
                x = 3*x +1
                chain += 1


Longest_Collatz_sequence(0)
end = time.time()
print(end - start)
print(max(chains))
