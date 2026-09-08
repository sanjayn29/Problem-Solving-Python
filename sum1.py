# Find the B-th Positive Integer Not Divisible by A 
# Problem Description 
# Given two positive integers A and B, find the B-th smallest positive integer that is not divisible by 
# A. 
# Input Format 
# * A single line containing two space-separated integers, A and B. 
# Output Format 
# * Print a single integer representing the B-th positive integer that is not divisible by A. 
# Constraints 
# ● 2 <= A <= 10^9 
# ● 1 <=B <= 10^9 
# Example 1 
# Input: 
# 3 7 
# Output: 
# 10 
# Example 2 
# Input: 
# 2 5 
# Output: 
# 9 

a,b = map(int,input().split())
ans = b+ (b-1) // (a-1)
print("Ans : ",ans)