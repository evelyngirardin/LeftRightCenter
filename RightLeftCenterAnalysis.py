from Die import Die
from Game import Game
import matplotlib.pyplot as plt 

def run_trials(number_of_players, number_of_trials=5001):
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
            print(str(int(n/number_of_trials*100)) + "%")

    x_axis = []
    y_axis = []
    percentages = []

    for i in range(0, basic_game.number_of_players):
        y_axis.append(winners[str(i)])
        x_axis.append(i+1)
        percentages.append(winners[str(i)]/number_of_trials)

    return x_axis, y_axis, percentages

def plots(names, number_of_wins, percentage_of_wins, number_of_players):

    fig, ax = plt.subplots()

    ax.bar(names, percentage_of_wins, width=1, edgecolor="white", linewidth=0.7)

    plt.title("Percentage of wins")

    fig1, ax1 = plt.subplots()

    difference_from_average = percentage_of_wins.copy()

    for item in range(0, len(difference_from_average)):
        difference_from_average[item] -= 1/number_of_players

    ax1.bar(names, difference_from_average, width=1, edgecolor='white', linewidth=0.7)

    plt.title("Difference between expected and actual percentage of wins")

    plt.show()


def main():
    # Set up
    number_of_players = 8
    number_of_trials = 50000

    names, number_of_wins, percentage_of_wins = run_trials(number_of_players, number_of_trials)
    plots(names, number_of_wins, percentage_of_wins, number_of_players)


if __name__ == '__main__':
    main()