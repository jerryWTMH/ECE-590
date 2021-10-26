"""
Math 560
Project 1
Fall 2021

Partner 1: Ching-Hang Hsu (Netid: ch450)
Partner 2: Zhuoer Li (Netid: zl328)
Date: 10/23
"""

"""
SelectionSort
Author: Ching-Hang Hsu
Date: 10/23
"""
def SelectionSort(listToSort):
    index = 0
    min = 0
    #pick the smallest element from the unsorted array
    for i in range(0, len(listToSort) - 1):
        min = listToSort[i]
        index = i
        for j in range(i, len(listToSort)):
            if(listToSort[j] < min):
                min = listToSort[j]
                index = j
        #put the index_ith smallest element at ith sorted array 
        temp = listToSort[i]
        listToSort[i] = listToSort[index]
        listToSort[index] = temp

    return listToSort

"""
InsertionSort
Author: Zhuoer Li
Date: 10/23
"""
def InsertionSort(listToSort):
    if len(listToSort) == 1:
        return listToSort
    for k in range(1, len(listToSort)):
        key = listToSort[k]
        i = k - 1
        while i >= 0 and key < listToSort[i]:
            listToSort[i + 1] = listToSort[i]
            i -= 1
        listToSort[i + 1] = key
    return listToSort

"""
BubbleSort
Author: Ching-Hang Hsu
Date: 10/23
"""
def BubbleSort(listToSort):
    
    if(len(listToSort) == 1):
        return listToSort
    n = len(listToSort)
    orderChecker = 1
    # scan n times, and find the biggest one in each time 
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if listToSort[j] > listToSort[j + 1]:
                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
                orderChecker = 0
        if orderChecker:
            break
    return listToSort

"""
MergeSort
Author: Zhuoer Li
Date: 10/23
"""
def MergeSort(listToSort):
    n = len(listToSort)
    if n == 1:
        return listToSort
    if n == 2:
        if(listToSort[0] > listToSort[1]):
            temp = listToSort[1]
            listToSort[1] = listToSort[0]
            listToSort[0] = temp
        return listToSort
    left_end = n // 2 ## // is floor division
    # right_start = n / 2 + 1
    L = listToSort[:left_end]
    R = listToSort[left_end :]
    MergeSort(L)
    MergeSort(R)
    i = j = k = 0 
    # i is index for L. 
    # j is index for R. 
    # k is index for final sorted array.
    #pick the larget one between L and R:
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            listToSort[k] = L[i]
            i += 1 # the picked array should add 1 to its index
        else :
            listToSort[k] = R[j]
            j += 1 # the picked array should add 1 to its index
        k += 1
    # When one of two arrays meets its own max length:
    while i < len(L):
        listToSort[k] = L[i]
        i += 1
        k += 1    
    while j < len(R):
        listToSort[k] = R[j]
        j += 1
        k += 1   
    return listToSort

"""
QuickSort
Author: Ching-Hang Hsu, Zhuoer Li
Date: 10/23

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    #move pivot to the correct position (i + 1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def QuickSort_recursive(listToSort, low, high):
    if low < high:
        partition_index = partition(listToSort, low, high)
        QuickSort_recursive(listToSort, low, partition_index - 1) # left half
        QuickSort_recursive(listToSort, partition_index + 1, high) # right half

def QuickSort(listToSort, i = 0, j = None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    if len(listToSort) == 1:
        return listToSort
    QuickSort_recursive(listToSort, 0, j - 1)
    return listToSort


"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
