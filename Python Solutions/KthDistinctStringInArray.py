"""
2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""

class KthDistinctStringInArray:
	def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)
        for s in arr:
            count[s] += 1
        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""