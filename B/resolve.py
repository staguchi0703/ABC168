def resolve():
    '''
    code here
    '''
    K = int(input())
    S = input()
    
    if len(S) <= K:
        print(S)
    else:
        res = S[:K]
        print(res+'...')

if __name__ == "__main__":
    resolve()
    