class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(nums) != len(set(nums))
        distinctNums = set()
        for n in nums:
            if n in distinctNums:
                return True
            distinctNums.add(n)
        return False