import heapq

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

def dijkstra_again(start, goal):
    path = [start]
    score = 0
    searching_heap = []
    checked = {start: score}
    heapq.heappush(searching_heap, (score, path))
    while(len(searching_heap) > 0):
        score, path = heapq.heappop(searching_heap)
        latest_pos = path[-1]
        if(latest_pos == goal):
            print(score)
            print(path)
            print(searching_heap)
        for next_pos, weight in example_graph[latest_pos].items():
            new_path = path + [next_pos]
            new_score = score + weight
            if(next_pos in checked and checked[next_pos] <= new_score):
                continue
            else:
                checked[next_pos] = new_score
                heapq.heappush(searching_heap, (new_score, new_path)) 

dijkstra_again('U', 'Z')