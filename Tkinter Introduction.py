import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.title('Main Window')
# window.resizable(False, False)
# window.configure(background='green')


def first_function():
    text = 'Hello World!'
    text_output = tk.Label(window, text=text, fg='red', font=('Helvetica', 16))  # what to display and how
    text_output.grid(row=0, column=1, sticky='W')


def second_function():
    text = 'Message! Second button function'
    text_output = tk.Label(window, text=text, fg='purple', font=('Comic Sans MS', 12))  # what to display and how
    text_output.grid(row=1, column=1, sticky='W', padx=50)


first_btn = tk.Button(text='Hello', command=first_function)
first_btn.grid(row=0, column=0, sticky='W')

first_btn = tk.Button(text='Second', command=second_function)
first_btn.grid(row=1, column=0, sticky='W', pady=20)

if __name__ == '__main__':
    window.mainloop()  #allows to execute main window
