# Kadane's Algorithm is used
"""
We keep a variable maxSum to store the maximum sum so far and another variable currMax to store the current sum value

We add the list items to currMax and compair it with the sum so far(maxSum) if sum so far is less than current sum then we make sum so far = current sum

after this we check if current sum is < 0 or not if yes then we make current sum = 0, since we need the greatest sum."""
class Solution:
    def maxSubArray(self, nums)->int:
        maxSum = -1000000000000 # maxSum should be the minimum possible integer
        currMax = 0
        for i in nums:
            currMax += i
            if maxSum < currMax:
                maxSum = currMax
            if currMax < 0:
                currMax = 0
        return maxSum

if __name__ == "__main__":
    li = [int(x) for x in input().split()]
    sol = Solution()
    ans = sol.maxSubArray(li)
    print(ans)
        
            