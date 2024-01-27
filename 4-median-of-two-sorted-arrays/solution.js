// Runtime: 87ms, Beats 77.04% of users with JavaScript
// Memory: 56.45MB, Beats 5.31% of users with JavaScript

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    const nums=[...nums1,...nums2];
    nums.sort((a,b)=>a-b);
    if(nums.length%2==1) return nums[Math.floor(nums.length/2)];
    return (nums[nums.length/2-1]+nums[nums.length/2])/2;
};