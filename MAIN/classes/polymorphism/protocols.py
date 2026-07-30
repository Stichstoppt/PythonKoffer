"""
Predefined-protocols
    Iterable[T]     def __iter__(self) -> Iterator[T]
    Iterator[T]     def __next__(self) -> T
                    def __iter__(self) -> Iterator[T]
    Sized           def __len__(self) -> int
    Container[T]    def __contains__(self, x: object) -> bool       # in-operator

    Sequence        def __getitem__(self, s)
                    def __len__(self):
"""

from typing import Protocol, Iterable


# ==========================
# PROTOKOLL DEFINIEREN
# ==========================
class Clickable(Protocol):
    def on_click(self) -> None: ...


# ================================


# ================================
# KLASSEN IMPLEMENTIEREN PROTOKOLL
# ================================
class Button:  # No Clickable base class!
    def on_click(self) -> None:  # Just same name and signature!! -> Static ducktpying
        print(" a|   - Button.on_click")


class Switch:
    def on_click(self) -> None:
        print(" b|   - Switch.on_click")


# ================================


def recap_protocol():
    def click_all(clickable: Iterable[Clickable]) -> None:
        for c in clickable:
            c.on_click()

    click_all([Button(), Switch()])
