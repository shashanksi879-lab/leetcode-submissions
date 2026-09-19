class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()  # stores unique sorted triplets

        for i in range(n):
            hashset = set()   # fresh set for each fixed i
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])  # value we need
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                # add current nums[j] for future pairs
                hashset.add(nums[j])

        ans = list(result)
        return ans