from dataclasses import dataclass
from enum import Enum, auto


# --- 1. SWITCH-CASE (Enums) ---
class Color(Enum):
    RED, GREEN, BLUE = auto(), auto(), auto()


def switch_demo(color: Color):
    match color:
        case Color.RED:
            return "red"
        case Color.GREEN:
            return "green"
        case Color.BLUE:
            return "blue"


# --- 2. STRUCTURAL MATCHING (Listen & Strings) ---
def structure_demo(line: str):
    match line.split():
        case [action]:  # 1 Element: Name binden
            return f"Action: {action}"
        case ["quit"]:  # Exakter Wert
            return "Quit Game"
        case ["get", obj]:  # Wert + Name binden
            return f"Get {obj}"
        case ["drop", *objs]:  # Extended Unpacking (Rest sammeln)
            return f"Drop list: {objs}"
        case ["north"] | ["go", "north"]:  # OR-Pattern (Mehrere Wege)
            return "Going North"
        case ["go", ("east" | "west") as d]:  # Sub-Pattern mit Bindung (`as`)
            return f"Going {d}"
        case ["run", d] if d in ["N", "S"]:  # Guard (Bedingung mit `if`)
            return f"Running {d}"
        case ["run", _]:  # Wildcard `_` (Unbekannte Richtung)
            return "Run unknown"
        case _:  # Default-Fall
            return "Unknown command"


# --- 3. DICTIONARIES (Inhalt & Typen) ---
def dict_demo(d: dict):
    match d:
        case {
            "index": idx,
            "name": name,
        }:  # Extrahiert Keys (Restliche Keys ignorieren)
            return f"{idx=}, {name=}"
        case {"text": str(msg)}:  # Typprüfung innerhalb des Dicts
            return f"Text message: {msg}"
        case {"sleep": duration}:  # Einzelner Key
            return f"Sleep for {duration}"


# --- 4. KLASSEN-ATTRIBUTE & TYPEN ---
@dataclass
class Point:
    x: int
    y: int


def type_demo(obj):
    match obj:
        case Point(x=0, y=0):  # Klassen-Attribute abgleichen
            return "Origin"
        case Point(x=0, y=y_val):  # Attribut abgleichen + Bindung an neuen Namen
            return f"Y-Axis at {y_val}"
        case Point():  # Instanz-Prüfung (Irgendein Punkt)
            return "Somewhere"
        case str(text):  # Reine Typ-Prüfung (isinstance) + Bindung
            return f"String: {text}"
        case (kind, int(n)):  # Verschachteltes Tupel + Typ-Prüfung im Element
            return f"Tuple: {kind=}, {n=}"
