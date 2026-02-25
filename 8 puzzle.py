from collections import deque

goal_state = [[1,2,3],[4,5,6],[7,8,0]]
start_state = [[1,2,3],[4,0,6],[7,5,8]]

def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == goal_state

def generate_children(state):
    i, j = get_blank_pos(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    children = []
    for dx, dy in moves:
        x, y = i+dx, j+dy
        if 0<=x<3 and 0<=y<3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            children.append(new_state)
    return children

def bfs(start):
    visited = []
    queue = deque([start])
    steps = 0
    while queue:
        node = queue.popleft()
        steps += 1
        # Convert list of lists to tuple of tuples for hashing in visited set
        node_tuple = tuple(tuple(row) for row in node)
        if node_tuple in visited:
            continue
        visited.append(node_tuple)
        # print(f"Step {steps}: {node}") # Uncomment to see steps
        if is_goal(node):
            return "Goal Reached!"
        
        for child in generate_children(node):
            child_tuple = tuple(tuple(row) for row in child)
            if child_tuple not in visited:
                queue.append(child)
    return "Goal Not Found"

# Run the BFS
result = bfs(start_state)
print(result)