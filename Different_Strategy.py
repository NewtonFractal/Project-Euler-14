import time
start = time.time()
Longest = []
numbers = []

def Longest_Collatz_sequence(chain, record):
    for x in range(3,1000000,2):
        y = x
        if chain > record:
            record = chain
            numbers.append(y-2)
            Longest.append(chain)
        chain = 0
        while x > 1:
            if x % 2 == 0:
                x /= 2
                chain += 1
            else:
                x = 3*x +1
                chain += 1
                if x in numbers:
                    z = numbers.index(x)
                    if Longest[z] + chain > record:
                        Longest.append(Longest[z] + chain)
                        numbers.append(y)
                        break

Longest_Collatz_sequence(0,0)
end = time.time()
print(end - start)
print(numbers[-1])
