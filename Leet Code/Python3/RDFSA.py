list = []

class Solution:
    def removeDuplicates(self, nums) -> int:
        newList = []
        for i in nums:
            if i not in newList:
                newList.append(i)
            else:
                continue
        j = 0
        for i in newList:
            nums[j] = i
            j = j+1
        return j


# Easiest Solution
"""
class Solution:
    def removeDuplicates(self, nums)->int:
        return len(set(nums))

Basically we are converting the given array into set and returning the length of the array"""

if __name__ == "__main__":
    for _ in range(int(input())):
        list.append(int(input()))
    sol = Solution()
    ans = sol.removeDuplicates(list)
    for i in range(ans):
        print(list[i])
