# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low<=high:
            mid = (low + high) // 2
            if isBadVersion(mid) == True and isBadVersion(mid-1)== False:
                return mid
            else:
                if isBadVersion(mid) == True:
                    high = mid-1
                elif isBadVersion(mid) == False:
                    low = mid +1
            
            
                