"""
1653. Minimum Deletions to Make String Balanced

You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
"""

class MinimumDeletionToMakeStringBalanced:
	def minimumDeletions(self, s: str) -> int:
        count_a = s.count('a')
        res = len(s)
        count_b = 0
        for i in range(len(s)):
            if s[i] == "a":
                count_a -= 1
            res = min(count_a + count_b, res)
            if(s[i] == "b"):
                count_b += 1
        return res