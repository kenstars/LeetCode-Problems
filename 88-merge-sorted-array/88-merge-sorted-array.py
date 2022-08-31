class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        total_length = m+n
        while i<m and j<len(nums2):
            print(i,j)
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                m+=1
                j+=1
            else:
                i+=1
        else:
            for i in nums2[j:]:
                nums1[m]=i
                m+=1
            while len(nums1)>total_length:
                nums1.pop(-1)
                