def resolve():
    '''
    code here
    '''
    N = input()
    res = N[-1]

    if int(res) in [2,4,5,7,9]:
        print('hon')
    elif int(res) in [0,1,6,8]:
        print('pon')
    else:
        print('bon')

if __name__ == "__main__":
    resolve()
