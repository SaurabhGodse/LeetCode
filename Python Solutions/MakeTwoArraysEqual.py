"""
1460. Make Two Arrays Equal by Reversing Subarrays

You are given two integer arrays of equal length target and arr. 
In one step, you can select any non-empty subarray of arr and reverse it.
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""

class MakeTwoArraysEqual:
	def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrDict = {}
        for num in arr:
            if num not in arrDict:
                arrDict[num] = 1
            arrDict[num] += 1
        targetDict = {}
        for num in target:
            if num not in targetDict:
                targetDict[num] = 1
            targetDict[num] += 1
        return arrDict == targetDict