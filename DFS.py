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



# Call the bfs function and plot the result step by step with the arrow indicating the movement of the state
import time
result = dfs()
if result:
    x = []
    y = []
    for state in result:
        x.append(state[0])
        y.append(state[1])
    vector = list(zip(x, y))
    for i in range(len(vector)-1):
        plt.arrow(vector[i][0], vector[i][1], vector[i+1][0]-vector[i][0], vector[i+1][1]-vector[i][1], length_includes_head=True, head_width=0.1)
        plt.scatter(vector[i][0], vector[i][1], marker='o', s=100, color='blue')
        plt.text(vector[i][0], vector[i][1], str(i+1), fontsize=12, color='white', horizontalalignment='center', verticalalignment='center')
        plt.xlim(-1, 4)
        plt.ylim(-1, 4)
        plt.pause(1)
    plt.scatter(vector[-1][0], vector[-1][1], marker='o', s=100, color='blue')
    plt.text(vector[-1][0], vector[-1][1], str(len(vector)), fontsize=12, color='white', horizontalalignment='center', verticalalignment='center')
    plt.xlim(-1, 4)
    plt.ylim(-1, 4)
    plt.show()
else:
    print("No solution found")











