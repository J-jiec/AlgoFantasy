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

