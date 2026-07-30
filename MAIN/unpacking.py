# GRUNDLAGEN (1:1 Zuweisung & Tausch)
x, y = 10, 20               # x = 10, y = 20
x, y = y, x                 # x = 20, y = 10 (Werte getauscht)
a, b, c = "XYZ"             # a = 'X', b = 'Y', c = 'Z' (Strings sind Iterables)

# 2. EXTENDED UNPACKING (Der *-Operator auf der LINKEN Seite)
# Der Stern sammelt die "Reste" immer als Liste.
first, *rest = [1, 2, 3, 4]       # first = 1, rest = [2, 3, 4]
*rest, last = [1, 2, 3, 4]        # rest =, last = 4
start, *mid, end = [1, 2, 3, 4]   # start = 1, mid =, end = 4

# Verschachteltes Unpacking
head, (sub_head, *sub_rest) = [1, [2, 3, 4]]  # head=1, sub_head=2, sub_rest=[3, 4]

# 3. WERTE IGNRIEREN (Konvention mit _)
_, wichtig, _ = (100, 200, 300)   # wichtig = 200 (Rest ignoriert)
first_item, *_ = [5, 6, 7, 8]     # first_item = 5 (kompletter Rest ignoriert)
anfang, *_, ende =# anfang = 1, ende = 5 (Mitte komplett egal)

# 4. ITERABLES ZUSAMMENFÜHREN (Der * und **-Operator auf der RECHTEN Seite)
liste_a = [1, 2]
liste_b = [4, 5]
kombiniert = [*liste_a, 3, *liste_b]  # kombiniert = [1, 2, 3, 4, 5]

dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 99, 'z': 3}            # 'y' existiert in beiden Dicts
merged = {**dict_a, **dict_b}         # {'x': 1, 'y': 99, 'z': 3} (Rechts überschreibt Links!)

# 5. FUNKTIONEN (Sammeln vs. Verteilen)
# A) Sammeln in der Definition:
def universelle_funktion(*args, **kwargs):
    # args fängt Positionsargumente als Tupel ab
    # kwargs fängt Keyword-Argumente als Dict ab
    return f"Args: {args}, Kwargs: {kwargs}"

# B) Verteilen beim Aufruf:
koordinaten = (10, 20)
def zeige_punkt(a, b):
    return f"Punkt bei X={a}, Y={b}"

# Aufruf durch Entpacken des Tupels
ergebnis = zeige_punkt(*koordinaten)  # Entspricht zeige_punkt(10, 20)
