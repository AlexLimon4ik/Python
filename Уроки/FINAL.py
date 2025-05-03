from random import *

class Player():
    def __init__(self, player_character):
        self.player_character = player_character
        
class Bot():
    def __init__(self, bot_character):
        self.bot_character = bot_character

class Tabel():
    def __init__(self):
        self.board = [" "] * 9

    def print_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("—" * 11)
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("—" * 11)
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("")

class Game():
    def __init__(self):
        print("Гра почалася:")

        self.game_tabel = Tabel()
        
        self.game_tabel.print_board()

        x_or_o = randint(0, 2)

        if x_or_o == 1:
            self.player = Player("X")
            self.bot = Bot("O")  
        else:
            self.player = Player("O")
            self.bot = Bot("X")  

        print(f"Ти: {self.player.player_character}")
        print(f"Бот: {self.bot.bot_character}")

    def is_draw(self):
        return " " not in self.game_tabel.board

    def check_win(self, character):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]            
        ]

        for combo in winning_combinations:
            if (self.game_tabel.board[combo[0]] == character and
                self.game_tabel.board[combo[1]] == character and
                self.game_tabel.board[combo[2]] == character):
                return True
        return False


    def player_choice_func(self):
        while True:
            try:
                choice = int(input("Виберіть клітинку (1-9): ")) - 1
                if 0 <= choice <= 8 and self.game_tabel.board[choice] == " ":
                    self.game_tabel.board[choice] = self.player.player_character
                    break
                else:
                    print("Некоректний вибір або клітинка зайнята! Спробуйте знову.")
            except ValueError:
                print("Введіть число від 1 до 9!")


        if self.check_win(self.player.player_character):
            self.game_tabel.print_board()
            print("Ти переміг!")
            return True
        return False


    def bot_choice_func(self):
        while True:
            bot_choice = randint(0, 8)
            if self.game_tabel.board[bot_choice] == " ":
                self.game_tabel.board[bot_choice] = self.bot.bot_character
                break

        self.game_tabel.print_board()

        if self.check_win(self.bot.bot_character):

            print("Бот переміг!")
            return True
        return False

    def play_game(self):
        while True:
            if self.player_choice_func():
                break
            if self.is_draw():
                self.game_tabel.print_board()
                print("Гра закінчилася нічиєю!")
                break
            if self.bot_choice_func():
                break
            if self.is_draw():
                self.game_tabel.print_board()
                print("Гра закінчилася нічиєю!")
                break


game = Game()

game.play_game()
