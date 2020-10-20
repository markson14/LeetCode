"""
KMP算法
1. 公共前缀表
2. 每次从公共前缀失败的index开始往下匹配
"""


def move_table(prefix):
    # 移动prefix table方便后续匹配
    prefix[1:] = prefix[:-1]
    prefix[0] = -1
    return prefix


def prefix_table(pattern, n):
    # 初始化prefix table
    prefix = [0]*len(pattern)
    pre_len = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[pre_len]:
            pre_len += 1
            prefix[i] = pre_len
            i += 1
        else:
            if pre_len > 0:
                pre_len = prefix[pre_len-1]
            else:
                prefix[i] = pre_len
                i += 1

    return prefix


def kmp_search(text, pattern):
    text = list(text)
    pattern = list(pattern)
    n = len(pattern)
    m = len(text)
    prefix = move_table(prefix_table(pattern, n))
    i, j = 0, 0
    while i < m:
        if j == n-1 and text[i] == pattern[j]:
            print(i-j)
            j = prefix[j]
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = prefix[j]
            if j == -1:
                i += 1
                j += 1


if __name__ == "__main__":
    s = 'ACBACAACAACABACAACAACABABCC'
    t = 'ACAACAB'
    prefix = move_table(prefix_table(t, len(t)))
    print('target array:', t)
    print('prefix table:', prefix)
    kmp_search(s, t)
    # print('Location:', result)
    # print('S String:', ''.join(s[result:]))
