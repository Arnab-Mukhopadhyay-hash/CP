import java.util.Scanner;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[] { i, map.get(target - nums[i]) };
            } else {
                map.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}

public class Two_Sum {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        int t = scan.nextInt();
        scan.close();
        Solution S = new Solution();
        int[] ans = S.twoSum(arr, t);
        for (int i = 0; i < ans.length; i++) {
            System.out.println(ans[i]);
        }
    }
}