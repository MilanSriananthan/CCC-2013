start = int(input())

def factors(num):
    factor = []
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            a = i
            b = num//i
            return [a,b]
    return [num, 1]

count = 0
while start != 1:
    result = factors(start)
    start -= result[1]
    count += result[0]-1

print(count)