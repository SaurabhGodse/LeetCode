"""
1395. Count Number of Teams
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""

class CountNumberOfTeams:
    def numTeams(self, rating: list[int]) -> int:
        res = 0
        for i in range(len(rating)):
            smallerLeft = 0
            for j in range(0, i):
                if(rating[j] < rating[i]):
                    smallerLeft += 1
            smallerRight = 0
            for j in range(i + 1, len(rating)):
                if(rating[j] < rating[i]):
                    smallerRight += 1
            res += (smallerLeft * (len(rating) - i - 1 - smallerRight)) + ((i - smallerLeft) * smallerRight)
        return res

runner = CountNumberOfTeams()
print(runner.numTeams([2,5,3,4,1]))
