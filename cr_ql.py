from envirment import envirment
from QL import QLearningTable

if __name__ == "__main__":
    env = envirment()
    RL = QLearningTable(actions=list(range(env.n_action)))

    env.after(100, update)
    env.mainloop()