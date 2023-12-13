from __future__ import annotations

from collections.abc import Callable
from enum import Enum, IntEnum, auto
from typing import TypedDict

import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class ButtonType(IntEnum):
    OPERATOR = auto()
    DIGIT = auto()
    RESULT = auto()


class ButtonColour(str, Enum):
    DARK_GREY = '#323232'
    LIGHT_GREY = '#3b3b3b'


class ButtonData(TypedDict):
    text: str
    function: Callable[[], None]
    variant: ButtonType


buttons: list[ButtonData] = [
    {
        'text': '',
        'function': object,
        'variant': ButtonType,
    }
]

# class MainWindow:
#     def __init__(self, root: customtkinter.CTk):
#         self.root = root
#         self.root.geometry("400x240")
#         self.button = customtkinter.CTkButton(master=self.root, text="CtkButton", command=self.button_function)
#         self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

#     def button_function(self):
#         print("Button pressed")

class OutputPanel(ctk.CTkFrame):
    pass

class ButtonGrid(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.buttons = [
            NumberButton(self, text=f'{num}', width=80, anchor=ctk.BOTTOM)
            for num in range(1, 10)
        ]

        for idx, button in enumerate(self.buttons):
            y, x = divmod(idx, 3)
            button.grid(row=y, column=x, padx=1, pady=1)
            button.configure(fg_color="#3b3b3b")
            

class NumberButton(ctk.CTkButton):
    def __init__(self, parent: ctk.CTkFrame, text: str, *args, **kwargs):
        super().__init__(master=parent, text=text, *args, **kwargs)

class OperatorButton(ctk.CTkButton):
    def __init__(self, parent: ctk.CTkFrame, text: str, *args, **kwargs):
        super().__init__(master=parent, text=text, *args, **kwargs)

class MainWindow(ctk.CTk):
    def __init__(self: MainWindow):
        super().__init__()

        self.title("Calculator")
        self.geometry("320x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.output_panel = OutputPanel(self)
        self.button_grid = ButtonGrid(self)
        self.button = NumberButton(self, "Testing", width=10)
        
        self.output_panel.grid(row=0, sticky='NEW')
        # self.button.grid(row=0, column=0)
        # self.button.configure(fg_color="#323232")
        self.button_grid.grid(row=1, sticky='SEW', columnspan=1)
        self.button_grid.configure(fg_color="#202020")
        

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

