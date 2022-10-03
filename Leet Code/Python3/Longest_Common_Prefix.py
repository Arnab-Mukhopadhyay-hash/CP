def findPrefix(string1, string2):
    prefix = ""
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            prefix = prefix + string1[i]
        else:
            break
    return prefix

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        answer = strs[0]
        for string in strs[1:]:
            answer = findPrefix(answer, string)
        return answer


if __name__ == "__main__":
    strs = []
    n = int(input())
    for i in range(n):
        st = input()
        strs.append(st)
    sol = Solution()
    ans = sol.longestCommonPrefix(strs)
    print(ans)
    