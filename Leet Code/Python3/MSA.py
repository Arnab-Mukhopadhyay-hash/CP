class Solution:
    # merge algorithm is used, the same merge algorithm is used in merge sort, Complexity = O(m+n)
    def merge(self, nums1, m, nums2, n):
        nums = []   # new array
        i = 0   # pointer to first element of nums1(array1)
        j = 0   # pointer to first element of nums2(array2)
        while i < m and j < n:  # loop runs until we reach end of any one array
            if nums1[i] <= nums2[j]: # we element of array1 is less than or equal to the element at array 2 then we copy the element of array1 and increase the pointer by one
                nums.append(nums1[i])
                i += 1
            else:   # if element of array2 is less than that of array1 then we copy the element from array2 and increase the pointer of array2
                nums.append(nums2[j])
                j += 1
        # lastly we copy the remaining elements since elements from only one array will be left
        while i < m:
            nums.append(nums1[i])
            i += 1
        
        while j < n:
            nums.append(nums2[j])
            j += 1
        # we copy the whole nums into nums1
        nums1[:] = nums
    

if __name__ == "__main__":
    m = int(input())
    nums1 = []
    for _ in range(m):
        nums1.append(int(input()))
    n = int(input())
    nums2 = []
    for _ in range(n):
        nums2.append(int(input()))
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
