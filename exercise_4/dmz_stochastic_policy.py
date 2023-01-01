from agent import Agent
import random

new = True
nodes = []


class Node:
    def __init__(self, left = 1/3, none = 1/3, right = 1/3) -> None:
        self.left = left
        self.none = none
        self.right = right
    
    def throw(self) -> str:
        rand = random.random()
        if rand > 0 and rand <= self.left:
            return 'left'
        elif rand > self.left and rand <= (self.none + self.left):
            return 'none'
        else:
            return 'right'
        
    def update_left(self, newValue):
        newLeftThreshold = 1 - newValue
        
        if (self.left > 0.80 or self.left < 0.20):
            return
        
        if (newValue > 0.80):
            newValue = 0.80
            newLeftThreshold = 0.20
        elif (newValue < 0.20):
            newValue = 0.20
            newLeftThreshold = 0.80
            
        if (self.right == 0):
            self.none = newLeftThreshold * (self.none + self.left)
            self.left = newValue
        else:
            self.none = newLeftThreshold * (self.none + self.left / 2)
            self.left = newValue
            self.right = newLeftThreshold * (self.right + self.left / 2)
            
            
    def update_right(self, newValue):
        newRightThreshold = 1 - newValue
        
        if (self.right > 0.80 or self.right < 0.20):
            return
        
        if (newValue > 0.80):
            newValue = 0.80
            newRightThreshold = 0.20
        elif (newValue < 0.20):
            newValue = 0.20
            newRightThreshold = 0.80
        if (self.left == 0):
            self.none = newRightThreshold * (self.none + self.right)
            self.right = newValue
        else:
            self.none = newRightThreshold * (self.none + self.right / 2)
            self.right = newValue
            self.left = newRightThreshold * (self.left + self.right / 2)
            
            
    def update_none(self, newValue):
        newNoneThreshold = 1 - newValue
        
        if (self.none > 0.80 and newValue > self.none) or (self.none < 0.20 and newValue < self.none):
            return
        
        if (newValue > 0.80):
            newValue = 0.80
            newNoneThreshold = 0.20
        elif (newValue < 0.20):
            newValue = 0.20
            newNoneThreshold = 0.80
        if (self.right == 0):
            self.left = newNoneThreshold * (self.left + self.none)
            self.none = newValue
        elif (self.left == 0):
            self.right = newNoneThreshold * (self.right + self.none)
            self.none = newValue
        else:
            self.left = newNoneThreshold * (self.left + self.none / 2)
            self.right = newNoneThreshold * (self.right + self.none / 2)
            self.none = newValue
        
def update_values(agent: Agent, node: Node):
    rewardValue = agent.known_rewards[agent.position]
    if rewardValue >= 30:
        increase = 1 + (rewardValue * 30 / 100) / 100
        node.update_none(node.none * increase)
    else:
        print(node.none)
        node.update_none(node.none * (1-(0.15 - 25 / 2 / 100)))
        print((1-(0.15 - 5 / 2 / 100)))
        print((1-(0.15 - 10 / 2 / 100)))
        print((1-(0.15 - 15 / 2 / 100)))
        print((1-(0.15 - 20 / 2 / 100)))
        print((1-(0.15 - 25 / 2 / 100)))
        print(node.none)
        breakpoint()
    if agent.position > 0 and agent.position < 7 and agent.known_rewards[agent.position - 1] > agent.known_rewards[agent.position + 1]:
        diff = agent.known_rewards[agent.position - 1] - agent.known_rewards[agent.position + 1]
        diffPer = 1 + (diff * 30 / 100) / 100
        node.update_left(node.left * diffPer)
    elif agent.position > 0 and agent.position < 7 and agent.known_rewards[agent.position - 1] < agent.known_rewards[agent.position + 1]:
        diff = agent.known_rewards[agent.position + 1] - agent.known_rewards[agent.position - 1]
        diffPer = 1 + (diff * 30 / 100) / 100
        node.update_right(node.right * diffPer)
        
def dmz_policy(agent: Agent) -> str:
    global new
    global nodes
    
    if new == True:
        new = False
        nodes = [Node(0,1/2,1/2), 
                 Node(),
                 Node(), 
                 Node(), 
                 Node(), 
                 Node(),
                 Node(), 
                 Node(1/2,1/2,0),]
    update_values(agent, (nodes[agent.position]))
    move = nodes[agent.position].throw()
    return move
