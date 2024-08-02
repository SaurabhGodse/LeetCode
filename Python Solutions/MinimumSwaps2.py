"""
2134. Minimum Swaps to Group All 1's Together II
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
"""

class MinimumSwaps2:
	def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        window_ones = max_window_ones = 0
        total_ones = nums.count(1)
        l = 0
        for r in range(2 * N):
            if nums[r % N]:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l % N]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_ones - max_window_ones