from environment import GameState, apply_action, end_calculations
from mcts import turn
import numpy as np
import copy, time


def game(players, rollouts, starting_tickets=2, deck=None, ticket_deck=None, seed=None):
    real_game_state = GameState(players, True, starting_tickets, seed, deck, ticket_deck)
    
    turn_count = 0
    while real_game_state.terminal:
        player = real_game_state.player_turn
        fake = copy.deepcopy(real_game_state)
        fake.real = False
        action = turn(fake, rollouts)
        real_game_state = apply_action(player, action, real_game_state)

        turn_count += 1
    
    return end_calculations(real_game_state)+real_game_state.points, turn_count

def gather_data(games, players, rollouts):
    winners = np.zeros(players)
    players_points = np.zeros((players, games))

    total_turns = 0

    start_time = time.time()
    for game_idx in range(games):
        print(game_idx)
        game_points, turn_count = game(players, rollouts)
        total_turns += turn_count
        for player_idx in range(players):
            players_points[player_idx][game_idx] = game_points[player_idx]

        winners[game_points.argmax()] +=1

    # Print Out Data
    avg_time = round((time.time()-start_time)/games, 4)
    means = np.mean(players_points, axis=1)
    std = np.round(np.std(players_points, axis=1), 4)
    winner_prop = np.round(winners/games, 4)
    avg_turns = total_turns/games

    print(f"Games: {games}")
    print(f"Rollouts: {rollouts}")
    print(f"Mean Points per Player: {means}")
    print(f"Standard Deviation of Points per Player: {std}")
    print(f"Win Proportion: {winner_prop}")
    print(f"Average Turns per Game: {avg_turns}")
    print(f"Average Time per Game: {avg_time}")

def main():
    #print(game(4, 1, seed=42))
    gather_data(games=100, players=4, rollouts=100)

if __name__ == "__main__":
    main()