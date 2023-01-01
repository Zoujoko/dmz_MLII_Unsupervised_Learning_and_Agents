from agent import Agent

# state = 1 sur 8 
# actions = left / right / none
# rewards = reward

direction = "left"
WORLD_UPDATE_PERIOD = 10
rounds = WORLD_UPDATE_PERIOD

def dmz_policy(agent: Agent) -> str:
    global direction
    global rounds
    
    if rounds == 0:
        rounds = WORLD_UPDATE_PERIOD
    else:
        rounds = rounds - 1
        
    if agent.position == 0:
            direction = "right"
    elif agent.position == 7:
            direction = "left"
            
    return calculate_weights(agent)
    

def calculate_weights(agent: Agent):
    delta = 0
    weights = [0,0,0,0,0,0,0,0]
    
    for i in range(8):
        if i > agent.position:
            delta = i - agent.position
        elif i < agent.position:
            delta = agent.position - i
        else:
            delta = 0
        weights[i] = (rounds - delta) * agent.known_rewards[i] 
    
    max = 0
    place_max = agent.position
    for i in range(8):
        if weights[i] > max:
            max = weights[i]
            place_max = i
    if (agent.known_rewards[place_max] < 30):
        return direction
    if max == 0:
        return direction
    else:
        return calculate_direction(agent, place_max)
    
def calculate_direction(agent: Agent, i: int) -> str:
    if i == agent.position:
        return 'none'
    elif i > agent.position:
        return 'right'
    elif i < agent.position:
        return 'left'