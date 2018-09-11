class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        if(n < 3){
            return false;
        }
        for(int i=0 ;i<n;i++){
            int max = INT_MIN;
            for(int j=i+1;j<n;j++){
                if(max < nums[j]){
                    max = nums[j];
                }
                if(max>nums[i] && max>nums[j] && nums[j]>nums[i]){
                     return true;                   
                }
            }
        }
        return false;
    }
};