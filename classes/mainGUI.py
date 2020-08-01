"""
Program: mainGUI
Author: Jacob Sharpe
Last date modified: 7/31/2020

this program holds all of the GUI portion of the game
"""
import string
import tkinter
from tkinter import font

from classes.game_mechanics import mechanics


def start_new_game_window():
    """ the first screen the player sees it allows them to choose the difficulty or exit
    if they don't want to play
    """
    game = tkinter.Tk()
    game.title("New Game")
    game.geometry("400x450")

    def pressed_button(difficulty):
        """ calls the game to start a new game when the button's be pressed and exits
        this screen
        :param difficulty, the game's difficulty level
        """
        gm.start_new_game(True, difficulty)
        game.destroy()

    titleFont = font.Font(family='Courier', size=30, weight='bold')
    difficulty_font = font.Font(size=11, weight='bold')
    button_font = font.Font(family='Courier',size=10, weight='bold')


    tkinter.Label(game, text="Hangman", height=2, font=titleFont).pack()
    tkinter.Label(game, text="Choose Difficulty", font=difficulty_font).pack()

    tkinter.Button(game, text='Easy', command=lambda: pressed_button("Easy"), width=40, height=3, font=button_font).pack(pady=(10,10))
    tkinter.Button(game, text='Medium', command=lambda: pressed_button("Medium"), width=40, height=3, font=button_font).pack(pady=(10,10))
    tkinter.Button(game, text='Hard', command=lambda: pressed_button("Hard"), width=40, height=3, font=button_font).pack(pady=(10,10))
    tkinter.Button(game, text='Never Mind', command=game.destroy, width=40, height=3, font=button_font).pack(pady=(10, 10))

    game.mainloop()



def main_game_window():
    """ this is where the main game is played
    """
    m = tkinter.Tk()
    m.title("Hangman Game")
    buttons = {}
    photos = [tkinter.PhotoImage(file="images/0left.png"), tkinter.PhotoImage(file="images/1left.png"),
              tkinter.PhotoImage(file="images/2left.png"),
              tkinter.PhotoImage(file="images/3left.png"), tkinter.PhotoImage(file="images/4left.png"),
              tkinter.PhotoImage(file="images/5left.png"),
              tkinter.PhotoImage(file="images/6left.png"), tkinter.PhotoImage(file="images/7left.png"),
              tkinter.PhotoImage(file="images/8left.png"),
              tkinter.PhotoImage(file="images/9left.png"), tkinter.PhotoImage(file="images/10left.png")]



    wins_Label = tkinter.Label(m)
    wins_Label.grid(row=0, column=0, columnspan=2)
    Losses_Label = tkinter.Label(m)
    Losses_Label.grid(row=0, column=7, columnspan=2)

    imgLabel = tkinter.Label(m)
    imgLabel.grid(row=1, column=0, columnspan=3)
    current_word = tkinter.StringVar()
    tkinter.Label(m, textvariable=current_word, font=("Helvetica 28 bold")).grid(row=1, column=4, columnspan=6)

    win_lose_label =tkinter.Label(m, height=2, font=("Courier 30 bold"))
    win_lose_label.grid(row=2, column=0, columnspan=9)


    def beginning_of_new_game():
        """ configures some of the display text and visual for the start of the game
        """
        wins_Label.configure(text="Wins: " + str(gm.return_wins()), font=("Courier 15 bold"), height=3)
        Losses_Label.configure(text="Losses: " + str(gm.return_losses()), font=("Courier 15 bold"), height=3)

        imgLabel.configure(image=photos[gm.get_tries()])
        current_word.set(gm.display_game_word_results())

        win_lose_label.configure(text=" ")

        for x in buttons:
            buttons[x][0].configure(state=tkinter.NORMAL)


    buttonRow = 27
    buttonColumn=0
    for x in string.ascii_uppercase:
       buttons[x] = [tkinter.Button(m, text=x, command=lambda letter=x: button_click(letter), width=11, height=3)]
       buttons[x][0].grid(row=buttonRow // 9, column=buttonColumn % 9)
       buttonRow += 1
       buttonColumn += 1


    def button_click(button_letter):
        """ accesses the guess option in the game mechanics and updates the
        game if the letter guessed is right or wrong
        depending on the difficulty it also disables the button choosen
        it also deterines if the game has been won or lost and calls the
        next function if it has been won or lost
        :param button_letter, the letter choosen
        """
        difficulty = gm.get_game_difficulty()
        if difficulty != "Hard":
            buttons[button_letter][0].configure(state=tkinter.DISABLED)
        gm.guess(button_letter)
        imgLabel.configure(image=photos[gm.get_tries()])
        current_word.set(gm.display_game_word_results())
        if gm.return_win_or_lose() == "Win" or gm.return_win_or_lose() == "Lose":
            result = gm.return_win_or_lose()
            win_or_lose(result)


    def win_or_lose(result):
        """ this disables all the buttons except for the new game button and displays a win or lose
        message to the user as well as the full word if the game has been lost
        :param result, the result of win or lose
        """
        wins_Label.configure(text="Wins: " + str(gm.return_wins()))
        Losses_Label.configure(text="Losses: " + str(gm.return_losses()))
        for x in buttons:
            buttons[x][0].configure(state=tkinter.DISABLED)
        if result == "Win":
            win_lose_label.configure(fg="Green", text="CONGLATURATION!!! YOU'RE WINNER!")
        elif result == "Lose":
            current_word.set(gm.display_game_word_loss_results())
            if gm.game_difficulty == "Easy":
                win_lose_label.configure(fg="Red", text="Wow you actually lost...On Easy!")
            else:
                win_lose_label.configure(fg="Red", text="GAME OVER!! YOU LOSE")




    def new_game_button():
        """ pulls up a new menu which allows the player to choose a new game and its difficulty
        """
        new_game_menu = tkinter.Tk()
        new_game_menu.title("New Game")
        new_game_menu.geometry("400x450")

        def game_set_up(difficulty):
            """ if a new game is choosen this sets up a new game
            :param difficulty the difficulty of the game
            """
            gm.start_new_game(True, difficulty)
            beginning_of_new_game()
            new_game_menu.destroy()

        titleFont = font.Font(family='Courier', size=30, weight='bold')
        difficulty_font = font.Font(size=11, weight='bold')
        button_font = font.Font(family='Courier', size=10, weight='bold')
        tkinter.Label(new_game_menu, text="NEW GAME", height=2, font=titleFont).pack()
        tkinter.Label(new_game_menu, text="Choose Difficulty", font=difficulty_font).pack()

        tkinter.Button(new_game_menu, text='Easy', command=lambda: game_set_up("Easy"), width=40, height=3,font=button_font).pack(pady=(10, 10))
        tkinter.Button(new_game_menu, text='Medium', command=lambda: game_set_up("Medium"), width=40, height=3,font=button_font).pack(pady=(10, 10))
        tkinter.Button(new_game_menu, text='Hard', command=lambda: game_set_up("Hard"), width=40, height=3, font=button_font).pack(pady=(10, 10))
        tkinter.Button(new_game_menu, text='I Changed My Mind', command=new_game_menu.destroy, width=40, height=3, font=button_font).pack(pady=(10, 10))
        new_game_menu.mainloop()


    new_game_button = tkinter.Button(m, text="New Game", command=new_game_button, width=11, height=3)
    new_game_button.grid(row=buttonRow // 9, column=buttonColumn % 9)



    beginning_of_new_game()
    m.mainloop()





if __name__ == '__main__':
    gm = mechanics()

    start_new_game_window()

    running = gm.get_game_started()
    if running:
        main_game_window()
