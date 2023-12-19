# Graph Algorithms (BFS, DFS, Shortest Paths)

num_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
print("__nodes1__ => ", num_nodes1, len(edges1))

# Depth-first search 
num_nodes3 = 9
edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
print("__nodes3__ => ", num_nodes3, len(edges3))

# Directed graph
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
print("__nodes6__ => ", num_nodes6, len(edges6))

#------Weighted Graphs----
# Graph with weights
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
print("__nodes5__ => ", num_nodes5, len(edges5))

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
print("__nodes7__ => ", num_nodes7, len(edges7))

# Adjacency List
class Graph:
    def __init__(self, num_nodes, edges):
        # create an empty list [] in range of nodes(num_nodes)
        self.data = [[] for _ in range(num_nodes)]
        for v1, v2 in edges:
            # pair v1, v2: v1 is node1 & v2 is node2
            # insert into the right list
            self.data[v1].append(v2)
            self.data[v2].append(v1)
            
    def __repr__(self):
        # creating a string with => "{} : {}".format(i, neighbors)
        # and join them with "\n".join() in new line
        return "\n".join(["{} : {}".format(i, neighbors) for (i, neighbors) in enumerate(self.data)])
    # when we have print we use str function
    def __str__(self):
        return repr(self)
    
# create graph g1 and give it number of node and edges
g1 = Graph(num_nodes1, edges1)
print("__g1.data__ => ", g1.data)
print("__g1 is represented by__str__ => ", g1)

# Breadth First Search
def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []
    
    visited[source] = True    
    queue.append(source)
    i = 0
    
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1
        
    return queue

print("___with bfs___: ", bfs(g1, 3))

# Depth First Search
def dfs(graph, source):
    visited = [False] * len(graph.data)
    stack = [source]
    result = []
    
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            result.append(current)
            visited[current] = True
            for v in graph.data[current]:
                stack.append(v)
                
    return result

print("___with dfs___: ", dfs(g1, 0))

# Directed and Weighted Graph
class Graph:
    def __init__(self, num_nodes, edges, directed=False):
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        
        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3
            
        for e in edges:
            self.data[e[0]].append(e[1])
            if self.weighted:
                self.weight[e[0]].append(e[2])
            
            if not directed:
                self.data[e[1]].append(e[0])
                if self.weighted:
                    self.data[e[1]].append(e[2])
                
    def __repr__(self):
        result = ""
        for i in range(len(self.data)):
            pairs = list(zip(self.data[i], self.weight[i]))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __str__(self):
        return repr(self)
    
g7 = Graph(num_nodes7, edges7, directed=True)
print("__class Graph__str => ", g7)
print("__weight__  => ", g7.weight)

# Shortest Path - Dijkstra's Algorithm
def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
        
def shortest_path(graph, source, dest):
    """Find the length of the shortest path between source and destination"""
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []
    idx = 0
    
    queue.append(source)
    distance[source] = 0
    visited[source] = True
    
    while idx < len(queue) and not visited[dest]:
        current = queue[idx]
        update_distances(graph, current, distance, parent)
        
        next_node = pick_next_node(distance, visited)
        if next_node is not None:
            visited[next_node] = True
            queue.append(next_node)
        idx += 1

    return distance[dest], distance, parent

print("__Shortest Path is__ => ", shortest_path(g7, 0, 5))





