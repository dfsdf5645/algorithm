#수 정렬하기
import sys
input = sys.stdin.readline

T = int(input().rstrip())

a = []
for i in range(T):
    # a += map(int, input().rstrip()) #map이 문제인듯 런타임에러뜸
    a.append(int(input().rstrip()))

a.sort()
for num in a:
    print(num)