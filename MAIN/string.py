###################
######Strings######
###################

s = "  Python ist super!  "

""" BEREINIGEN & FORMATIEREN (Gibt neuen String zurück) """
s_clean = s.strip()  # Entfernt Whitespaces am Start/Ende -> "Python ist super!"
s_lower = s_clean.lower()  # Alles klein -> "python ist super!"
s_upper = s_clean.upper()  # Alles groß -> "PYTHON IST SUPER!"

""" TEILEN & ZUSAMMENFÜGEN (Sehr wichtig für Klausuren) """
# .split() macht aus einem String eine LISTE
words_list = s_clean.split(" ")  # -> ["Python", "ist", "super!"]

# .join() macht aus einer Liste einen STRING (Syntax beachten: "trennzeichen".join())
connected = "-".join(words_list)  # -> "Python-ist-super!"

""" SUCHEN, ERSETZEN & PRÜFEN """
replaced = s_clean.replace("super", "toll")  # Ersetzt Substrings
idx = s_clean.find("ist")  # Gibt Start-Index zurück (hier 7). Wenn nicht gefunden: -1

# Gibt immer Boolean (True/False) zurück:
is_in = "Python" in s_clean  # True (O(n)-Laufzeit, zieht durch den String)
starts = s_clean.startswith("Py")  # True
ends = s_clean.endswith("!")  # True
is_num = "123".isdigit()  # True (Prüft, ob der String nur aus Zahlen besteht)

""" STRING SLICING (Syntax: [start:stop:step]) """
text = "Klausur"
reverse_text = text[::-1]  # Dreht den String komplett um -> "rusualK"
sub_text = text[0:4]  # Schneidet von Index 0 bis exklusive 4 ab -> "Klau"

""" EFFICIENT FORMATTING (f-Strings) """
version = 3.13
info = f"Python {version} ist aktuell."  # Ausdrücke in {} werden direkt evaluiert
