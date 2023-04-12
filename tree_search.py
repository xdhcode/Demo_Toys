import matplotlib.pyplot as plt
class CrossRiver:
    def __init__(self, x, y, b):
        self.x = x
        self.y = y
        self.b = b
        self.initial_state = (x, y, 'left') 
        self.final_state = (0, 0, 'right') 
    
    def is_valid(self, state):
        if state[0] < 0 or state[1] < 0 or state[0] > self.x or state[1] > self.y:
            return False
        if state[0] > 0 and state[0] < state[1]:
            return False
        if self.x - state[0] > 0 and self.x - state[0] < self.y - state[1]:
            return False
        return True
    
    def get_next_states(self, state):
        next_states = []
        if state[2] == 'left':
            for i in range(3):
                for j in range(3):
                    if i + j > 0 and i + j <= self.b:
                        next_state = (state[0]-i, state[1]-j, 'right')
                        if self.is_valid(next_state):
                            next_states.append(next_state)
        else:
            for i in range(3):
                for j in range(3):
                    if i + j > 0 and i + j <= self.b:
                        next_state = (state[0]+i, state[1]+j, 'left')
                        if self.is_valid(next_state):
                            next_states.append(next_state)
        return next_states
    
    def bfs(self):
        visited = set()
        queue = [[self.initial_state]]
        if self.initial_state == self.final_state:
            return [self.initial_state]
        while queue:
            path = queue.pop(0)
            state = path[-1]
            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    new_path = list(path)
                    new_path.append(next_state)
                    if next_state == self.final_state:
                        return new_path
                    queue.append(new_path)
        return None
    
    def dfs(self):
        visited = set()
        stack = [[self.initial_state]]
        if self.initial_state == self.final_state:
            return [self.initial_state]
        while stack:
            path = stack.pop()
            state = path[-1]
            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    new_path = list(path)
                    new_path.append(next_state)
                    if next_state == self.final_state:
                        return new_path
                    stack.append(new_path)
        return None
    
    def plot_result(self, result):
        if result:
            X = []
            Y = []
            for state in result:
                X.append(state[0])
                Y.append(state[1])
            vector = list(zip(X, Y))
            for i in range(len(vector)-1):
                print(result[i])
                plt.text(vector[i+1][0]+0.02*i, vector[i+1][1]+0.04*i, str(i+1), fontsize=12, color='red', horizontalalignment='center', verticalalignment='center')
                plt.arrow(vector[i][0], vector[i][1], vector[i+1][0]-vector[i][0], vector[i+1][1]-vector[i][1], length_includes_head=True, head_width=0.1)
                plt.xlim(-1, self.x+1)
                plt.ylim(-1, self.y+1)
                plt.title('Boat:'+result[i][2])
                plt.xlabel('Good guys')
                plt.ylabel('Bad guys')
                plt.pause(1)  
            print(result[-1])
            plt.show()
        else:
            print("No solution found")
    
    def draw_movement(self, result):
        if result:
            for i in range(len(result)):
                state = result[i]
                x=state[0]
                y=state[1]
                side=state[2]
                good_guy = 'o'
                bad_guy = 's'
                boat = '^'

                plt.clf()
                plt.axvline(x=3, color='b')
                if side == 'left':
                    plt.scatter(2, self.x, marker=boat, color='y')
                else:
                    plt.scatter(4, self.x, marker=boat, color='y')
                for i in range(x):
                    plt.scatter(1,i,marker=good_guy,color='g')
                for i in range(y):
                    plt.scatter(1,self.x+i,marker=bad_guy,color='r')
                for i in range(self.x-x):
                    plt.scatter(5,i,marker=good_guy,color='g')
                for i in range(self.y-y):
                    plt.scatter(5, self.x+i,marker=bad_guy,color='r')
                plt.xlim(0, 6)
                plt.ylim(-1, self.x+self.y+1)
                plt.title('Cross River')
                plt.pause(1)
            plt.show()

cross_river = CrossRiver(3, 3, 2)
result = cross_river.bfs()#dfs/bfs
cross_river.plot_result(result)
cross_river.draw_movement(result)