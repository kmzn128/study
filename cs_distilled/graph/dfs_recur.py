def _dfs(graph, node, seen_nodes):
    print(node)
    seen_nodes.add(node)
    if node not in graph:
        return
    for n in graph[node]:
        if n not in seen_nodes:
            _dfs(graph, n, seen_nodes)
    

def dfs_recur(graph, start_node):
    next_nodes = []
    seen_nodes = set()
    _dfs(graph, start_node, seen_nodes)

graph = {
    'A':['B','C','D'],
    'B':['E','F','G'],
    'E':['H','I'],
    'C':['J'],
    'J':['K'],
    'D':['L','M'],
    'M':['N']
    }

g_undir = {
    1:[2,3],
    2:[1,2,4],
    3:[1,3,5],
    4:[2,5],
    5:[3,4,6],
    6:[5]
    }

dfs_recur(g_undir, 1)