"""
1508. Range Sum of Sorted Subarray Sums

You are given the array nums consisting of n positive integers. 

You computed the sum of all non-empty continuous subarrays from the array 
and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
"""

class RangeSumOfSortedSubarraySums:
	def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        sub_array_sum = []
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                sub_array_sum.append(cur_sum)
        sub_array_sum.sort()
        return sum(sub_array_sum[left - 1 : right]) % MOD