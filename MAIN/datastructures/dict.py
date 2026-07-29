##############
#####DICT#####
##############

"""Erzeugung & Laufzeiten (O-Notation)"""

d = {"a": 1, "b": 2}
val = d["a"]  # O(1) im Schnitt - Extrem schneller Zugriff über Hash
d["c"] = 3  # O(1) im Schnitt - Schnelles Einfügen
del d["b"]  # O(1) im Schnitt - Schnelles Löschen
d.pop("c")  # O(1) im Schnitt - Schnelles Löschen, gibt den Wert zurück
exists = "a" in d  # O(1) im Schnitt - Prüft nur KEYS, nicht Values! Extrem schnell.

""" Zugriff auf alle Elemente """
d.keys()
d.values()
d.items()

""" Fehlende Keys abfangen """
# val = d["missing"]     # X Führt sofort zu einem KeyError-Absturz!
val = d.get("missing", 0)  #  Sicher! Gibt 0 zurück, wenn Key nicht existiert.

""" Hinzufügen & Überschreiben """
# wenn "key" schon in dict, dann passiert nichts, sonst wird neuer eintrag mit key und default value
d.setdefault("key", 3)
d.update({"five": 5, "six": 6})  # Add all, extend, but also overwrites existing keys.

""" Immutable dict """
fset = frozenset({2, 3, 5, "seven"})  # Frozen set, immutable.

""" Ansichten (Views) iterieren """
for key, value in d.items():
    pass  # Unpacking von Key und Value in der Schleife
