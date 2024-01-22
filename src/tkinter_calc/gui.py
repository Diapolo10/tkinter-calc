"""Calculator GUI."""

from __future__ import annotations

from enum import Enum, IntEnum, auto
from typing import TYPE_CHECKING, Any, TypedDict, Unpack

import customtkinter as ctk

if TYPE_CHECKING:
    from collections.abc import Callable

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class ButtonType(IntEnum):
    """Button types."""

    OPERATOR = auto()
    DIGIT = auto()
    RESULT = auto()


class ButtonColour(str, Enum):
    """Button colours."""

    DARK_GREY = '#323232'
    LIGHT_GREY = '#3b3b3b'


class ButtonData(TypedDict):
    """Data describing a button."""

    text: str
    function: Callable[[], None]
    variant: ButtonType


buttons: list[ButtonData] = [
    {
        'text': '',
        'function': object,
        'variant': ButtonType,
    },
]


class OutputPanel(ctk.CTkFrame):
    """The results are shown here."""

class ButtonGrid(ctk.CTkFrame):
    """Grid of buttons used to operate the calculator."""

    def __init__(self: ButtonGrid, parent: ctk.CTkFrame, *args: Unpack[Any], **kwargs: Unpack[Any]) -> None:
        """Initialise grid of buttons."""
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
    """Button for numbers."""

    def __init__(self: NumberButton, parent: ctk.CTkFrame, text: str, *args: Unpack[Any], **kwargs: Unpack[Any]) -> None:
        """Initialise number button."""
        super().__init__(*args, master=parent, text=text, **kwargs)

class OperatorButton(ctk.CTkButton):
    """Button for operators."""

    def __init__(self: OperatorButton, parent: ctk.CTkFrame, text: str, *args: Unpack[Any], **kwargs: Unpack[Any]) -> None:
        """Initisalise operator button."""
        super().__init__(*args, master=parent, text=text, **kwargs)

class MainWindow(ctk.CTk):
    """Main program window."""

    def __init__(self: MainWindow) -> None:
        """Initialise main program window."""
        super().__init__()

        self.title("Calculator")
        self.geometry("320x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.output_panel = OutputPanel(self)
        self.button_grid = ButtonGrid(self)
        self.button = NumberButton(self, "Testing", width=10)

        self.output_panel.grid(row=0, sticky='NEW')
        # NOTE: Play with self.button.grid(row=0, column=0)
        # NOTE: Play with self.button.configure(fg_color="#323232")
        self.button_grid.grid(row=1, sticky='SEW', columnspan=1)
        self.button_grid.configure(fg_color="#202020")


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

