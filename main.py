import tkinter as tk
from tkinter import messagebox
import tkmacosx as tmac
from tkinter import ttk
from quiz_brain import QuizBrain
from questionbank import QuestionBank
from question import Question
import random
import time

BACKGROUND_COLOR = '#A3A499'
ACTIVE_BACKGROUND_COLOR = '#A3A499'
DISABLED_BACKGROUND_COLOR = '#304641'
FONT_COLOR = '#2A0E0A'
ACTIVE_DROPDOWN_FONT_COLOR = '#271C1F'
CLICK_HERE_COLOR = '#912E1F'

TITLE_FONT_NAME = 'American Typewriter'
LABEL_FONT_NAME = 'American Typewriter'
CANVAS_TEXT_FONT_NAME = 'American Typewriter'

TITLE_FONT_SIZE = 48
LABEL_FONT_SIZE = 24
DROPDOWN_FONT_SIZE = 16
CANVAS_TEXT_FONT_SIZE_MIN = 18
CANVAS_TEXT_FONT_SIZE_MEDIUM = 20
CANVAS_TEXT_FONT_SIZE_MAX = 24
DROPDOWN_LIST_FONT_SIZE = 10
CLICK_HERE_SIZE = 20

MAX_QUESTION_NUMBER = 12

quiz_canvas_image = ''
quiz_number = ''
quiz_question = ''
quiz_answer = ''
quiz_correct_answer = ''
quiz_click_here = ''

layout = 0
is_checked = 0

score = 0
high_score = 0


# ------------------------- Window Orientation Switcher ------------------------- #


def remove_all():
    title_label.grid_forget()
    quiz_canvas.delete('all')
    quiz_canvas.grid_forget()
    score_label.grid_forget()
    high_score_label.grid_forget()
    category_label.grid_forget()
    category_drop.grid_forget()
    difficulty_label.grid_forget()
    difficulty_drop.grid_forget()
    portrait_btn.grid_forget()
    landscape_btn.grid_forget()
    exit_btn.grid_forget()
    yes_btn.grid_forget()
    no_btn.grid_forget()
    A_btn.grid_forget()
    B_btn.grid_forget()
    C_btn.grid_forget()
    D_btn.grid_forget()


def set_font_size():
    if len(question_text) > 70:
        quiz_canvas.itemconfig(quiz_question, font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MEDIUM, 'bold'))
    elif len(question_text) > 200:
        quiz_answer.itemconfig(quiz_question, font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MIN, 'bold'))


def set_horizontal():
    global quiz_canvas_image, quiz_number, quiz_question, quiz_answer, quiz_correct_answer, layout, quiz_click_here
    if layout == 0:
        quiz_canvas.coords(quiz_correct_answer, 400, 100)
        quiz_canvas.coords(quiz_question, 400, 250)
        quiz_canvas.coords(quiz_correct_answer, 380, 400)
        quiz_canvas.coords(quiz_click_here, 550, 450)
        layout = 1

    remove_all()
    set_font_size()

    title_label.grid(row=0, column=0, columnspan=6)

    quiz_canvas_image = quiz_canvas.create_image(400, 263, image=quiz_canvas_background_image_h)

    quiz_number = quiz_canvas.create_text(400, 100,
                                          text=f"{quiz.get_current_question_number() + 1}/{quiz.get_total_question_number()}",
                                          font=(LABEL_FONT_NAME, LABEL_FONT_SIZE, ''), fill=FONT_COLOR, justify="left")
    quiz_question = quiz_canvas.create_text(400, 250, text=f"Question: {question_text}",
                                            font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MAX, 'bold'),
                                            fill=FONT_COLOR, justify="left", width=640)
    quiz_correct_answer = quiz_canvas.create_text(400, 450, text=f"",
                                                  font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MAX, ''),
                                                  fill=FONT_COLOR, justify="left", width=640)
    quiz_click_here = quiz_canvas.create_text(400, 550, text=f"",
                                              font=(LABEL_FONT_NAME, CLICK_HERE_SIZE, 'bold'),
                                              fill=CLICK_HERE_COLOR, justify="left", width=640)

    quiz_canvas.config(width=800, height=526)
    quiz_canvas.grid(row=1, rowspan=8, column=0, columnspan=4)

    score_label.grid(row=1, column=4, columnspan=2, sticky='NW')
    high_score_label.grid(row=2, column=4, columnspan=2, sticky='NW')

    category_label.grid(row=3, column=4, columnspan=2, sticky='NW')
    category_drop.grid(row=4, column=4, columnspan=2, sticky='NW')

    difficulty_label.grid(row=5, column=4, columnspan=2, sticky='NW')
    difficulty_drop.grid(row=6, column=4, columnspan=2, sticky='NW')

    portrait_btn.grid(row=7, column=4, sticky='SE')
    landscape_btn.grid(row=7, column=5, sticky='SW')

    exit_btn.grid(row=8, column=5, columnspan=2, sticky='SW')

    if is_checked == 0:
        if current_question_type == 'boolean':
            yes_btn.grid(row=9, column=1, sticky='NE')
            no_btn.grid(row=9, column=2, sticky='NW')
        elif current_question_type == 'multiple':
            A_btn.grid(row=9, column=0)
            B_btn.grid(row=9, column=1)
            C_btn.grid(row=9, column=2)
            D_btn.grid(row=9, column=3)


def set_vertical():
    global quiz_canvas_image, quiz_number, quiz_question, quiz_answer, quiz_correct_answer, layout, quiz_click_here
    if layout == 1:
        quiz_canvas.coords(quiz_correct_answer, 300, 100)
        quiz_canvas.coords(quiz_question, 300, 300)
        quiz_canvas.coords(quiz_correct_answer, 400, 500)
        quiz_canvas.coords(quiz_click_here, 400, 550)
        layout = 0

    remove_all()
    set_font_size()

    exit_btn.grid(row=0, column=0, sticky='SW')

    portrait_btn.grid(row=0, column=3, sticky='SE')
    landscape_btn.grid(row=0, column=4, sticky='SE')

    title_label.config(width=9)
    title_label.grid(row=0, column=0, columnspan=5)

    category_label.grid(row=2, column=0, columnspan=2, sticky='NW')
    category_drop.grid(row=3, column=0, columnspan=2, sticky='NW')

    difficulty_label.grid(row=4, column=0, columnspan=2, sticky='NW')
    difficulty_drop.grid(row=5, column=0, columnspan=2, sticky='NW')

    score_label.grid(row=2, column=3, sticky='NE')
    high_score_label.grid(row=4, column=3, sticky='NE')

    quiz_canvas_image = quiz_canvas.create_image(300, 350, imag=quiz_canvas_background_image_v)

    quiz_number = quiz_canvas.create_text(300, 100,
                                          text=f"{quiz.get_current_question_number() + 1}/{quiz.get_total_question_number()}",
                                          font=(LABEL_FONT_NAME, LABEL_FONT_SIZE, ''),
                                          fill=FONT_COLOR, justify="left")

    quiz_question = quiz_canvas.create_text(300, 300, text=f"Question: {question_text}",
                                            font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MAX, 'bold'),
                                            fill=FONT_COLOR, justify="left", width=450)

    quiz_correct_answer = quiz_canvas.create_text(300, 500, text=f"",
                                                  font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MAX, ''),
                                                  fill=FONT_COLOR, justify="left", width=450)
    quiz_click_here = quiz_canvas.create_text(400, 550, text=f"",
                                              font=(LABEL_FONT_NAME, CLICK_HERE_SIZE, 'bold'),
                                              fill=CLICK_HERE_COLOR, justify="left", width=640)

    quiz_canvas.config(width=600, height=700)
    quiz_canvas.grid(row=6, column=0, columnspan=5)

    if is_checked == 0:
        if current_question_type == 'boolean':
            yes_btn.grid(row=7, column=1, sticky='NE')
            no_btn.grid(row=7, column=2, sticky='NW')
        elif current_question_type == 'multiple':
            A_btn.grid(row=7, column=0, sticky='E')
            B_btn.grid(row=7, column=1)
            C_btn.grid(row=7, column=2)
            D_btn.grid(row=7, column=3, sticky='E')


# ------------------------- GUI Elements ------------------------- #

root = tk.Tk()
root.title("Family Quizzler")
root.configure(bg=BACKGROUND_COLOR, padx=20, pady=20)
# style = ttk.Style(root)
# style.theme_use('classic')

title_label = tk.Label(text='Quizzler     ', bg=BACKGROUND_COLOR, fg=FONT_COLOR,
                       font=(TITLE_FONT_NAME, TITLE_FONT_SIZE, ''))

quiz_canvas = tk.Canvas(bg=BACKGROUND_COLOR, highlightthickness=0)
quiz_canvas_background_image_v = tk.PhotoImage(file='img/bg_vertical.png')
quiz_canvas_background_image_h = tk.PhotoImage(file='img/bg_horizontal.png')

score_label = tk.Label(text=f'Score: {score}', bg=BACKGROUND_COLOR, fg=FONT_COLOR,
                       font=(LABEL_FONT_NAME, LABEL_FONT_SIZE, ''), padx=0, pady=5)
high_score_label = tk.Label(text=f'High score: {high_score}', bg=BACKGROUND_COLOR, fg=FONT_COLOR,
                            font=(LABEL_FONT_NAME, LABEL_FONT_SIZE, ''), padx=0, pady=5)

category_label = tk.Label(text='Category: ', bg=BACKGROUND_COLOR, fg=FONT_COLOR,
                          font=(LABEL_FONT_NAME, LABEL_FONT_SIZE, ''), padx=0, pady=5)

category_selected = tk.StringVar()
category_selected.set('Choose one from the list above')
category_options = ['General Knowledge',
                    'Entertainment: Books',
                    'Entertainment: Film',
                    'Entertainment: Video Games',
                    'Science & Nature',
                    'Science: Computers',
                    'Mythology',
                    'Geography',
                    'History',
                    'Sports',
                    'Animals',
                    'Politics',
                    'Entertainment: Japanese Anime & Manga',
                    'Entertainment: Cartoon & Animation',
                    ]

category_drop = tk.OptionMenu(root, category_selected, *category_options)
category_drop.config(background=BACKGROUND_COLOR, borderwidth=0, foreground=FONT_COLOR,
                     activeforeground=ACTIVE_DROPDOWN_FONT_COLOR,
                     font=(LABEL_FONT_NAME, DROPDOWN_FONT_SIZE, ''), width=22, justify='left')

difficulty_label = tk.Label(text='Difficulty', bg=BACKGROUND_COLOR, fg=FONT_COLOR,
                            font=(LABEL_FONT_NAME, LABEL_FONT_SIZE, ''), padx=0, pady=5)


def option_changed(*args):
    if category_selected.get() in category_options and difficulty_selected.get() in difficulty_options:
        set_up_quiz()


difficulty_selected = tk.StringVar()
difficulty_selected.set('Choose from the list above')
difficulty_selected.trace('w', option_changed)
difficulty_options = ['easy', 'medium', 'hard']
difficulty_drop = tk.OptionMenu(root, difficulty_selected, 'Choose from the list above', *difficulty_options)
difficulty_drop.config(background=BACKGROUND_COLOR, borderwidth=0, foreground=FONT_COLOR,
                       activeforeground=ACTIVE_DROPDOWN_FONT_COLOR,
                       font=(LABEL_FONT_NAME, DROPDOWN_FONT_SIZE, ''), width=22, justify='left')

portrait_image = tk.PhotoImage(file="img/portrait.png")
portrait_btn = tmac.Button(image=portrait_image, command=set_vertical, background=BACKGROUND_COLOR,
                           activebackground=ACTIVE_BACKGROUND_COLOR, borderless=1, focuscolor='',
                           width=75, height=98)
landscape_image = tk.PhotoImage(file="img/landscape.png")
landscape_btn = tmac.Button(image=landscape_image, command=set_horizontal, background=BACKGROUND_COLOR,
                            activebackground=ACTIVE_BACKGROUND_COLOR, borderless=1, focuscolor='',
                            width=98, height=75)


def exit_app():
    root.destroy()


exit_image = tk.PhotoImage(file="img/exit 2.png")
exit_btn = tmac.Button(image=exit_image, command=exit_app, background=BACKGROUND_COLOR,
                       activebackground=ACTIVE_BACKGROUND_COLOR, borderless=1, focuscolor='',
                       width=130, height=100)


def check_ok():
    global score
    if correct_answer:
        score += 1
    feedback_from_answer()


ok_image = tk.PhotoImage(file="img/hit.png")
yes_btn = tmac.Button(image=ok_image, command=check_ok, background=BACKGROUND_COLOR,
                      activebackground=ACTIVE_BACKGROUND_COLOR, disabledforeground=DISABLED_BACKGROUND_COLOR,
                      borderless=1, focuscolor='', width=130, height=100)


def check_no():
    global score
    if not correct_answer:
        score += 1
    feedback_from_answer()


no_image = tk.PhotoImage(file="img/miss.png")
no_btn = tmac.Button(image=no_image, command=check_no, background=BACKGROUND_COLOR,
                     activebackground=ACTIVE_BACKGROUND_COLOR, disabledforeground=DISABLED_BACKGROUND_COLOR,
                     borderless=1, focuscolor='', width=130, height=100)


def check_A():
    global score
    if correct_answer == all_answer[0]:
        score += 1
    feedback_from_answer()


A_image = tk.PhotoImage(file="img/letter_A.png")
A_btn = tmac.Button(image=A_image, command=check_A, background=BACKGROUND_COLOR,
                    activebackground=ACTIVE_BACKGROUND_COLOR, disabledforeground=DISABLED_BACKGROUND_COLOR,
                    borderless=1, focuscolor='', width=130, height=100)


def check_B():
    global score
    if correct_answer == all_answer[1]:
        score += 1
    feedback_from_answer()


B_image = tk.PhotoImage(file="img/letter_B.png")
B_btn = tmac.Button(image=B_image, command=check_B, background=BACKGROUND_COLOR,
                    activebackground=ACTIVE_BACKGROUND_COLOR, disabledforeground=DISABLED_BACKGROUND_COLOR,
                    borderless=1, focuscolor='', width=130, height=100)


def check_C():
    global score
    if correct_answer == all_answer[2]:
        score += 1
    feedback_from_answer()


C_image = tk.PhotoImage(file="img/letter_C.png")
C_btn = tmac.Button(image=C_image, command=check_C, background=BACKGROUND_COLOR,
                    activebackground=ACTIVE_BACKGROUND_COLOR, disabledforeground=DISABLED_BACKGROUND_COLOR,
                    borderless=1, focuscolor='', width=130, height=100)


def check_D():
    global score
    if correct_answer == all_answer[3]:
        score += 1
    feedback_from_answer()


D_image = tk.PhotoImage(file="img/letter_D.png")
D_btn = tmac.Button(image=D_image, command=check_D, background=BACKGROUND_COLOR,
                    activebackground=ACTIVE_BACKGROUND_COLOR, disabledforeground=DISABLED_BACKGROUND_COLOR,
                    borderless=1, focuscolor='', width=130, height=100)

# ------------------------- Calculations ------------------------- #

question_bank = QuestionBank()
quiz = QuizBrain(question_bank.new_question_bank())

total_nr_of_questions = MAX_QUESTION_NUMBER
current_question_nr = 0

question_text = 'Chose a category to play'
correct_answer = ''

current_question_type = ''
all_answer = []

category_drop.config(state='normal')
difficulty_drop.config(state='normal')

yes_btn.grid(row=9, column=1, sticky='NE')
no_btn.grid(row=9, column=2, sticky='NW')
A_btn.grid(row=9, column=0)
B_btn.grid(row=9, column=1)
C_btn.grid(row=9, column=2)
D_btn.grid(row=9, column=3)
yes_btn.grid_remove()
no_btn.grid_remove()
A_btn.grid_remove()
B_btn.grid_remove()
C_btn.grid_remove()
D_btn.grid_remove()

try:
    with open('save/save.txt') as save_file:
        high_score = int(save_file.read())
except (FileNotFoundError, ValueError):
    with open('save/save.txt', 'w') as save_file:
        save_file.write(str(0))
        high_score = 0
set_vertical()


def save_high_score():
    with open('save/save.txt', 'w') as output:
        output.write(str(high_score))


def all_answers_from_current_question():
    global all_answer
    all_answer = []
    for ans in quiz.get_current_question().incorrect_answers:
        all_answer.append(ans)
    all_answer.append(quiz.get_current_question().correct_answer)
    random.shuffle(all_answer)
    return all_answer


def set_up_quiz():
    global is_checked
    is_checked = 1

    category_drop.config(state='disabled')
    difficulty_drop.config(state='disabled')

    global question_text, current_question_type, total_nr_of_questions, current_question_nr, correct_answer, question_bank, quiz
    quiz.reset_quiz()
    question_bank = QuestionBank(category=category_selected.get(), difficulty=difficulty_selected.get(),
                                 number_of_questions=MAX_QUESTION_NUMBER)
    quiz = QuizBrain(question_bank.new_question_bank())
    # print(f'Current question number is: {quiz.get_current_question_number()}')
    current_question_nr = quiz.get_current_question_number()
    current_question_type = quiz.get_current_question().question_type
    correct_answer = quiz.get_current_question().correct_answer

    yes_btn.grid_remove()
    no_btn.grid_remove()
    A_btn.grid_remove()
    B_btn.grid_remove()
    C_btn.grid_remove()
    D_btn.grid_remove()

    if current_question_type == 'boolean':
        answer = 'Is it True or False?'
        yes_btn.grid()
        no_btn.grid()
    elif current_question_type == 'multiple':
        ans = all_answers_from_current_question()
        answer = f'''
            A: {ans[0]}
            B: {ans[1]}
            C: {ans[2]}
            D: {ans[3]}
        '''
        A_btn.grid()
        B_btn.grid()
        C_btn.grid()
        D_btn.grid()
        print(root.winfo_height())
    question_text = quiz.get_current_question().question + '\n' + answer
    set_font_size()
    quiz_canvas.itemconfig(quiz_question, text=question_text)


def reset_quiz():
    global score, question_text, current_question_type, total_nr_of_questions, current_question_nr, question_bank, quiz

    score = 0
    question_text = 'Chose a category to play'
    quiz_canvas.itemconfig(quiz_question, text=question_text)

    title_text = f"{quiz.get_current_question_number() + 1}/{quiz.get_total_question_number()}"
    quiz_canvas.itemconfig(quiz_number, text=title_text)

    quiz_canvas.itemconfig(quiz_correct_answer, text='')
    quiz_canvas.itemconfig(quiz_click_here, text='')

    question_bank = QuestionBank()
    quiz = QuizBrain(question_bank.new_question_bank())
    quiz.reset_quiz()
    yes_btn.grid_remove()
    no_btn.grid_remove()
    A_btn.grid_remove()
    B_btn.grid_remove()
    C_btn.grid_remove()
    D_btn.grid_remove()
    category_drop.config(state='normal')
    difficulty_drop.config(state='normal')


def feedback_from_answer():
    global correct_answer

    yes_btn.grid_remove()
    no_btn.grid_remove()
    A_btn.grid_remove()
    B_btn.grid_remove()
    C_btn.grid_remove()
    D_btn.grid_remove()

    calculate_high_score()

    score_label.configure(text=f'Score: {score}')
    high_score_label.configure(text=f'High Score: {high_score}')

    title_text = f"{quiz.get_current_question_number() + 1}/{quiz.get_total_question_number()}"
    quiz_canvas.itemconfig(quiz_number, text=title_text)
    correct_answer_text = 'The correct answer for the question above, is: \n' + quiz.get_current_question().correct_answer
    quiz_canvas.itemconfig(quiz_correct_answer, text=correct_answer_text,
                           font=(LABEL_FONT_NAME, CANVAS_TEXT_FONT_SIZE_MIN, '',))
    click_here = 'Click Here to Continue'
    quiz_canvas.itemconfig(quiz_click_here, text=click_here)
    if layout == 1:
        quiz_canvas.coords(quiz_correct_answer, 400, 400)
        quiz_canvas.coords(quiz_click_here, 550, 450)
    else:
        quiz_canvas.coords(quiz_correct_answer, 300, 450)
        quiz_canvas.coords(quiz_click_here, 300, 550)
    quiz_canvas.bind('<Button-1>', next_step)


def calculate_high_score():
    global high_score
    if score > high_score:
        high_score = score


def next_step(*args):
    global current_question_nr, question_text, current_question_type, is_checked

    yes_btn.grid_remove()
    no_btn.grid_remove()
    A_btn.grid_remove()
    B_btn.grid_remove()
    C_btn.grid_remove()
    D_btn.grid_remove()

    quiz_canvas.itemconfig(quiz_correct_answer, text='')
    quiz_canvas.itemconfig(quiz_click_here, text='')
    quiz_canvas.unbind('<Button-1>')

    quiz.next_question()
    is_checked = 0

    if quiz.still_has_question():
        current_question_nr = quiz.get_current_question_number()
        current_question_type = quiz.get_current_question().question_type
        if current_question_type == 'boolean':
            answer = 'Is it True or False?'
            yes_btn.grid()
            no_btn.grid()
        elif current_question_type == 'multiple':
            ans = all_answers_from_current_question()
            answer = f'''
                    A: {ans[0]}
                    B: {ans[1]}
                    C: {ans[2]}
                    D: {ans[3]}
                '''
            A_btn.grid()
            B_btn.grid()
            C_btn.grid()
            D_btn.grid()
        question_text = quiz.get_current_question().question + '\n\n' + answer
        set_font_size()
        quiz_canvas.itemconfig(quiz_question, text=question_text)
    else:
        calculate_high_score()
        msg_box = tk.messagebox.askquestion('Warning', 'You completed the challenge. \nDo you want to '
                                                       'continue playing?\n\nOtherwise the program quits.',
                                            icon='warning')
        # If the user doesn't want to continue playing, exit
        title_text = f"{quiz.get_current_question_number() + 1}/{quiz.get_total_question_number()}"
        quiz_canvas.itemconfig(quiz_number, text=title_text)
        if msg_box == 'no':
            print(f"Your final score is: {score}/{total_nr_of_questions}")
            save_high_score()
            exit_app()
        if msg_box == 'yes':
            save_high_score()
            reset_quiz()


root.mainloop()
