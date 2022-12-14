from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from collections import abc  # noqa
from functools import partial
from typing import Any, Generic, TypeVar


_T = TypeVar("_T")


class PlaceholderEntry(ttk.Entry):
    def __init__(
        self,
        master: ttk.Widget,
        *args: Any,
        placeholder: str,
        prefill: str = '',
        placeholdercolor: str = "grey60",
        **kwargs: Any,
    ):
        super().__init__(master, *args, **kwargs)
        self._prefill: str = prefill
        self._show: str = kwargs.get("show", '')
        self._text_color: str = kwargs.get("foreground", '')
        self._ph_color: str = placeholdercolor
        self._ph_text: str = placeholder
        self.bind("<FocusIn>", self._focus_in)
        self.bind("<FocusOut>", self._focus_out)
        if isinstance(self, ttk.Combobox):
            # only bind this for comboboxes
            self.bind("<<ComboboxSelected>>", self._combobox_select)
        self._ph: bool = False
        self._insert_placeholder()

    def _insert_placeholder(self) -> None:
        """
        If we're empty, insert a placeholder, set placeholder text color and make sure it's shown.
        If we're not empty, leave the box as is.
        """
        if not super().get():
            self._ph = True
            super().config(foreground=self._ph_color, show='')
            super().insert("end", self._ph_text)

    def _remove_placeholder(self) -> None:
        """
        If we've had a placeholder, clear the box and set normal text colour and show.
        """
        if self._ph:
            self._ph = False
            super().delete(0, "end")
            super().config(foreground=self._text_color, show=self._show)
            if self._prefill:
                super().insert("end", self._prefill)

    def _focus_in(self, event: tk.Event[PlaceholderEntry]) -> None:
        self._remove_placeholder()

    def _focus_out(self, event: tk.Event[PlaceholderEntry]) -> None:
        self._insert_placeholder()

    def _combobox_select(self, event: tk.Event[PlaceholderEntry]):
        # combobox clears and inserts the selected value internally, bypassing the insert method.
        # disable the placeholder flag and set the color here, so _focus_in doesn't clear the entry
        self._ph = False
        super().config(foreground=self._text_color, show=self._show)

    def _store_option(
        self, options: dict[str, object], name: str, attr: str, *, remove: bool = False
    ) -> None:
        if name in options:
            if remove:
                value = options.pop(name)
            else:
                value = options[name]
            setattr(self, attr, value)

    def configure(self, *args: Any, **kwargs: Any) -> Any:
        options: dict[str, Any] = {}
        if args and args[0] is not None:
            options.update(args[0])
        if kwargs:
            options.update(kwargs)
        self._store_option(options, "show", "_show")
        self._store_option(options, "foreground", "_text_color")
        self._store_option(options, "placeholder", "_ph_text", remove=True)
        self._store_option(options, "prefill", "_prefill", remove=True)
        self._store_option(options, "placeholdercolor", "_ph_color", remove=True)
        return super().configure(**kwargs)

    def config(self, *args: Any, **kwargs: Any) -> Any:
        # because 'config = configure' makes mypy complain
        self.configure(*args, **kwargs)

    def get(self) -> str:
        if self._ph:
            return ''
        return super().get()

    def insert(self, index: tk._EntryIndex, content: str) -> None:
        # when inserting into the entry externally, disable the placeholder flag
        if not content:
            # if an empty string was passed in
            return
        self._remove_placeholder()
        super().insert(index, content)

    def delete(self, first: tk._EntryIndex, last: tk._EntryIndex | None = None) -> None:
        super().delete(first, last)
        self._insert_placeholder()

    def clear(self) -> None:
        self.delete(0, "end")

    def replace(self, content: str) -> None:
        super().delete(0, "end")
        self.insert("end", content)


class PlaceholderCombobox(PlaceholderEntry, ttk.Combobox):
    pass


class HelpLabel(ttk.Label):
    WRAPLENGTH = 200

    def __init__(
        self, master: tk.Misc, *args: Any, delay: int = 800, tooltip: str = '', **kwargs: Any
    ):
        super().__init__(master, *args, **kwargs)
        self.delay: int = delay
        self.tooltip: str = tooltip
        self._tlw: tk.Wm | None = None
        self._schedule_id: str | None = None
        self.bind("<Enter>", self._schedule)
        self.bind("<Leave>", self._hide)

    def _schedule(self, event: tk.Event[HelpLabel]):
        if self._schedule_id is None:
            self._schedule_id = self.after(self.delay, self._show)

    def _show(self):
        self._tlw = tk.Toplevel(self)
        self._tlw.wm_overrideredirect(True)
        x = self.winfo_pointerx() + 2
        y = self.winfo_pointery() - 20
        self._tlw.wm_geometry(f"+{x}+{y}")
        label = ttk.Label(
            self._tlw,
            text=self.tooltip,
            justify="left",
            background="lightyellow",
            relief="solid",
            borderwidth=1,
            wraplength=self.WRAPLENGTH,
        )
        label.pack(ipadx=1)

    def _hide(self, event: tk.Event[HelpLabel] | None = None):
        if self._schedule_id is not None:
            self.after_cancel(self._schedule_id)
            self._schedule_id = None
        if self._tlw is not None:
            self._tlw.destroy()  # type: ignore


class SelectMenu(tk.Menubutton, Generic[_T]):
    def __init__(
        self,
        master: tk.Misc,
        *args: Any,
        tearoff: bool = False,
        options: dict[str, _T],
        relief: tk._Relief = "solid",
        background: tk._Color = "white",
        **kwargs: Any,
    ):
        super().__init__(master, *args, background=background, relief=relief, width=40, **kwargs)
        self._options: dict[str, _T] = options
        self.menu = tk.Menu(self, tearoff=tearoff)
        self.config(menu=self.menu)
        for name in options.keys():
            self.menu.add_command(label=name, command=partial(self.config, text=name))

    def get(self) -> _T | None:
        return self._options.get(self.cget("text"))
