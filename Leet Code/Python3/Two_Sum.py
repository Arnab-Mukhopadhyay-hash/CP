from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in HashMap:
                return [HashMap[target - nums[i]], i]
            else:
                HashMap[nums[i]] = i

if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    t = int(input())
    ans = Solution()
    # li = 
    print(ans.twoSum(nums, t))