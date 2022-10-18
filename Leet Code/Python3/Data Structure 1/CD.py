class Solution:
    def containsDuplicate(self, nums)->bool:
        HashTable = {}
        for i in nums:
            if i in HashTable:
                return True
            HashTable[i] = 1
        return False


if __name__ == "__main__":
    li = [int(x) for x in input().split()]
    sol = Solution()
    ans = sol.containsDuplicate(li)
    print(ans)
