example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

import collections
import math

def bellman_ford(g,s):
    distance = collections.defaultdict(int)
    for key in g: 
        distance[key] = math.inf
    distance[s] = 0
    for key in g:
        for key2 in g[key]:
            if(distance[key] != math.inf):
                if(distance[key2] > distance[key] + g[key][key2]):
                    distance[key2] = distance[key] + g[key][key2]
    return distance               
    

print(bellman_ford(example_graph, 'U'))