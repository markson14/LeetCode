class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dic = collections.Counter(barcodes)
        l = [x for x,y in dic.most_common()]
        
        r = [0]*len(barcodes)
        index = 0
        for i in l:
            count = 0
            while True:
                if count == dic[i]:
                    break
                r[index],index,count = i,index+2,count+1
                if index >= len(r):
                    index = 1
        return r