from Die import Die
from Game import Game

def main():
    basic_die = Die(1,1,1,3)
    number_of_players = 10
    basic_game = Game(number_of_players, basic_die, 3)
    winners = {}
    number_of_trials=100000
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

    x_axis = []
    y_axis = []
    percentages = []

    for i in range(0, basic_game.number_of_players):
        y_axis.append(winners[str(i)])
        x_axis.append(i+1)
        percentages.append(winners[str(i)]/number_of_trials)

    print(x_axis)
    print(y_axis)
    print(percentages)



if __name__ == '__main__':
    main()