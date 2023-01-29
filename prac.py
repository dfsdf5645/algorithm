import sys
input = sys.stdin.readline

T = int(input()) #3

for i in range(T): #0, 1, 2
    l = list(map(int, input().split())) #4 5 6 쪼개 4,5,6 
    # A, B, C, D = map(int, input().rstrip().split())
print(l)
#------------------------------------------
# T = int(input())
# for test_case in range(1, T+1):
#     num = list(map(int,input().split()))
#     avg = sum(num)/len(num)
#     avg = round(avg)
#     print("#{} {}".format(test_case, avg))
# #------------------------------------------
# num = int(input())
# #print(T)
# for i in range(num):
#     l = list(map(int,input().split()))
#     l.sort()