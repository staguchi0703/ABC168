def resolve():
    '''
    code here
    '''
    import collections
    N, M = [int(item) for item in input().split()]
    path_list = [[int(item) for item in input().split()] for _ in range(M)]

    to_list = [[] for _ in range(N+1)]
    from_list = [[] for _ in range(N+1)]
    order_list = [[] for _ in range(N+1)]

    for path in path_list:
        to_list[path[0]] += [path[1]]
        to_list[path[1]] += [path[0]]

    # print(to_list)

    que = collections.deque([1])
    cnt = 0

    while que:
        temp = que.popleft()
        cnt += 1

        order_list[temp] = 1

        if len(to_list[temp])>=1:
            for to in to_list[temp]:
                if from_list[to] == []:
                    from_list[to] = temp
                    que.append(to)

    print('Yes')
    for item in from_list[2:]:
        print(item)



if __name__ == "__main__":
    resolve()
