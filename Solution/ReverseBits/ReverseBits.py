class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        a = bin(n)[2:]
        x = 32 - len(a)
        y = x*'0' + str(a)
        y = y[::-1]
        return int(y,2)