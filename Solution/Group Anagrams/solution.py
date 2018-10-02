import collections
def func(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
        print(tuple(sorted(s)), s)
    return list(ans.items())
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print('Input: {}'.format(strs))
    print()
    print('Output: {}'.format(func(strs)))
