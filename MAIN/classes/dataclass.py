"""
- generated __init__, __repr__ and equality
- field(default_factory=...) for mutable defaults
- properties possible, but not needed for simple cases
"""

from dataclasses import dataclass, field


@dataclass(
    init=True, repr=True, frozen=False
)  # controls method generation, frozen makes instance immutable
class Example:
    x: int
    y: int = 0
    size: int = 0

    root: int = field(
        repr=False, default=-1
    )  # removed from repr, more field info, cf. str()

    lst: list[int] = field(
        default_factory=list
    )  # use a factory, same problem as default variables in funcs

    def __post_init__(self):  # is called after init
        self.size = len(self.lst)
