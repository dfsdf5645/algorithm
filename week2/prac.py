T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'yes'
    # [1] si,sj, ei,ej 좌표 찾기
    si = sj = N
    ei = ej = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='#':
                if si>i:    si=i
                if sj>j:    sj=j
                if ei<i:    ei=i
                if ej<j:    ej=j
 
    if (ei-si)!=(ej-sj):    # 정사각형 아님
        ans = 'no'
    else:
        for i in range(si, ei+1):
            for j in range(sj, ej+1):
                if arr[i][j]!='#':
                    ans = 'no'
 
    print(f'#{test_case} {ans}')