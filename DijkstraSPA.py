# Program that implements Dijkstra's algorithm

def shortest_dist_node(dist):
    allNodes = dist.keys()
    bestNode = allNodes[0]
    smallestDist = dist[bestNode]
    for v in dist:
        if dist[v] < smallestDist:
            (bestNode, smallestDist) = (v, dist[v])
    return bestNode

def dijkstra(graph, startNode):
    dist_so_far = {}
    dist_so_far[startNode] = 0
    final_dist = {}
    while len(final_dist) < len(graph) and dist_so_far:
        shortestNode = shortest_dist_node(dist_so_far)
        # lock it down!                                                                                                                                                                                     
        final_dist[shortestNode] = dist_so_far[shortestNode]
        del dist_so_far[shortestNode]
        for neighbor in graph[shortestNode]:
            if neighbor not in final_dist:
                if neighbor not in dist_so_far:
                    dist_so_far[neighbor] = final_dist[shortestNode] + graph[shortestNode][neighbor]
                elif final_dist[shortestNode] + graph[shortestNode][neighbor] < dist_so_far[neighbor]:
                    dist_so_far[neighbor] = final_dist[shortestNode] + graph[shortestNode][neighbor]
    return final_dist