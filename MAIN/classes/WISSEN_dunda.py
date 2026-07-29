"""
===================================================
# Was ist der Unterschied zwischen __repr__ und __str__?
__str__ (für den Endnutzer)
Ziel: Eine schöne, gut lesbare und verständliche Textausgabe (human-readable).
Aufruf: Die Funktion str(obj) oder direkt beim Drucken mit print(obj).
Standard-Verhalten: Wenn eine Klasse kein __str__ definiert hat, fällt Python automatisch auf __repr__ zurück.

__repr__ (für den Entwickler)
Ziel: Eine eindeutige, technische und unmissverständliche Darstellung des Objekts (unambiguous). Sie sollte im Idealfall so aussehen, dass man sie als Python-Code kopieren könnte, um das Objekt exakt so neu zu erschaffen.
Aufruf: Die Funktion repr(obj), beim Anzeigen in der interaktiven Konsole (REPL) oder beim Debuggen.
Standard-Verhalten: Wenn nicht definiert, gibt es die unschöne Standard-Adresse zurück (z. B. <__main__.Spieler object at 0x... >).

WICHTIG: Wenn __repr__ definiert ist aber kein __str__, ruft print das __repr__ auf
===================================================

===================================================
# Was ist der Unterschied zwischen __repr__ und __str__?
__new__(cls, ...) – Die Geburt
Aufgabe: Erstellt die eigentliche Instanz der Klasse im Arbeitsspeicher.
Typ: Es ist eine Klassenmethode (erhält als ersten Parameter die Klasse cls, nicht die Instanz self).
Rückgabewert: Muss zwingend das neu erstellte Objekt zurückgeben (über super().__new__(cls)). Wenn hier nichts zurückgegeben wird, bricht der Prozess ab und __init__ wird niemals aufgerufen.
Einsatzbereich: Wird in 99 % der Fälle nicht angefasst. Man braucht es fast nur für fortgeschrittene Muster, wie das Erzeugen von Singletons oder das Vererben von unveränderlichen Typen (int, str, tuple).

__init__(self, ...) – Die Taufe
Aufgabe: Befüllt das frisch gebackene Objekt mit Attributen (Zuweisung von self.name = ...).
Typ: Es ist eine Instanzmethode (erhält das bereits existierende Objekt als self).
Rückgabewert: Darf niemals etwas zurückgeben (gibt implizit None zurück). Ein return mit einem Wert führt sofort zu einem TypeError.
===================================================

===================================================
# Destruktor
__del__(self)
wird aufgerufen, wenn Referenzcounter auf Objekt null wird
===================================================
"""
