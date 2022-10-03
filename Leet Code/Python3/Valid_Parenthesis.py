class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            try:
                if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    stack.append(s[i])
                elif stack[len(stack) - 1] == '(' and s[i] != ')':
                    return False
                elif stack[len(stack) - 1] == '{' and s[i] != '}':
                    return False
                elif stack[len(stack) - 1] == '[' and s[i] != ']':
                    return False
                else:
                    stack.pop()
            except IndexError:
                return False

        if len(stack) != 0:
            return False
        return True
            

if __name__ == "__main__":
    string = input()
    sol = Solution()
    ans = sol.isValid(string)
    print(ans)