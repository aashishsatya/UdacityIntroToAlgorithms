#
# Implement remove_min
#

def remove_min(heapList):
    # get last element and replace first element with it
    heapList[0] = heapList.pop()
    down_heapify(heapList, 0)
    return heapList

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(heapList,i): 
    return (left_child(i) >= len(heapList)) and (right_child(i) >= len(heapList))
def one_child(heapList,i): 
    return (left_child(i) < len(heapList)) and (right_child(i) >= len(heapList))

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(heapList, i):
    # If i is a leaf, heap property holds
    if is_leaf(heapList, i): 
        return
    # If i has one child...
    if one_child(heapList, i):
        # check heap property
        if heapList[i] > heapList[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (heapList[i], heapList[left_child(i)]) = (heapList[left_child(i)], heapList[i])
        return
    # If i has two children...
    # check heap property
    if min(heapList[left_child(i)], heapList[right_child(i)]) >= heapList[i]: 
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if heapList[left_child(i)] < heapList[right_child(i)]:
        # Swap into left child
        (heapList[i], heapList[left_child(i)]) = (heapList[left_child(i)], heapList[i])
        down_heapify(heapList, left_child(i))
        return
    else:
        (heapList[i], heapList[right_child(i)]) = (heapList[right_child(i)], heapList[i])
        down_heapify(heapList, right_child(i))
        return heapList

#########
# Testing Code
#

# build_heap
def build_heap(heapList):
    for i in range(len(heapList)-1, -1, -1):
        down_heapify(heapList, i)
    return heapList

print build_heap([4,3,5,2,6,7,9])