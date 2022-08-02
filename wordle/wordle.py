from tkinter import *
import words
from tkinter import messagebox

def wordle():
    global word,guesscount
    window = Toplevel(screen)
    window.title('Wordle Game')
    window.geometry('280x310')

    black = "#000a01"
    green = "#00b315"
    yellow = "#e0d909"
    grey = "#292724"
    white = "#fafafa"

    window.config(bg=black)
    word = words.get_word()
    guesscount = 1
    print(word)
    wordInput = Entry(window)
    wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

    def get_guess():
        global word, guesscount
        guess = wordInput.get()
        guess = guess.lower()
        guesscount +=1

        if guesscount <= 6 :
            if len(guess) == 5 :
                if word == guess:
                    messagebox.showinfo("Correct!",f"Correct! the word was {word.title()}")
                else:
                    for i,letter in enumerate(guess):
                        label =  Label(window, text=letter.upper())
                        label.grid(row=guesscount,column=i,padx=10,pady=10)

                        if letter == word[i]:
                            label.config(bg=green,fg=black)

                        if letter in word and not letter == word[i]:
                            label.config(bg=yellow,fg=black)

                        if letter not in word:
                            label.config(bg=grey,fg=white)
            else:
                messagebox.showerror("Use 5 letter word", "Please use 5 letter word in your guess!")
        else:
            messagebox.showerror("You lose!",f"You lose! The word was {word}")

    def back():
        window.destroy()
        screen.deiconify()
    
    def info():
        messagebox.showinfo("Intro","Players have six attempts to guess a five-letter word, with feedback given for each guess in the form of colored tiles indicating when letters match or occupy the correct position\n-Green for letter is correct and in the correct position\n-Yellow for the answer but not in the right position\n-Grey for indicates it is not in the answer at all.")
    
    def exit():
        window.destroy()
        screen.destroy()
    
    wordGuessButton = Button(window, text='Guess',command=get_guess)
    wordGuessButton.grid(row=999,column=3,columnspan=1)
    
    info= Button(window, text='Intro',command=info)
    info.place(x=100,y=250)

    back = Button(window, text='< Back',command=back)
    back.place(x=10,y=250)
    
    exit = Button(window, text='Exit',command=exit)
    exit.place(x=180,y=250)

    screen.withdraw()
    window.mainloop()

def home():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Wordle Game")

    lab = Label(screen,text='WELCOME IN WORDLE GAME',font=("Neue Helvetica",15))
    lab.pack(pady=70)

    wordlebtn = Button(screen,text="Play Game",font=('Neue Helvetica',15),command=wordle)
    wordlebtn.pack(pady=10)

    exitbtn = Button(screen,text="Exit",font=('Neue Helvetica',15),command=exit)
    exitbtn.pack(pady=10)

    screen.mainloop()
home()