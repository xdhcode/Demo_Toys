import os
import time
import numpy as np
import pandas as pd
from tqdm import tqdm



class envirment():
    def __init__(self,N=3,M=3):
        self.main_path='E:\\0-Work\\Data\\2-crossriver'
        self.N=N
        self.M=M
        #action
        self.action=['商人护卫→','商人商人→','护卫护卫→','商人→','护卫→','商人护卫←','商人商人←','护卫护卫←','商人←','护卫←']
        self.act_dim=1#动作空间
        self.n_action=len(self.action)
        #observation
        self.state=np.array([N,M,0])#初始位置0-left 1-right
        self.state_dim=len(self.state)
        #environment
        self.steps=0
        self.reward=0
        self.max_episode_steps=100#环境中的最大步数
        self.record=pd.DataFrame()
        self.history=[]
        self.gg=False

    def seed(self,seed):
        np.random.seed(seed)

    def reset(self):
        self.steps=0
        self.reward=0
        self.boat='left'
        self.state=np.array([self.N,self.M,0])
        self.record=pd.DataFrame()
        self.gg=False
        return self.state
    
    def act_sample(self):
        act=np.random.randint(-self.n_action,self.n_action+0.5, size=self.act_dim)
        return act

    def act(self,act):
        score=-0.05
        cross=False
        if self.state[2]==0:
            if act==-5:#'商人护卫→'
                if (self.state-1>=0).all():
                    self.state+=-1
                    cross=True
            elif act==-4:#'商人商人→'
                if self.state[0]-2>=0:
                    self.state[0]+=-2
                    cross=True
            elif act==-3:#'护卫护卫→'
                if self.state[1]-2>=0:
                    self.state[1]+=-2
                    cross=True
            elif act==-2:#'商人→'
                if self.state[0]-1>=0:
                    self.state[0]+=-1
                    cross=True
            elif act==-1:#'护卫→'
                if self.state[1]-1>=0:
                    self.state[1]+=-1
                    cross=True
            else:
                pass

            if cross:
                self.state[2]=1
            else:
                score=-0.85

        elif self.state[2]==1:
            if act==0:#'商人护卫←'
                if self.state[0]+1<=self.N and self.state[1]+1<=self.M:
                    self.state+=1
                    cross=True
            elif act==1:#'商人商人←'
                if self.state[0]+2<=self.N:
                    self.state[0]+=2
                    cross=True
            elif act==2:#'护卫护卫←'
                if self.state[1]+2<=self.M:
                    self.state[1]+=2
                    cross=True
            elif act==3:#'商人←'
                if self.state[0]+1<=self.N:
                    self.state[0]+=1
                    cross=True
            elif act==4:#'护卫←'
                if self.state[1]+1<=self.M:
                    self.state[1]+=1
                    cross=True
            else:
                pass
            
            if cross:
                self.state[2]=0
            else:
                score=-0.85

        if self.state[0]<self.state[1]:
            if self.state[0]!=0:
                self.gg=True
                score=-2
        if (self.N-self.state[0])<(self.M-self.state[1]):
            if (self.N-self.state[0])!=0:
                self.gg=True
                score=-2

        self.history.append(self.state)
        flag=0
        for i in range(len(self.history)):
            if (self.history[i]==self.state).all():
                flag=1
        if flag==1:#重复扣分
            score=-0.3

        return score
    
    def step(self,act):
        self.steps+=1
        if self.steps % 10==0:
            print('env step:',self.steps)
        
        score=self.act(act)
        
        if self.gg:
            done=True
        else:
            self.record=pd.concat([self.record,pd.DataFrame(self.state).T],axis=0)

            if self.state[0]==0 and self.state[1]==0:
                done=True
                self.reward+=1
                if self.reward==1:
                    self.record.reset_index(drop=True)
                    self.record.to_csv(self.main_path+'\\envirment_record.csv')
            elif self.steps>=self.max_episode_steps: 
                done=True
            else:
                done=False
            self.reward+=score
        return self.state,self.reward,done

if __name__=='__main__':
    a=envirment()
