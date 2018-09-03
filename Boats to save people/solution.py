
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        m,n = 0,len(people)
        for i in range(n-1,-1,-1):
            if people[m] + people[i] <=limit:
                m+=1
            if m>=i:
                return n-i
                