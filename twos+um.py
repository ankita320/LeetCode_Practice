class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] n = new int[2];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i; j < nums.length; j++) {
                if (nums[i] + nums[j] == target && i != j) {
                    n[0] = i;
                    n[1] = j;
                    break;
                }
            }
        }
        
        
        return n;


    }
}
