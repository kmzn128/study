from collections import deque
def bfs(graph, start_node, key):
    next_nodes = deque([])
    seen_nodes = set()
    
    next_nodes.append(start_node)
    seen_nodes.add(start_node)
    
    while next_nodes:
        node = next_nodes.popleft()
        print(node)
        if node == key:
            return node
        if node in graph:
            for n in graph[node]:
                if not n in seen_nodes:
                    next_nodes.append(n)
                    seen_nodes.add(n)
    return

graph = {
    'A':['B','C','D'],
    'B':['E','F','G'],
    'E':['H','I'],
    'C':['J'],
    'J':['K'],
    'D':['L','M'],
    'M':['N']
    }

bfs(graph, 'A','E')