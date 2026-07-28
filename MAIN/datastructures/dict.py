##############
#####DICT#####
##############

"""Erzeugung & Laufzeiten (O-Notation)"""

d = {"a": 1, "b": 2}
val = d["a"]  # O(1) im Schnitt - Extrem schneller Zugriff über Hash
d["c"] = 3  # O(1) im Schnitt - Schnelles Einfügen
del d["b"]  # O(1) im Schnitt - Schnelles Löschen
exists = "a" in d  # O(1) im Schnitt - Prüft nur KEYS, nicht Values! Extrem schnell.

""" Fehlende Keys abfangen """
# val = d["missing"]     # X Führt sofort zu einem KeyError-Absturz!
val = d.get("missing", 0)  #  Sicher! Gibt 0 zurück, wenn Key nicht existiert.

""" setdefault """
# wenn "key" schon in dict, dann passiert nichts, sonst wird neuer eintrag mit key und default value
d.setdefault("key", 3)

# Ansichten (Views) iterieren
for key, value in d.items():
    pass  # Unpacking von Key und Value in der Schleife
