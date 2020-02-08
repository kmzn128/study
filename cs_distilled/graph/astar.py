import math
import heapq

dungeon = [
        'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
        'OS  O     O     O         O          O',
        'O   O  O  O  O            O    OOOO  O',
        'O      O     O  O   OOOO  O    O  OOOO',
        'OOOOOOOOOOOOOOOOOO  O     O    O     O',
        'O                O  O     O          O',
        'O        OOO     O  O     OOOOOOOOO  O',
        'OG OO    O    OOOO  O     O      OO  O',
        'O   O    O          O     O  O   O   O',
        'O   OOO  O          O        O   O   O',
        'O        O          O        O       O',
        'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
        ]

def find_char(ch):
    for i, row in enumerate(dungeon):
        for j, c in enumerate(row):
            if(c == ch):
                return (i,j)

POS_START = find_char('S')
POS_GOAL = find_char('G')

            
def reachable(i,j):
    if(i < 0 or i >= len(dungeon)):
        return False
    if(j < 0 or j >= len(dungeon[0])):
        return False
    if(dungeon[i][j] == 'O' or dungeon[i][j] == 'S'):
        return False
    return True
    
four_dir = [(1,0),(-1,0),(0,1),(0,-1)]

def show_next_step(pos):
    ans = set()
    for dir in four_dir:
        pos0 = pos[0] + dir[0]
        pos1 = pos[1] + dir[1]
        if(reachable(pos0, pos1)):
            ans.add((pos0, pos1))
    return ans

def calc_distance(pos):
    return math.sqrt(((pos[0]-POS_GOAL[0])**2) + \
                     ((pos[1]-POS_GOAL[1])**2) \
                    )                    

def output(path):
    li = [list(row) for row in dungeon]
    for pos in path:
        li[pos[0]][pos[1]] = "*"
    for row in li:
        print("".join(row))
        

def main():
    path = [POS_START]
    score = len(path) + calc_distance(POS_START)
    searching_heap = []
    checked = {POS_START: score}
    heapq.heappush(searching_heap, (score, path))
    while(len(searching_heap) > 0):
        score, path = heapq.heappop(searching_heap)
        latest_pos = path[-1]
        if(latest_pos == POS_GOAL):
            output(path)
        next_poses = show_next_step(latest_pos)
        for np in next_poses:
            new_path = path + [np]
            new_score = len(new_path) + calc_distance(np)
            if(np in checked and checked[np] <= new_score):
                continue
            else:
                checked[np] = new_score
                heapq.heappush(searching_heap, (new_score, new_path))
        
main()
    
    