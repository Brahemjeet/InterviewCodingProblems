class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        narr = []
        n = len(nums)
        for i in range(n*2):
            narr.append(nums[i%n])
        return narr