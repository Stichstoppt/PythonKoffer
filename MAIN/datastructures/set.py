###############
######SET######
###############

# 1. Erzeugung & Laufzeiten (O-Notation)
# FALLE: {} erzeugt ein leeres DICT! Ein leeres Set MUSS so erzeugt werden:
empty_set = set()

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(5)  # O(1) im Schnitt - Schnelles Hinzufügen
s1.remove(2)  # O(1) - Löschen. Führt zu KeyError, wenn 2 fehlt!
s1.discard(99)  # O(1) - Sicher löschen. Ignoriert Fehler, wenn 99 fehlt.
exists = 3 in s1  # O(1) im Schnitt - Sensationell schnell im Vergleich zu Listen!

# 2. Mathematische Mengenoperationen (Venn-Diagramm)
# Wichtig für die Klausur: Operator-Schreibweise (| & - ^)
union = s1 | s2  # Vereinigung: {1, 2, 3, 4, 5, 6}
intersect = s1 & s2  # Schnittmenge: {3, 4}
diff = s1 - s2  # Differenz: {1, 2} (In s1, aber NICHT in s2)
sym_diff = (
    s1 ^ s2
)  # Symmetrische Diff: {1, 2, 5, 6} (In einem von beiden, aber nicht in beiden)

# 3. Teilmengen-Abfragen
is_sub = {1, 2}.issubset(s1)  # Gibt True zurück
