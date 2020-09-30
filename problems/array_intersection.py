"""
https://algodaily.com/challenges/array-intersection/
"""


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
