def get_next_array(t_list):
    nxt = [0]*len(t)
    nxt[0], nxt[1] = -1, 0
    for j in range(2, len(t)):
        k = nxt[j-1]
        while k != -1:
            if t[j-1] == t[k]:
                nxt[j] = k+1
                break
            else:
                k = nxt[k]
            nxt[j] = 0
    return nxt


def KMPMatch(s, t):
    s_list = list(s)
    t_list = list(t)
    nxt = get_next_array(t_list)
    i, j = 0, 0
    while i < len(s_list) and j < len(t_list):
        if j == -1 or s_list[i] == t_list[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]
    if j == len(t_list):
        return i-j
    else:
        return -1


if __name__ == "__main__":
    s = 'ACBACAACAACACAACAB'
    t = 'ACAACAB'
    result = KMPMatch(s, t)
    print('Location:', result)
    print('S String:',''.join(s[result:]))
