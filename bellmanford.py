import geopandas as gpd
import networkx as nx
import numpy as np
import momepy
import time

def bellmanford(Graph):
    # Gainesville Fire Station
    Graph.nodes[(-9164362.209753478, 3458275.7772084177)]['dist'] = 0
    for i in range(len(list(G.nodes)) - 1):
      for from_vertex in Graph.nodes:
          neighbors = Graph.__getitem__(from_vertex)
          for to_vertex in neighbors:
              du = Graph.nodes[from_vertex]['dist']
              wt = neighbors[to_vertex][0]['LengthM']
              dv = Graph.nodes[to_vertex]['dist']
              if du + wt < dv:
                  Graph.nodes[to_vertex]['dist'] = du + wt
                  Graph.nodes[to_vertex]['pred'] = from_vertex
    return Graph

# Based off of pseudocode from discussion slides
# repeat V - 1 times
# for each edge(from u, to v) with weight w in edges do:
#     if dist[u] + w < dist[v] then
#         dist[v] = dist[u] + w
#         pred[v] = u

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
    result = bellmanford(G)
    end = time.time()
    print("The algorithm took ", (end-start), " seconds to run.")