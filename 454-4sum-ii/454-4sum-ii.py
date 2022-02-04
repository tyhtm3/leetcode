class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                if nums1[i]+nums2[j] not in dict:
                    dict[nums1[i]+nums2[j]] = 1
                else:
                    dict[nums1[i]+nums2[j]] += 1
        count = 0
        for i in range(n):
            for j in range(n):
                target = -(nums3[i]+nums4[j])
                if target in dict:
                    count += dict[target]
        return count
        