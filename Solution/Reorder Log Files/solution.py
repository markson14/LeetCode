class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dic_letter = []
        dic_digit = []
        for log in logs:
            log = log.split(' ')
            head = log[0]
            ifcase = ''.join(log[1:])
            log = ' '.join(log[1:])
            if ifcase.isdigit():
                dic_digit.append([head,log])
            else:
                dic_letter.append([head,log])
        res = []
        dic_letter = sorted(dic_letter, key = lambda x:x[1])
        for key,value in dic_letter:
            res.append(key+" "+value)
        for key,value in dic_digit:
            res.append(key+" "+value)
        return res