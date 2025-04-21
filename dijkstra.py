# Dijkstra's Algorithm Implementation
import heapq


def Dijkstra(Graph, start=963):
    # Initialize everything
    # Start is the index of Gainesville's Fire Station
    for node in Graph.nodes:
        Graph.nodes[node]['distance'] = float('inf')
        Graph.nodes[node]['predecessor'] = None
        Graph.nodes[start]['distance'] = 0
    # Initialize priority queue
    pq = [(0, start)]
    visitedNodes = set()

    while pq:
        current_distance, current = heapq.heappop(pq)
        if current in visitedNodes:
            continue
        visitedNodes.add(current)
        for neighboringNodes in Graph[current]:
            weight = Graph[current][neighboringNodes][0]['LengthM']
            distance = current_distance + weight

            # If distance is less than the current distance, update
            if distance < Graph.nodes[neighboringNodes]['distance']:
                Graph.nodes[neighboringNodes]['distance'] = distance
                Graph.nodes[neighboringNodes]['predecessor'] = current
                heapq.heappush(pq, (distance, neighboringNodes))