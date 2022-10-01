class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        sx2 = sx[::-1]
        if sx == sx2:
            return True
        return False

if __name__ == "__main__":
    x = int(input())
    a = Solution()
    ans = a.isPalindrome(x)
    print(ans)