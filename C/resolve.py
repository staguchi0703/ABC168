def resolve():
    '''
    code here
    '''
    import math
    A, B, H, M = [int(item) for item in input().split()]

    h_ = 2*math.pi*(H*5 + M/60*5)/60
    m_ = 2*math.pi*(M/60)

    h_pos = [A*math.sin(h_), A*math.cos(h_)]
    m_pos = [B*math.sin(m_), B*math.cos(m_)]
    # print(h_pos)
    # print(m_pos)
    res = math.sqrt((h_pos[0]-m_pos[0])**2 + (h_pos[1]-m_pos[1])**2)
    print(res)
if __name__ == "__main__":
    resolve()
