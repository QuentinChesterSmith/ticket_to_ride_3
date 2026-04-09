import numpy as np
from routes import to_array
from union_find import UnionFind
import random, copy

# Precomputed based off board
routes_array = to_array()
# Rows:
# City1
# City2
# Length
# Color
destination_tickets= np.array([
    # City1
    [27, 1, 1, 23, 23, 18, 12, 12, 14, 14, 11, 16, 5, 5, 5, 26, 26, 28, 3, 3, 4, 24, 24, 2, 2, 25, 0, 0, 13, 13],
    # City2
    [35, 8, 6, 20, 9, 28, 10, 29, 10, 19, 5, 19, 35, 23, 28, 33, 20, 33, 32, 8, 33, 32, 17, 5, 28, 35, 26, 9, 19, 21],
    # Points
    [12, 13, 7, 7, 9, 11, 4, 11, 10, 8, 8, 8, 20, 16, 21, 9, 13, 6, 17, 11, 17, 8, 9, 9, 22, 10, 20, 13, 12, 11]
])

point_table = [0, 1, 2, 4, 7, 10, 15]
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


def shuffle_deck():
    deck = np.array([0]*12 + [1]*12 + [2]*12 + [3]*12 + [4]*12+ [5]*12 + [6]*12 + [7]*12 + [8]*14)
    np.random.shuffle(deck)
    return deck

def reshuffle_deck(discard_pile):
    discard_pile = np.array(discard_pile, dtype=int)
    np.random.shuffle(discard_pile)
    return discard_pile

class GameState():
    def __init__(self, players, real=False, starting_tickets=2, seed=None, deck=None, ticket_deck=None):
        self.real = real
        if seed:
            np.random.seed(seed)
            random.seed(seed)

        self.players = players
        self.player_turn = 0 # Int 0 to (players-1)
        self.cards = np.zeros((self.players, 9)) # 2D Array of cards in everyones hands
        self.tickets = [] # Nested Lists for players destination tickets
        self.cars = np.full(self.players, 45) # 1D Array of players available train cars
        self.routes = np.full(97, -1) # 1D Array of all routes value is claimed status; -1 is none
        self.points = np.zeros(self.players)
        
        self.discard_pile = []
        
        
        self.terminal = True

        # Deck Logic
        if deck is None:
            self.deck = shuffle_deck()
        else:
            self.deck = deck

        if ticket_deck is None:
            self.ticket_deck = list(range(30))
            random.shuffle(self.ticket_deck)
        else:
            self.ticket_deck = ticket_deck

        self.face_up = np.array(self.deck[0:5])

        # Shuffle and distribute destination tickets.
        for player in range(self.players):
            self.tickets.append(self.ticket_deck[:starting_tickets])
            self.ticket_deck = self.ticket_deck[starting_tickets:]

def get_actions(player, state):
    # Routes check
    cars = state.cars[player]
    cards = state.cards[player]
    color_cards = np.array([cards[0]+cards[8], cards[1]+cards[8], cards[2]+cards[8], cards[3]+cards[8], cards[4]+cards[8], cards[5]+cards[8], cards[6]+cards[8], cards[7]+cards[8], cards[np.argmax(cards[:-1])]+cards[8]])

    # Mask for routes
    mask = np.ones(routes_array.shape[1], dtype=bool)
    # Check which routes are unclaimed
    mask &= (state.routes == -1)
    # Check if player has enough cars
    mask &= (routes_array[2]<=cars)
    # Check if player has enough cards
    mask &= (color_cards[routes_array[3]] >= routes_array[2])

    indices = np.where(mask)[0]
    tuple_routes = [(0, int(x)) for x in indices]

    # Draw Cards
    if len(state.deck) >= 7:
        tuple_draws = [(1, x) for x in range(16)]
    else:
        tuple_draws = []
    
    # Draw tickets
    tuple_tickets = []
    if len(state.ticket_deck) > 0:
        tuple_tickets.append((2, 0))

    if len(tuple_routes+tuple_draws+tuple_tickets) == 0:
        state.terminal = False
    return tuple_routes+tuple_draws+tuple_tickets

def apply_action(player, action, state):
    player_hand = state.cards[player, :]
    starting_hand = copy.deepcopy(player_hand)
    if action[0] == 0:
        # Claiming a route
        route = routes_array[:, action[1]]
        
        state.routes[action[1]] = player
        state.cars[player] -= route[2] # Subtract cars
        state.points[player] += point_table[route[2]] # Add points

        if state.cars[player] <= 3:
            # End game
            state.terminal = False

        if route[3] != 8: # If not gray route
            cards_needed = route[2]
            player_hand[route[3]] -= cards_needed # Negative if locomotives are needed
            player_hand[8] += min(player_hand[route[3]], 0) # Subtracts if its negative from previous line
            player_hand[route[3]] = max(player_hand[route[3]], 0)
        else:
            gray_idx = np.argmax(player_hand[:-1])
            cards_needed = route[2]
            player_hand[gray_idx] -= cards_needed # Negative if locomotives are needed
            player_hand[8] += min(player_hand[gray_idx], 0) # Subtracts if its negative from previous line
            player_hand[gray_idx] = max(player_hand[gray_idx], 0)
    
        # Add to discard pile
        hand_diff = starting_hand - player_hand
        append_list = [int(i) for i in range(len(hand_diff)) for _ in range(int(hand_diff[i]))]
        state.discard_pile.extend(append_list)
    elif action[0] == 1:
        # Drawing Cards
        card_indices = draw_order[action[1]]
        drawn_cards = state.deck[card_indices]
        state.deck = np.delete(state.deck, card_indices)

        player_hand[drawn_cards[0]]+=1
        player_hand[drawn_cards[1]]+=1

        if len(state.deck) <= 7:
            state.deck = np.append(state.deck, reshuffle_deck(state.discard_pile))
            state.discard_pile = []

    elif action[0] == 2:
        # Drawing Tickets
        if len(state.ticket_deck) > 0:
            state.tickets[player].append(state.ticket_deck[0])
            state.ticket_deck.pop(0)

    # Turn Logic
    state.player_turn +=1
    if state.player_turn > (state.players-1):
        state.player_turn = 0
    return state

def end_calculations(state):
    # Tickets
    point_change = [0]*state.players
    for player1 in range(state.players):
        find = UnionFind(36)
        for idx, player2 in enumerate(state.routes):
            if player1 == player2:
                route = routes_array[:, idx].copy()
                find.union(route[0], route[1])

        for ticket in state.tickets[player1]:
            if find.connection(destination_tickets[0][ticket], destination_tickets[1][ticket]):
                point_change[player1] += destination_tickets[2][ticket]
            else:
                point_change[player1] -= destination_tickets[2][ticket]
    
    return np.array(point_change)
