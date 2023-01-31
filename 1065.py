#한수
import sys
input = sys.stdin.readline

N = int(input())

if N <= 99:
    print(N)
elif 100 <= N < 1000:
    count = 99
    for num in range(100, N+1): #N
        a = []
        for i in str(num):
            a.append(i)
            b = list(map(int, a))
        first = b[1] - b[0]
        second = b[2] - b[1]
        if first == second:
            count += 1
        num += 1
    print(count)
else:
    print(144)