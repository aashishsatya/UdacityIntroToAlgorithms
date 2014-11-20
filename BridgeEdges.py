# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       
def create_rooted_spanning_tree(G, root):
    
    # initializing nodes
    S = {}
    for node in G.keys():
        S[node] = {}
    
    visitedNodes = [root]
    newParents = [root]
    
    # run for as long as there are parents nodes
    while newParents:
        newChildren = []
        for parent in newParents:
            children = G[parent].keys()
            for child in children:
                if child in S[parent].keys():
                    # means the child was an earlier parent
                    continue
                if child in visitedNodes:
                    # child has already been visited
                    # so the node is red
                    S[parent][child] = 'red'
                    S[child][parent] = 'red'                    
                    # one for the parent, one for the child
                else:
                    # child has not been visited
                    # we have a green light
                    S[parent][child] = 'green'
                    S[child][parent] = 'green'
                    newChildren.append(child)
                    visitedNodes.append(child)
        # children have become the new parents
        # ah, how the sands of time have changed!!
        newParents = newChildren
            
    return S

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def post_order_helper(S, root, ansDict, visited = []):
    
    children = S[root].keys()
    
    # children "down" the tree
    properChildren = []
    
    # find proper children
    for child in children:
        if child in visited or S[root][child] == 'red':
            continue
        properChildren.append(child)
        if child not in visited:        
            visited += [child]
            
    if not properChildren:
        # means the node is a final leaf of the spanning tree
        # assign to it the next possible number
        if ansDict:
            nodes = ansDict.keys()
            # computing largest value in the dict
            largestValue = ansDict[nodes[0]]
            for key in nodes:
                if ansDict[key] > largestValue:
                    largestValue = ansDict[key]
            ansDict[root] = largestValue + 1
            return ansDict
        ansDict[root] = 1 
        return ansDict
    for child in properChildren:
        post_order_helper(S, child, ansDict, visited)
    largestValue = ansDict[properChildren[0]]
    for child in properChildren:
        if ansDict[child] > largestValue:
            largestValue = ansDict[child]
    ansDict[root] = largestValue + 1
    return ansDict           
    
def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    
    # it is obvious that we have to do depth first search first
    # so using recursion
    ansDict = post_order_helper(S, root, {}, [root])
    return ansDict

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3} or\
           po == {'a': 7, 'c': 5, 'b': 6, 'e': 3, 'd': 4, 'g': 1, 'f': 2}

##############

def number_of_descendants_helper(S, root, ansDict, visited = []):
    children = S[root].keys()
    
    # children "down" the tree
    properChildren = []
    
    # find proper children
    for child in children:
        if child in visited or S[root][child] == 'red':
            continue
        properChildren.append(child)
        if child not in visited:        
            visited += [child]
            
    if not properChildren:
        ansDict[root] = 1 
        return ansDict
    for child in properChildren:
        number_of_descendants_helper(S, child, ansDict, visited)
    sumValue = 0
    for child in properChildren:
            sumValue += ansDict[child]
    ansDict[root] = sumValue + 1
    return ansDict      
    
def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    ansDict = number_of_descendants_helper(S, root, {}, [root])
    return ansDict

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order_helper(S, root, po, ansDict, visited = []):
    
    children = S[root].keys()
    
    # children "down" the tree
    properChildren = []
    redChildren = []
    
    # find proper children
    for child in children:
        if S[root][child] == 'red':
            redChildren.append(child)
            continue
        if child in visited:
            continue
        properChildren.append(child)
        if child not in visited:        
            visited += [child]
            
    if not properChildren:
        # check red edges
        if redChildren:
            lowestPO = po[redChildren[0]]
            for redChild in redChildren:
                if po[redChild] < lowestPO:
                    lowestPO = po[redChild]
            if lowestPO < po[root]:
                ansDict[root] = lowestPO
                return ansDict
        ansDict[root] = po[root] 
        return ansDict
        
    for child in properChildren:
        lowest_post_order_helper(S, child, po, ansDict, visited)
    lowestPO = ansDict[properChildren[0]]
    for child in properChildren:
        if ansDict[child] < lowestPO:
            lowestPO = ansDict[child]
    # check red edges
    for redChild in redChildren:
        if po[redChild] < lowestPO:
            lowestPO = po[redChild]
    ansDict[root] = lowestPO
    return ansDict    

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    ansDict = lowest_post_order_helper(S, root, po, {}, visited = [root])
    return ansDict
    

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2} or \
           l == {'a':1, 'b':4, 'c':1, 'd':1, 'e':1, 'f':1, 'g':1}


################

def highest_post_order_helper(S, root, po, ansDict, visited = []):
    
    children = S[root].keys()
    
    # children "down" the tree
    properChildren = []
    redChildren = []
    
    # find proper children
    for child in children:
        if S[root][child] == 'red':
            redChildren.append(child)
            continue
        if child in visited:
            continue
        properChildren.append(child)
        if child not in visited:        
            visited += [child]
            
    if not properChildren:
        # check red edges
        if redChildren:
            highestPO = po[redChildren[0]]
            for redChild in redChildren:
                if po[redChild] > highestPO:
                    highestPO = po[redChild]
            if highestPO > po[root]:
                ansDict[root] = highestPO
                return ansDict
        ansDict[root] = po[root] 
        return ansDict
        
    for child in properChildren:
        highest_post_order_helper(S, child, po, ansDict, visited)
    highestPO = ansDict[properChildren[0]]
    for child in properChildren:
        if ansDict[child] > highestPO:
            highestPO = ansDict[child]
    # check red edges
    for redChild in redChildren:
        if po[redChild] > highestPO:
            highestPO = po[redChild]
    if po[root] > highestPO:
        highestPO = po[root]
    ansDict[root] = highestPO
    return ansDict

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    ansDict = highest_post_order_helper(S, root, po, {}, visited = [root])
    return ansDict

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3} or \
           h == {'a':7, 'b':6, 'c':6, 'd':6, 'e':3, 'f':2, 'g':2}
    
#################

def bridge_edges(G, root):
    
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    rootedSpanningTree = create_rooted_spanning_tree(G, root)
    postOrderedNodes = post_order(rootedSpanningTree, root)
    noOfDescendantsDict = number_of_descendants(rootedSpanningTree, root)
    lowestPODict = lowest_post_order(rootedSpanningTree, root, postOrderedNodes)
    highestPODict = highest_post_order(rootedSpanningTree, root, postOrderedNodes)
        
    # list of bridge edges, the hero of the day
    bridgeEdges = []
    
    # get each edge and check conditions
    
    visitedNodes = [root]
    newParents = [root]
    
    # run for as long as there are parents nodes
    while newParents:
        newChildren = []
        for parent in newParents:
            children = rootedSpanningTree  [parent].keys()
            for child in children:
#                if parent == 'd' and child == 'e':
#                    print 'd-e condition reached'
                if child in visitedNodes:
                    # means the child was an earlier parent
                    continue
                if rootedSpanningTree[parent][child] == 'red':
                    # ignore red children
                    continue
                else:
                    # child has not been visited
                    # check the constraints for the child
                    if (highestPODict[child] <= postOrderedNodes[child]) and \
                       (lowestPODict[child] > (postOrderedNodes[child] - noOfDescendantsDict[child])):
                           bridgeEdges.append((parent, child))
                    newChildren.append(child)
                    visitedNodes.append(child)
        # children have become the new parents
        # ah, how the sands of time have changed!!
        newParents = newChildren
        
    return bridgeEdges
    

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')] or bridges == [('e', 'd')]
