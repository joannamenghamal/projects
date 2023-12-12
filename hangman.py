#! usr/bin/env python3
import json
import random
import tkinter as tk
from typing import List, Any


class HangMan:
    # guessed: list[Any]

    def __init__(self):
        self.root = tk.Tk()  # set up window
        self.root.geometry("1000x540")
        self.root.title("HANGMAN GAME")
        self.root.configure(background="Pink")

        # creates label (static text) and use pack to display it
        self.info_label = tk.Label(self.root, text="Guess a letter!", background="Pink", font=('Helvetica', 20))
        self.info_label.pack(padx=0, pady=10)

        self.my_entry = tk.Entry(self.root, font=('Helvetica', 14))
        self.my_entry.pack(padx=20, pady=20)
        # creates button
        self.my_button1 = tk.Button(self.root, text="Enter", font=("Helvetica", 16), fg='blue',
                                    highlightbackground='pink', command=self.play)
        self.my_button1.pack()
        # Created a button to exit
        self.my_button2 = tk.Button(self.root, text="Exit", font=("Helvetica", 16), fg='blue',
                                    highlightbackground='pink', command=exit)
        self.my_button2.pack()
        # Creates a button to exit. When pressed, it will call the program again
        self.my_button3 = tk.Button(self.root, text="New Game?",
                                    fg='blue', highlightbackground='pink', command=self.restart)
        self.my_button3.pack(padx=20, pady=20)
        self.label_frame1 = tk.Label(self.root, text="Guessed Letters:", bg='pink',
                                     font=("Helvetica", 14), padx=10, pady=10)
        self.label_frame1.pack()

        # set up the game
        self.my_word = self.getword()  # get the random word. It is now called self.my_word

        self.guessed = []  # will contain list of letters guessed
        self.my_entry.focus()  # set the cursor to entry box
        self.output = tk.Label(self.root, text="", bg='Pink', fg='red', font=("Helvetica", 16))
        self.output.pack()
        # will contain the list of guessed letters in textbox
        self.guessed_text = tk.Text(self.root, height=1, width=10, bg='white', fg='Purple')
        self.guessed_text.pack()
        # FIve letter word dashes
        self.word_with_blanks = "_" * len(self.my_word)
        self.word_label = tk.Label(self.root, text=self.word_with_blanks, font=("Helvetica", 50), bg='Teal')
        self.word_label.pack(padx=20, pady=20)
        self.root.mainloop()  # display window

    # gets random word from json file
    def getword(self):
        my_file = open("/Users/Joanna/Downloads/list_of_words.json")
        my_read = my_file.read()
        json_loading = json.loads(my_read)
        chosen_word = []

        for item in json_loading:
            chosen_word.append(item["word"])

        random_word = random.choice(chosen_word)
        print(f"Your chosen word is: {random_word}")
        return random_word

    def game_over(self, result):
        word = self.my_word
        if result == "Win":
            result_text = "Great! You won!"
        else:
            result_text = "Sorry, you lost... The word was " + word
        # opens a window upon winning
        self.popup = tk.Toplevel()
        self.popup.title("")
        self.popup.geometry("160x100")
        self.label = tk.Label(self.popup, text=result_text)
        self.label.pack()

        self.popup.mainloop()

    def play(self):
        word = self.my_word     # local variable of self.my_word
        letter = self.my_entry.get()    # get the user input
        self.my_entry.delete(0, "end")
        if letter != "":
            letter = letter[0]  # take the first character if the player enters multiple
            if letter in word:  # if letter in word - use for loop to find position
                for i in range(len(word)):
                    if word[i] == letter:
                        self.word_with_blanks = self.word_with_blanks[:i] + letter + self.word_with_blanks[i+1:]
                self.word_label.config(text=self.word_with_blanks)
                if '_' not in self.word_with_blanks:
                    self.game_over("Win")
            # if the letter is already in guessed list
            if letter in self.guessed:
                self.output.config(text="You already guessed that letter!")
                "-".join(self.guessed)

            elif letter in self.my_word:
                self.output.config(text="You guessed a letter!")
                self.guessed.append(letter)
            else:
                self.output.config(text="")
                self.guessed.append(letter)
                self.guessed_text.insert(tk.INSERT, letter)
                " ".join(self.guessed)

        print(letter)
        print(self.my_word)
        print(self.guessed)

    def restart(self):
        self.root.destroy()
        HangMan()


HangMan()
