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

def warshall(g):
    le = len(g)
    keys = g.keys() 
    distances = collections.defaultdict(collections.defaultdict)
    for key in keys:
        row = collections.defaultdict(int)
        for key2 in keys:
            if key2 in g[key]:
                row[key2] = g[key][key2]
            elif(key == key2):
                row[key2] = 0
            else:
                row[key2] = math.inf
        distances[key] = row
    for key in keys:
        for key2 in distances:
            for key3 in distances[key2]:
                distances[key2][key3] = min(distances[key2][key3], \
                                           distances[key2][key] + distances[key][key3])
    return distances

print(warshall(example_graph))