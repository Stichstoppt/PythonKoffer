"""
Ein Mixin ist eine spezialisierte Klasse, die nur dafür da ist, anderen Klassen bestimmte Methoden (Verhalten) hinzuzufügen, ohne als eigenständige Basisklasse gedacht zu sein.
"""

"""
Die 3 goldenen Regeln eines Mixins:
1. Kein eigener Zustand: Sie hat fast nie eine __init__-Methode oder eigene Instanzvariablen.
2. Nicht instanziierbar: Man erstellt nie ein Objekt direkt aus einem Mixin (x = MeinMixin() ist sinnlos).
3. Pluggable: Sie bietet fertig programmierte Methoden, die jede Klasse sofort nutzen kann, solange die Klasse bestimmte Voraussetzungen erfüllt. 
"""


# Das Mixin: Bietet fertige Funktionalität (JSON-Konvertierung)
class JSONMixin:
    def to_json(self):
        import json

        return json.dumps(self.__dict__)


# Die Hauptklasse: Nutzt das Mixin über Mehrfachvererbung
class Auto(JSONMixin):
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell


# Nutzung:
mein_auto = Auto("Tesla", "Model 3")
print(mein_auto.to_json())  # Ausgabe: {"marke": "Tesla", "modell": "Model 3"}
