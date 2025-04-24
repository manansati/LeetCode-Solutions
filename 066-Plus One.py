class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1]+=1
        else:
            digits[-1] = 1
            digits.append(0)
        return digits
