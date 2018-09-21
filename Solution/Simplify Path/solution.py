class Solution:
    '''
        . 表示停留当前文件路径，
        .. 表示回到之前文件路径
        从后往前计算..个数来判断是否返回路径
        难度：Medium

    '''
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')[::-1]
        sk = 0
        res = []
        for i in path:
            if i and i != '.':
                if i == '..':
                    sk += 1
                else:
                    if sk == 0:
                        res.append(i)
                    else:
                        sk -= 1
            
        return '/'+'/'.join(res[::-1])