# -*- coding: utf-8 -*-
# @Time    : 8/8/20 13:26
# @Author  : Sikun Xu
# @FileName: sort.py
# @Software: PyCharm

class Sort:
    def __init__(self):
        """
        TODO
        """
        pass


class QuickSort(Sort):
    def __init__(self, arr: list):
        """
        TODO
        """
        # init
        super(QuickSort, self).__init__()

        # parameters
        self.arr = arr

        # attributes
        pass

        # execute the algorithm
        self.quick_sort()

    def quick_sort(self):
        """
        Reference for quick sort:
        1. https://en.wikipedia.org/wiki/Quicksort
        """

        # 1. pick the pivot
        pivot = self.arr[-1]

        # 2. partitioning
        for idx in range(-2, -len(self.arr)-1, -1):
            
        # 3. recursion
        pass

    
    
# Insertion Sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        cur = nums[i]
        j = i - 1
        while (j >= 0) & (cur < nums[j]):
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = cur
    return nums


# Bubble Sort
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# Selection Sort
def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


# Quick Sort
def quick_sort(nums):
    _quicksort(nums, 0, len(nums) - 1)

def _quicksort(nums, left, right):
    if left >= right:
        return
    p = partition(nums, left, right)
    _quicksort(nums, left, p)
    _quicksort(nums, p + 1, right)

def partition(nums, left, right):
    pivot = left
    idx = pivot + 1
    for i in range(idx, right + 1):
        if nums[i] < nums[pivot]:
            nums[i], nums[idx] = nums[idx], nums[i]
            idx += 1
    nums[pivot], nums[idx - 1] = nums[idx - 1], nums[pivot]
    return (idx - 1)


# Merge Sort
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = int(len(nums) / 2)
    left = nums[:mid]
    right = nums[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    outcome = []
    while ((len(left) > 0) & (len(right) > 0)):
        if left[0] >= right[0]:
            outcome.append(right[0])
            right.pop(0)
        else:
            outcome.append(left[0])
            left.pop(0)
    while (len(left) > 0):
        outcome.append(left[0])
        left.pop(0)
    while (len(right) > 0):
        outcome.append(right[0])
        right.pop(0)
    return outcome

