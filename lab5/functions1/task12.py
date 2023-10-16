nums=[int(a) for a in input().split()]
def histogram(nums):
    for num in nums:
        print('*' * num)
        
cn=histogram(nums)