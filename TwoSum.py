class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return []
        test_map = {}
        for i in range(len(nums)):
            req = target-nums[i]
            if req in test_map:
                return [test_map[req], i]
            test_map[nums[i]] = i
            # if test_map.get(target-nums[i]) is None:
            #     test_map[target-nums[i]] = i
            #     if test_map.get(nums[i]) is not None and nums[i] != target-nums[i]:
            #         return [test_map.get(nums[i]), i]
            # elif nums[i] == target-nums[i]:
            #     return [test_map.get(target-nums[i]), i]


s = Solution()
print(s.twoSum([11], 11))
