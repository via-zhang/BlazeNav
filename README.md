# BlazeNav
Team project for Data Structures and Algorithms, Spring 2025

Comparing Bellman-Ford and Dijkstra's Algorithms to find the shortest path between the Gainesville Fire Station #1 and a user-inputted fire location.

The **BlazeNav.ipynb** is the main Jupyter Notebook that hosts the main project and functions. The dijkstra.py and bellmanford.py files provide supplementary code that focuses on each algorithm. You can run the **BlazeNav.ipynb** notebook for an interactive way to find the shortest path given an inputted fire location. Alternatively, you can run ```python dijkstra.py``` in your command line to find the ammount of time it takes for Dijkstra's Algorithm to find the shorest path from the Gainesville Fire Station to every other node in the graph of road networks. You can do the same for the Bellman-Ford Algorithm by running ```python bellmanford.py```

## Dependencies
Python packages: geopandas, matplotlib, momepy, networkx, numpy, contextily, libpysal, shapely, heapq
