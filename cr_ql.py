from envirment import envirment
from QL import QLearningTable
import numpy as np
class River:
    def __init__(self,x=3,y=3,b=2):
        self.x=x
        self.y=y
        self.b=b
        self.initial_state = (x, y, 'left') 
        self.final_state = (0, 0, 'right') 
        self.state=(x, y, 'left') 
        self.reword=0
        self.step=0
    def reset(self):
        self.state=(x, y, 'left') 
        self.reword=0
        self.step=0
    def act(self):

    def step(self,act):
        next_state=self.get_next_states(self.state)

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
    



class Qlearning:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((env.x+1, env.y+1, 2, env.b+1, env.b+1, env.x+1, env.y+1, 2))
    
    def choose_action(self, state):
        if np.random.uniform() < self.epsilon:
            return np.random.choice(self.env.get_actions(state))
        else:
            return np.argmax(self.q_table[state])
    
    def step(self, state, action):
        next_state = self.env.get_next_state(state, action)
        reward = self.env.get_reward(next_state)
        done = self.env.is_done(next_state)
        return next_state, reward, done
    
    def reset(self):
        self.env.reset()
    
    def train(self, episodes=1000):
        for episode in range(episodes):
            state = self.env.get_state()
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done = self.step(state, action)
                q_next = np.max(self.q_table[next_state])
                self.q_table[state][action] += self.alpha * (reward + self.gamma * q_next - self.q_table[state][action])
                state = next_state
    
    def test(self):
        self.reset()
        state = self.env.get_state()
        done = False
        while not done:
            action = np.argmax(self.q_table[state])
            next_state, reward, done = self.step(state, action)
            state = next_state
            self.env.plot_state(state)

if __name__ == "__main__":
    env = envirment()
    RL = QLearningTable(actions=list(range(env.n_action)))

    env.after(100, update)
    env.mainloop()