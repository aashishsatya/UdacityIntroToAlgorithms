# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 23:09:45 2014

@author: aashish_b130160cs
"""

import random

def partition(listToPartition, pivot):
    """
    Partitions a list based on a given pivot
    Inputs: A list and a pivot
    Output: A tuple of three lists containing elements smaller, equal to
    and bigger than the pivot respectively
    """
    smaller = []
    equal = []
    bigger = []
    for value in listToPartition:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            bigger.append(value)
        else:
            equal.append(value)
    return smaller, equal, bigger
    
def topK(listOfVals, k):
    """
    Returns the top k elements in a set
    Input: A list and k, the number 'top' items to be returned
    Output: A list containing the top k elements
    """
    pivot = random.choice(listOfVals)
    smaller, equal, bigger = partition(listOfVals, pivot)
    if len(smaller) > k:
        return topK(smaller, k)
    if len(smaller) == k:
        return smaller
    if len(smaller) + len(equal) >= k:
        return smaller + equal[:k-len(smaller)]
    return smaller + equal + topK(bigger, k - len(smaller) - len(equal))