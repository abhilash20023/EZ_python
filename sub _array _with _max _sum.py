# 21) sub array with max sum
# You are given a list of integers, and your task is to find the subarray with the maximum sum.
# Write a function or method to solve this problem efficiently and return the maximum sum.
# Input:
# n: the no of elements in the array
# nums (List of integers): A list of integers (1 <= len(nums) <= 10^5)
# Sample input:
# 8
# -1 2 3 10 -4 7 2 -5
# Sample output:
# 20
# Explanation:
# The max subarry sum is 20. The subarray is [2,3,10,-4,7,2]

nums=list(map(int,input().split()))
temp=0
res=0
for i in nums:
    temp+=i
    if temp<i:
        temp=i
    if res<temp:
        res=temp
print(res)