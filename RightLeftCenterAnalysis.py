from Die import Die
from Game import Game

def run_trials(number_of_players, number_of_trials=5000):
    basic_die = Die(1,1,1,3)
    basic_game = Game(number_of_players, basic_die, 3)
    winners = {}
    for n in range(0, number_of_trials):
        while basic_game.winner is None:
            basic_game.play_turn()
        winner = basic_game.winner
        winner_name = winner.name
        if winner_name in winners.keys():
            winners[winner_name] += 1
        else:
            winners[winner_name] = 1
        basic_game = Game(number_of_players, basic_die, 3)
        if n%1000==0:
            print(n)

    x_axis = []
    y_axis = []
    percentages = []

    for i in range(0, basic_game.number_of_players):
        y_axis.append(winners[str(i)])
        x_axis.append(i+1)
        percentages.append(winners[str(i)]/number_of_trials)

    return names, number_of_wins, percentage_of_wins

def main():
    run_trials(10)

if __name__ == '__main__':
    main()