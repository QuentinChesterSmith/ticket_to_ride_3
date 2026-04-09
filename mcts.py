from environment import GameState, get_actions, apply_action, end_calculations
from routes import to_array
import numpy as np
import random, copy

routes_array = to_array()


draw_order = [
    np.array([0, 1]),
    np.array([0, 2]),
    np.array([0, 3]),
    np.array([0, 4]),
    np.array([0, 5]),
    np.array([1, 2]),
    np.array([1, 3]),
    np.array([1, 4]),
    np.array([1, 5]),
    np.array([2, 3]),
    np.array([2, 4]),
    np.array([2, 5]),
    np.array([3, 4]),
    np.array([3, 5]),
    np.array([4, 5]),
    np.array([5, 6])
]

class MCTSNode():
    def __init__(self, state, action=None, parent=None):
        self.state = state
        self.action = action
        self.parent = parent
        self.children = []
        self.visits = 0
        self.total_reward = 0
        self.untried_actions = get_actions(self.state.player_turn, self.state)

def ucb1(node, C=np.sqrt(2)):
    total_reward = node.total_reward
    child_visits = node.visits
    parent_visits = node.parent.visits

    exploitation = total_reward/child_visits
    exploration = C * np.sqrt(np.log(parent_visits)/child_visits)
    return exploitation + exploration

def basic_heuristics(actions, state):
    player = state.player_turn
    weights = []
    for action in actions:
        weight = 1.0 # Base weight

        if action[0] == 0:
            # Increase weight if length > 3
            route_idx = action[1]
            if routes_array[2][route_idx] > 3:
                weight += 0.15
        elif action[0] == 1:
            # Increase weight if collecting more cards of same type
            colors = state.deck[draw_order[action[1]]]
            if state.cards[player][colors[0]] > 0 or state.cards[player][colors[1]] > 0:
                weight += 0.2


        weights.append(weight)
    probs = np.array(weights)
    probs /= probs.sum()
    idx = np.random.choice(len(actions), p=probs)
    return actions[idx]

def selection(node):
    if len(node.children) == 0:
        return node # Terminal Leaf Node

    best = -9999
    best_node = None
    for child in node.children:
        value = ucb1(child)
        if value > best:
            best = value
            best_node = child
    if best_node is None:
        print(node.children)
        raise ValueError("Selection cannot find best node")
    else:
        return best_node

def expansion(node, player):
    if len(node.untried_actions) == 0:
        return node # Terminal Leaf Node
    action = random.choice(node.untried_actions)
    node.untried_actions.remove(action)
    new_node = MCTSNode(apply_action(player, action, copy.deepcopy(node.state)), action, node)
    return new_node


def simulation(node):
    simulated_state = copy.deepcopy(node.state)
    while simulated_state.terminal:
        player = simulated_state.player_turn
        possible_actions = get_actions(player, simulated_state)
        if len(possible_actions) == 0:
            break
        #action = random.choice(possible_actions) # Random choice for now, basic heuristics later
        action = basic_heuristics(possible_actions, simulated_state) # Basic heuristics logic
        simulated_state = apply_action(player, action, simulated_state)
    
    points = end_calculations(simulated_state) + simulated_state.points
    return points # Returns array of all players points

def backprop(leaf_node, reward):
    node = leaf_node
    while node.parent is not None: # Traverses up the tree and stops at root node because node.parent is None
        node.visits += 1
        node.total_reward += reward
        node = node.parent
    
    # Root node
    node.visits += 1
    node.total_reward += reward
    node = node.parent

def turn(starting_state, rollouts):
    player = starting_state.player_turn
    root_node = MCTSNode(starting_state)

    for _ in range(rollouts):
        node = root_node

        # Selection and Expansion
        while len(node.untried_actions) == 0: # Repeats until selection makes it way all the way down the tree
            past_node = node
            node = selection(node)
            if past_node == node:
                break
        expanded_node = expansion(node, player)
        if node == expanded_node: # Terminal Leaf Node
            pass
        else:
            node.children.append(expanded_node)

        # Simulation
        reward = simulation(expanded_node)[player]

        # Backprop
        backprop(leaf_node=expanded_node, reward=reward)
    
    # Pick best actual move
    best = -99999
    best_action = None
    for child in root_node.children:
        if child.total_reward > best:
            best = child.total_reward
            best_action = child.action
    if best_action is None:
        print(root_node.state.discard_pile)
        raise ValueError("No actions above -99999")
    
    return best_action

