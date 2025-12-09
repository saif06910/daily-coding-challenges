"""
Problem: Palindrome Number (LeetCode #9)
Link: https://leetcode.com/problems/palindrome-number/
Date: 09-12-2025 (at the time of this commit)
Difficulty: Easy

Approaches:
    1. String Conversion (Simple & Clean)
       - Convert integer to string
       - Compare string with its reverse using slicing
       - Handle negative numbers (always return false)
       - Time: O(n), Space: O(n) where n is number of digits
    
    2. Half Reversal (Most Optimal)
       - Only reverse half of the number to save operations
       - Compare first half with reversed second half
       - Handle odd-length numbers by dividing reversed half by 10
       - Time: O(n/2) ≈ O(n), Space: O(1)

Time Complexity: O(n) for all approaches where n is number of digits
    - String approach: Must process all n digits to build string and reverse it
    - Half reversal: Only processes n/2 digits, but O(n/2) = O(n) in Big-O notation
      (we drop constants in asymptotic analysis, so dividing by 2 doesn't matter)

Space Complexity: O(n) for string approach, O(1) for mathematical approach

Key Insight: 
    While string conversion is clean and readable, solving it mathematically demonstrates
    stronger algorithmic thinking. The half-reversal optimization is particularly elegant
    because it recognizes we only need to check half the digits - if first half equals
    reversed second half, the number is a palindrome. This cuts operations nearly in half!
    
    Note: Although O(n/2) is technically faster than O(n) in practice (literally 2x faster),
    in Big-O notation we ignore constant factors. Both are classified as O(n) because they
    scale linearly with input size. Think of it this way: if you double the digits, both
    approaches roughly double their runtime.

Mathematical Digit Manipulation :

    1. EXTRACT last digit: number % 10
       Example: 12345 % 10 = 5
       Use case: Getting rightmost digit for processing
    
    2. REMOVE last digit: number // 10
       Example: 12345 // 10 = 1234
       Use case: Moving to next digit, iterating through digits right-to-left
    
    3. BUILD number from digits: number * 10 + digit
       Example: 123 * 10 + 4 = 1234
       Use case: Constructing reversed numbers, accumulating digit-by-digit results
       Think of it as "shifting left and appending" - like concatenating strings but for numbers
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        Approach 1: String Conversion - O(n) time, O(n) space
        Simple and pythonic solution using string slicing
        """
        # Negative numbers are never palindromes
        if x < 0:
            return False
        
        # Convert to string and compare with reverse
        return str(x) == str(x)[::-1]
     
    def isPalindromeHalfReversal(self, x):
        """
        Approach 2: Half Reversal (Most Optimal) - O(n/2) ≈ O(n) time, O(1) space
        Only reverse half of the number for efficiency
        
        Mathematical Digit Manipulation Toolkit (applicable to many problems):
            1. EXTRACT last digit: number % 10
            2. REMOVE last digit: number // 10
            3. BUILD number from digits: number * 10 + digit
        """
        # Negative numbers are never palindromes
        if x < 0:
            return False
        
        # Numbers ending in 0 (except 0 itself) are never palindromes
        # Example: 10 reversed is 01 which equals 1, not 10 (and also note that numbers do not begin with 0)
        if x != 0 and x % 10 == 0:
            return False
        
        reversed_half = 0
        
        # Reverse only half of the number
        # Stop when reversed_half >= x (we've processed half or more)
        # This loop runs n/2 times where n is the number of digits
        while x > reversed_half:
            digit = x % 10  # extract last digit (#1)
            reversed_half = reversed_half * 10 + digit  # build reversed number (#3)
            x //= 10  # remove last digit (#2)
        
        # For even length numbers: x should equal reversed_half
        # Example: 1221 -> x=12, reversed_half=12 -> 12 == 12 
        
        # For odd length numbers: x should equal reversed_half // 10
        # Example: 12321 -> x=12, reversed_half=123 -> 12 == 123//10 
        # (we ignore the middle digit by dividing reversed_half by 10)
        return x == reversed_half or x == reversed_half // 10
