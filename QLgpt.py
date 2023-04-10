# Define the initial state of the problem
initial_state = {'left': {'good_guys': 3, 'bad_guys': 3, 'boat': False}, 'right': {'good_guys': 0, 'bad_guys': 0, 'boat': False}}

# Define the goal state of the problem
goal_state = {'left': {'good_guys': 0, 'bad_guys': 0, 'boat': False}, 'right': {'good_guys': 3, 'bad_guys': 3, 'boat': False}}

# Define the actions that can be taken
actions = [('good_guys', 1, 0), ('bad_guys', 1, 0), 
('good_guys', 2, 0), ('bad_guys', 2, 0), 
('good_guys', 0, 1), ('bad_guys', 0, 1), 
('good_guys', 0, 2), ('bad_guys', 0, 2)]

# Define the function to check if a state is valid
def is_valid(state):
    if state['left']['good_guys'] >= state['left']['bad_guys'] or state['right']['good_guys'] >= state['right']['bad_guys']:
        return False
    return True

# Define the function to apply an action to a state
def apply_action(state, action):
    new_state = {'left': {'good_guys': state['left']['good_guys'], 'bad_guys': state['left']['bad_guys'], 'boat': not state['left']['boat']}, 'right': {'good_guys': state['right']['good_guys'], 'bad_guys': state['right']['bad_guys'], 'boat': not state['right']['boat']}}
    if action[0] == 'good_guys':
        new_state['left']['good_guys'] -= action[1]
        new_state['right']['good_guys'] += action[1]
    elif action[0] == 'bad_guys':
        new_state['left']['bad_guys'] -= action[1]
        new_state['right']['bad_guys'] += action[1]
    return new_state

# Define the function to check if a state is the goal state
def is_goal(state):
    if state == goal_state:
        return True
    return False

# Define the function to solve the problem using breadth-first search
def bfs():
    queue = [(initial_state, [])]
    while queue:
        state, path = queue.pop(0)
        if is_goal(state):
            return path
        for action in actions:
            new_state = apply_action(state, action)
            if is_valid(new_state):
                new_path = path + [action]
                queue.append((new_state, new_path))

if __name__=='__main__':
    bfs()