# Define the initial and final states
import matplotlib.pyplot as plt

x=3
y=3

initial_state = (x, y, 'left') # 'left' represents the boat on the initial side
final_state = (0, 0, 'right') # 'right' represents the boat on the final side

# Define the function to check if a state is valid
def is_valid(state):
    if state[0] < 0 or state[1] < 0 or state[0] > x or state[1] > y:
        return False
    if state[0] > 0 and state[0] < state[1]:
        return False
    if x - state[0] > 0 and x - state[0] < y - state[1]:
        return False
    return True

# Define the function to get the next valid states
def get_next_states(state):
    next_states = []
    if state[2] == 'left': # Boat is on the initial side
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2:
                    next_state = (state[0]-i, state[1]-j, 'right')
                    if is_valid(next_state):
                        next_states.append(next_state)
    else: # Boat is on the final side
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2:
                    next_state = (state[0]+i, state[1]+j, 'left')
                    if is_valid(next_state):
                        next_states.append(next_state)
    return next_states

# Define the bfs function to find the path from the initial to the final state
def bfs():
    visited = set()
    queue = [[initial_state]]
    if initial_state == final_state:
        return [initial_state]
    while queue:
        path = queue.pop(0)
        state = path[-1]
        if state not in visited:
            visited.add(state)
            for next_state in get_next_states(state):
                if next_state not in visited: # check if next_state is already visited
                    new_path = list(path)
                    new_path.append(next_state)
                    if next_state == final_state:
                        return new_path
                    queue.append(new_path)
    return None



# Define the dfs function to find the path from the initial to the final state
def dfs():
    visited = set()
    stack = [[initial_state]]
    if initial_state == final_state:
        return [initial_state]
    while stack:
        path = stack.pop()
        state = path[-1]
        if state not in visited:
            visited.add(state)
            for next_state in get_next_states(state):
                new_path = list(path)
                new_path.append(next_state)
                if next_state == final_state:
                    return new_path
                stack.append(new_path)
    return None

# Call the bfs function and plot the result step by step with the arrow indicating the movement of the state
import time
result = dfs()
# result = dfs()
if result:
    X = []
    Y = []
    for state in result:
        X.append(state[0])
        Y.append(state[1])
    vector = list(zip(X, Y))
    for i in range(len(vector)-1):
        print(result[i])
        plt.text(vector[i+1][0], vector[i+1][1], str(i+1), fontsize=12, color='red', horizontalalignment='center', verticalalignment='center')
        plt.arrow(vector[i][0], vector[i][1], vector[i+1][0]-vector[i][0], vector[i+1][1]-vector[i][1], length_includes_head=True, head_width=0.1)
        plt.xlim(-1, 4)
        plt.ylim(-1, 4)
        plt.title('Boat:'+result[i][2])
        plt.xlabel('Good guys')
        plt.ylabel('Bad guys')
        plt.pause(1)  
    plt.arrow(vector[-2][0], vector[-2][1], vector[-1][0]-vector[-2][0], vector[-1][1]-vector[-2][1], length_includes_head=True, head_width=0.1)
    plt.text(vector[-1][0], vector[-1][1], str(len(vector)), fontsize=12, color='red', horizontalalignment='center', verticalalignment='center')
    plt.xlim(-1, 4)
    plt.ylim(-1, 4)
    plt.title('Boat:'+result[-1][2])
    plt.xlabel('Good guys')
    plt.ylabel('Bad guys')
    plt.show()
else:
    print("No solution found")



















