from Tkinter import *
import random
heading = ('Courier', 18)
normal = ('Courier', 13)
guesses = 3

root = Tk()


class Answer:
    def __init__(self, val, loc_input, loc_display):
        self.val = val
        self.loc_input = loc_input
        self.loc_display = loc_display

    def compare_answer(self, guess=False):
        if self.val == self.loc_input.get().upper():
            self.loc_display['text'] = 'You got the answer right!'
            self.loc_display['bg'] = 'green'
            return True
        else:
            if not guess:
                self.loc_display['text'] = 'The correct answer was: %s' % self.val
            else:
                self.loc_display['text'] = 'This answer is wrong.'
            self.loc_display['bg'] = 'red'
            self.loc_display['fg'] = 'white'
            return False


def shift(current, new):
    current.grid_remove()
    new.grid()


def rand_words(words):
    first = random.choice(words)
    while True:
        second = random.choice(words)
        if second != first:
            return first, second


def rand_list(word_list, to_remove):
    new_list = list(word_list)
    new_list.remove(to_remove)
    random.shuffle(new_list)
    return new_list


def display(location, sec):
    location['text'] = "%ds left" % sec
    if not sec:
        shift(memorise, answer)
        return
    root.after(1000, display, location, sec - 1)


def add(fill, text):
    fill.delete(0, END)
    fill.insert(END, text)


def submit(sub_button, first, second):
    global guesses
    guesses -= 1
    first.compare_answer(guesses)
    second.compare_answer(guesses)
    if not guesses or first.compare_answer(guesses) and second.compare_answer(guesses):
        sub_button.grid_remove()
        guesses = 3


def reset():
    shift(answer, start)
    for widget in memorise.winfo_children():
        widget.destroy()
    for widget in answer.winfo_children():
        widget.destroy()


def game_loop(num, sec):
    numxnum = "{0}x{0}".format(num)
    file_address = open("%s.txt" % numxnum, 'r')
    words = file_address.read().splitlines()
    file_address.close()
    first_word, second_word = rand_words(words)
    first_list = rand_list(words, second_word)
    second_list = rand_list(words, first_word)

    shift(start, memorise)
    Label(memorise, text=numxnum, font=heading).grid(row=0, column=0, columnspan=num, padx=80, pady=10)
    for i in range(num ** 2):
        Label(memorise, text=first_list[i], font=normal).grid(row=i / num + 1, column=i % num, padx=10, pady=5)
    time_left = Label(memorise, font=normal)
    time_left.grid(row=num + 2, column=0, columnspan=num, pady=10)
    display(time_left, sec)

    # shifted to answer frame
    Label(answer, text=numxnum, font=heading).grid(row=0, column=0, columnspan=num, padx=80, pady=10)
    for i in range(num ** 2):
        Button(answer, text=second_list[i], font=normal, command=lambda i=i: add(in_second, second_list[i])).grid(row=i / num + 1, column=i % num, padx=10, pady=5)
    Label(answer, text="Word now here:", font=normal).grid(row=num + 2, column=0, columnspan=num - 1, padx=10, sticky=W)
    in_second = Entry(answer, font=normal, bg="pale goldenrod", width=8)
    in_second.grid(row=num + 2, column=num - 1, padx=10, pady=5)
    second_right = Label(answer, font=normal, bg="dodgerblue", width=num*10)
    second_right.grid(row=num + 3, column=0, columnspan=num, padx=10)
    second = Answer(second_word, in_second, second_right)

    Label(answer, text="Word not present:", font=normal).grid(row=num + 4, column=0, columnspan=num - 1, padx=10, sticky=W)
    in_first = Entry(answer, font=normal, bg="pale goldenrod", width=8)
    in_first.grid(row=num + 4, column=num - 1, padx=10, pady=5)
    first_right = Label(answer, font=normal, bg="dodgerblue", width=num*10)
    first_right.grid(row=num + 5, column=0, columnspan=num, padx=10)
    first = Answer(first_word, in_first, first_right)

    sub_button = Button(answer, text="Submit", font=normal, command=lambda: submit(sub_button, second, first))
    sub_button.grid(row=num + 6, column=0, pady=5)
    Button(answer, text="Return", font=normal, command=reset).grid(row=num + 6, column=num-1, pady=10)


memorise = Frame(root)
answer = Frame(root)

instruct = Frame(root)

start = Frame(root)
start.grid()
Label(start, text="Memory Game", font=heading).grid(row=0, column=0, padx=50, pady=10)
Button(start, text="3x3", font=normal, width=12, command=lambda: game_loop(3, 30)).grid(row=1, column=0, pady=5)
Button(start, text="4x4", font=normal, width=12, command=lambda: game_loop(4, 45)).grid(row=2, column=0, pady=5)
Button(start, text="How to use", font=normal, width=12, command=lambda: shift(start, instruct)).grid(row=3, column=0, pady=5)

root.mainloop()