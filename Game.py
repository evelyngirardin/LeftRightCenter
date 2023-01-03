from tkinter import CURRENT
from Player import Player
from random import choices
from Die import Die

class Game:
    def __init__(self, number_of_players, die, starting_money):
        self.die = die
        self.total_turns = 0
        self.total_rolls = 0
        self.total_money = starting_money*number_of_players
        self.winner = None
        self.number_of_players = number_of_players
        self.current_players = number_of_players
        self.current_turn = 0
        self.turn_order = []

        for i in range(0, number_of_players):
            player = Player(starting_money, str(i))
            self.turn_order.append(player)

        for i in range(0, number_of_players):
            right_player = self.turn_order[(i-1)%number_of_players]
            left_player = self.turn_order[(i+1)%number_of_players]
            self.turn_order[i].set_neighbors(right_player, left_player)

    def play_turn(self):
        """ rolls a die per dollar up to 3, deals with the result, and checks if there is a winner. """
        current_player = self.turn_order[self.current_turn]

        if current_player.money !=0:
            probabilities = self.die.get_all_probabilities()
            left_player = current_player.left_player
            right_player = current_player.right_player

            if current_player.money <= 3:
                rolls = choices(list(probabilities.keys()), weights=list(probabilities.values()), k=current_player.money)
            else:
                rolls = choices(list(probabilities.keys()), weights=list(probabilities.values()), k=3)
            
            current_player.number_of_rolls += len(rolls)
            self.total_rolls += len(rolls)

            for roll in rolls:
                if roll == "L":
                    if left_player.money == 0:
                        self.current_players+=1
                    left_player.money += 1
                    current_player.money -= 1
                elif roll == "R":
                    if right_player.money == 0:
                        self.current_players+=1
                    right_player.money += 1
                    current_player.money -= 1
                elif roll == "C":
                    current_player.money -= 1
                    self.total_money -= 1

            if current_player.money == 0:
                self.current_players-=1

        
        self.total_turns += 1
        self.current_turn = self.total_turns%self.number_of_players

       
        if self.current_players == 1:
            for player in self.turn_order:
                if player.money != 0:
                    self.winner = player
                    break