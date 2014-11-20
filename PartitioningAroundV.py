#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    rankOfV = rank(L, v)
    smallerThanV = []
    biggerThanV = []
    equalToV = []
    for value in L:
        if value < v:
            smallerThanV.append(value)
        elif value > v:
            biggerThanV.append(value)
        else:
            equalToV.append(value)
            
    return smallerThanV + equalToV + biggerThanV

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos



