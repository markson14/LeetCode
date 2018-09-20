class Solution:

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        last = [-1] * 10
        num_list = [_ for _ in str(num)]
        for i in range(len(num_list)):
            last[int(num_list[i])] = i
        print(last)
        for j in range(len(num_list)):
            for k in range(9,int(num_list[j]),-1):
                print(j,last[k])
                if j <= last[k]:
                    tmp = num_list[j]
                    num_list[j] = num_list[last[k]]
                    num_list[last[k]] = tmp
                    return int(''.join(num_list))
        return num
                    
            