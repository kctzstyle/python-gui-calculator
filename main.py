
import tkinter as tk

from app import Application


if __name__ == '__main__':
    window = tk.Tk()
    window.title('계산기')
    window.geometry("240x270")
    window.resizable(False, False)

    app = Application(master=window)
    app.mainloop()
