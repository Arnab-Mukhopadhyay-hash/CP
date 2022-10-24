class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        arr = []
        current = head
        while current is not None:
            arr.append(current.val)
            current = current.next
        arr2 = arr[::-1]
        print(arr, arr2)
        if arr == arr2:
            return True
        return False

        # i = 0
        # n = len(arr)
        # while i < n:
        #     if arr[i] != arr[n-i-1]:
        #         return False
        #     else:
        #         i += 1
        # return True


if __name__ == '__main__':
    head = ListNode(1)
    n1 = ListNode(2)
    head.next = n1
    n2 = ListNode(2)
    n1.next = n2
    n3 = ListNode(1)
    n2.next = n3

    sol = Solution()
    ans = sol.isPalindrome(head)
    print(ans)