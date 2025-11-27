# 347. Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. 

> **You may return the answer in any order.**

---
 
```
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
```
```
Example 2:

Input: nums = [1], k = 1

Output: [1]
```
```
Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
```
 
```
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
``` 

---

> **Follow up**
>
> Your algorithm's time complexity must be better than O(n log n), where n is the array's size.




# 238. Product of Array Except Self


> Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

> The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

> You must write an algorithm that runs in O(n) time and without using the division operation.

 
```
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```
```
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```
```
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
```

> Follow up
>
> Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
