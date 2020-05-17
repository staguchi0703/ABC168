def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    sards = [[int(item) for item in input().split()] for _ in range(N)]

    sards_cal1 = []
    for a, b in sards:
        sards_cal1.append(a/b)
    
    sards_cal2 = []
    for a,b in sards:
        sards_cal2.append(b/a)

    sard_cal1_cnt = collections.Counter(sards_cal1)
    sard_cal2_cnt = collections.Counter(sards_cal2)

    cnt = 0
    for k1, v1 in sard_cal1_cnt.items():
        for k2, v2 in sard_cal2_cnt.items():
            if k1 == k2 * (-1):
                cnt += v1*v2
    print(cnt//2)

if __name__ == "__main__":
    resolve()
