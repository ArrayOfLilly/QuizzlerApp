import tkinter as tk
from tkinter import ttk

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
style = ttk.Style(window)
style.theme_use('classic')


def select_from_list(event):
    selected = event.widget.get()
    print(selected)


# label text for title
ttk.Label(window, text="Choose a category from the list: ",
          background='cyan', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)

# Set label
ttk.Label(window, text="Select the Category :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=5, padx=5, pady=25)

# Create Combobox
selection = tk.StringVar()
category_drop = ttk.Combobox(window, width=27, textvariable=selection, state='readonly')

# Adding combobox drop down list
category_drop['values'] = ('General Knowledge',
                    'Entertainment: Books',
                    'Entertainment: Film',
                    'Science & Nature',
                    'Science: Computers',
                    'Mythology',
                    'Geography',
                    'History',
                    'Sports',
                    'Animals',
                    'Politics',
                    'Animals',
                    'Entertainment: Japanese Anime & Manga',
                    'Entertainment: Cartoon & Animation',
                    )

category_drop.grid(column=1, row=5)
category_drop.current(0)
category_drop.bind("<<ComboboxSelected>>", select_from_list)

window.mainloop()
