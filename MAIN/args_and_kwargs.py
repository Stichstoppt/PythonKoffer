# LINKS vom / : Nur Position
# RECHTS vom * : Nur Keyword (Name)
def power_funktion(x, y, /, standard, *, runden=False):
    print(f"{x=}, {y=}, {standard=}, {runden=}")


# --- RICHTIGER AUFRUF ---
power_funktion(2, 3, 10, runden=True)  # Funktioniert perfekt
power_funktion(2, 3, standard=10, runden=True)  # Funktioniert auch (Mitte ist flexibel)

# --- FALSCHE AUFRUFE (Werfen beide einen TypeError) ---
# power_funktion(x=2, y=3, 10, runden=True)   # Fehler! x und y MÜSSEN namenlos sein
# power_funktion(2, 3, 10, True)              # Fehler! runden MUSS mit Namen genannt werden


# Definition aller möglichen Argument-Typen in der exakt vorgeschriebenen Reihenfolge:
def super_funktion(
    a,
    b,  # 1. Positionelle Argumente (Pflicht)
    c=10,  # 2. Optionale positionelle Argumente (mit Default-Wert)
    *args,  # 3. Beliebig viele weitere positionelle Argumente (als Tupel)
    d,  # 4. Keyword-Only Argument (MUSS mit 'd=...' übergeben werden)
    e=20,  # 5. Keyword-Only Argument (mit Default-Wert)
    **kwargs,  # 6. Beliebig viele weitere Keyword-Argumente (als Dictionary)
):
    print(f"{a=}, {b=}, {c=}, {args=}, {d=}, {e=}, {kwargs=}")
    print(f"{args} ist ein Tupel!")
    print(f"{kwargs} ist ein Dict!")


# --- DER AUFRUF (So verhalten sich die Argumente) ---

super_funktion(
    1,
    2,  # a=1, b=2
    3,  # c=3 (überschreibt den Default-Wert 10)
    4,
    5,
    6,  # args=(4, 5, 6)
    d="Pflicht!",  # d="Pflicht!" (Keyword-Only, Name ist zwingend!)
    e=99,  # e=99 (überschreibt den Default-Wert 20)
    beispiel=100,
    x=200,  # kwargs={'beispiel': 100, 'x': 200}
)
