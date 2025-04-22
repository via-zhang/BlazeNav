import geopandas as gpd
import networkx as nx
import numpy as np
import heapq
import momepy
import time

def dijkstra(Graph):
    # Initialize everything
    # Start is the index of Gainesville's Fire Station
    Graph.nodes[(-9164362.209753478, 3458275.7772084177)]['dist'] = 0
    # Initialize priority queue
    pq = [(0, (-9164362.209753478, 3458275.7772084177))]
    visitedNodes = set()

    while pq:
        current_distance, current = heapq.heappop(pq)
        if current in visitedNodes:
            continue
        visitedNodes.add(current)
        currentNeighbors = Graph.__getitem__(current)
        for neighboringNodes in currentNeighbors:
            weight = currentNeighbors[neighboringNodes][0]['LengthM']
            distance = current_distance + weight

            # If distance is less than the current distance, update
            if distance < Graph.nodes[neighboringNodes]['dist']:
                Graph.nodes[neighboringNodes]['dist'] = distance
                Graph.nodes[neighboringNodes]['pred'] = current
                heapq.heappush(pq, (distance, neighboringNodes))
    return Graph

if __name__ == '__main__':
    # Read road network data in Alachua County (181,572 rows)
    roads = gpd.read_file('road_vertices_3857.zip')[['LengthM', 'geometry', 'FULLNAME', 'MTFCC', 'StartX', 'StartY']]
    # Subset to primary and secondary roads (19,398)
    roads = roads[(roads['MTFCC'] == 'S1100') | (roads['MTFCC'] == 'S1200')]

    # Create graph (based on Networkx documentation)
    G = momepy.gdf_to_nx(roads, approach="primal", length="LengthM")
    nx.set_node_attributes(G, np.inf, "dist")
    nx.set_node_attributes(G, None, "pred")

    start = time.time()
    result = dijkstra(G)
    end = time.time()
    print("The algorithm took ", (end-start), " seconds to run.")