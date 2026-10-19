class Solution:
    # ---------- helper to find left-most occurrence ----------
    def binarySearchLeft(self, nums, target):
        n          = len(nums)
        low, high  = 0, n - 1
        index      = -1              # default: not found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid          # potential left boundary
                high  = mid - 1      # continue searching left
            elif nums[mid] > target:
                high  = mid - 1      # target is in the left half
            else:                    # nums[mid] < target
                low   = mid + 1      # target is in the right half
        return index

    # ---------- helper to find right-most occurrence ----------
    def binarySearchRight(self, nums, target):
        n          = len(nums)
        low, high  = 0, n - 1
        index      = -1              # default: not found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid          # potential right boundary
                low   = mid + 1      # continue searching right
            elif nums[mid] > target:
                high  = mid - 1
            else:                    # nums[mid] < target
                low   = mid + 1
        return index

    # ---------- main driver ----------
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ext_left = self.binarySearchLeft(nums, target)
        # if the target never appears, no need for the second search
        if ext_left == -1:
            return [-1, -1]

        ext_right = self.binarySearchRight(nums, target)
        return [ext_left, ext_right]