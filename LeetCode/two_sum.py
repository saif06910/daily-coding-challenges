"""
Problem: Two Sum (LeetCode #1)
Link: https://leetcode.com/problems/two-sum/
Date: 08-12-2025 (at the time of this commit)
Difficulty: Easy

Approaches:
    1. Hashmap (Optimal)
       - Store numbers we've seen in a dictionary as we iterate
       - For each number, check if its complement (target - number) exists
       - If yes, we found our pair; if no, add current number to hashmap
       - Time: O(n), Space: O(n)
    
    2. Brute Force (Nested Loops)
       - Check every possible pair of numbers
       - Use two loops: outer picks first number, inner picks second
       - Return indices when we find a pair that sums to target
       - Time: O(n²), Space: O(1)

Time Complexity: O(n) for hashmap, O(n²) for brute force
Space Complexity: O(n) for hashmap, O(1) for brute force

Key Insight: 
    The hashmap approach trades space for speed - we use O(n) extra memory to achieve
    O(n) time instead of O(n²). In algorithmic optimization, we generally prefer 
    improvements in time at the cost of memory because we can always "buy" more memory 
    (add RAM), but we can never "buy" more time (only better algorithms can improve runtime).
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Optimal hashmap solution - O(n) time, O(n) space
        """
        seen_hashmap = {}  # number : index, for example {2 : 0, 7 : 1, ... }

        for i in range(len(nums)):
            desired_number = target - nums[i]

            if desired_number in seen_hashmap:
                return [seen_hashmap[desired_number], i]  # previous index, current index

            seen_hashmap[nums[i]] = i  # store number and its index
        
        return []  # no solution found
    
    
    def twoSumBruteForce(self, nums, target):
        """
        Brute force solution - O(n²) time, O(1) space
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):  # start from i+1 to avoid using same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []  # no solution found

