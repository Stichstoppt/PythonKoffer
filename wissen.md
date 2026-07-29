# Integer Caching
In Python gibt is bei Integern genau dann True zurück, wenn sich die Werte im Bereich von -5 bis 256 befinden.

# Division
/ ist echte Division, kein Flooring
// Floor Division wie man sie aus Java oder C kennt. Float bleibt Float -> 1.5/1.0 = 1.0

# Tail Call Optimization (TLO)
GIBT ES NICHT IN PYTHON
Bei rekursiven Fkts. wird optimiert, wenn im return nur der pure rekursive Aufruf ist ohne Berechnung

# Global Interpreter Lock (GIL)
Die GIL (Global Interpreter Lock) ist ein Synchronisationsmechanismus in CPython, der sicherstellt, dass immer nur ein Thread gleichzeitig Python-Bytecode ausführt. Dadurch wird die Speicherverwaltung von Python threadsicher, allerdings blockiert es echtes Multithreading auf Multi-Core-CPUs bei rechenintensiven Aufgaben (CPU-bound).

# Deadlock
Zwei oder mehr Threads blockieren sich dauerhaft gegenseitig, weil jeder auf eine Ressource wartet, die der andere gerade hält.

# Livelock
Livelock: Zwei oder mehr Threads ändern als Reaktion aufeinander ständig aktiv ihren Zustand, kommen dadurch aber nie mit ihrer eigentlichen Arbeit voran (wie zwei Fußgänger, die im Flur synchron immer wieder in dieselbe Richtung ausweichen).

# Wie erweitert man eine Zeile? 
return \
    result                              # This is one logical line, the backslash continues it.

# Wie verhalten sich default Values in Python?
Nutze niemals veränderliche Objekte (wie [] oder {} oder Instanzen von Klassen ) als Standardargumente in Funktionsdefinitionen, da diese nur ein einziges Mal beim Laden des Codes erstellt und danach von allen Funktionsaufrufen geteilt werden. Verwende stattdessen stattdessen immer None als Standardwert und initialisiere die Liste sicher erst innerhalb der Funktion mit if param is None: param = [].

# Was ist eine Klasse in Python?
Ein Objekt, welches auch Attribute und Methoden(@classmethod) haben kann.

# Was ist der Unterschied zwischen @classmethod und @staticmethod?
@classmethod ist eine Methode, die zu dem Objekt der Klasse gehört (erster Parameter ist cls)
@staticmethod ist eine freistehende Methode ohne Zugriff auf cls & self, die aber semantisch zur Klasse passt.


## Primitives

# Ints
Ints können beliebig lang sein, d. h. sie sind "exakt". Der Speicherbedarf hängt von der Länge ab, daher benötigen kurze Ints weniger Speicher.

# Bools
Wichtig: Eine Konvertierung in ein Bool prüft im Wesentlichen, ob der Wert eine Art von Null oder leer ist (false) oder nicht, d. h. !=0 (true). Rangfolge der Booleschen Operatoren: not > and > or

# Floats
Fast alle Python-Varianten implementieren 'float' nach IEEE-754 "Double Precision", d. h. als Standard-'double'. Konstanten wie 'inf' können manchmal verwendet werden, um Variablenin Algorithmen zu initialisieren. Achtung: Operationen mit 'nan' oder 'inf' können zu seltsamem oderunerwartetem Verhalten führen. Jede Operation mit 'nan' ergibt 'nan'. Bei 'inf' hängt es davon ab. Normale Float-Mathematik bleibt oft auf dem Fast-Path der CPU(vektorisiert, gepipelined). Sobald 'inf' oder 'nan' ins Spiel kommen, müssen CPUs/Runtimes oft langsame Pfade nehmen, Extra-Checks machenoder IEEE-754-Exceptions auslösen/maskieren.

========================
float_inf = float("inf")
========================

# Strings
Überraschenderweise kann man Strings, aber auch Kommentare, mit '' statt "" definieren. Die Wahl ist frei, es gibt keine Empfehlung. Wichtig: Strings sind immutable(unveränderlich), d. h. Operationen wie '+=', 'replace', 'upper' etc. geben immer einen neuen String zurück. 

# None
None wird oft verwendet, um einen nicht spezifizierten Wert darzustellen,wie einen nicht gesetzten Parameter. Es ähnelt einer Null-Referenz undist false, wenn es in eine Boolesche Variable konvertiert wird.

# Wert-Gleichheit 
(==):Prüft, ob zwei Objekte denselben Wert haben. Für die meisten eingebauten Typen nutzt Python typspezifische __eq__-Methoden, um den Wertvergleich zu implementieren. Zwei verschiedene Objekte im Speicher können vom Wert her dennoch gleich sein. 
Identitäts-Gleichheit (is): Prüft, ob zwei Objekte exakt dieselbe Instanz sind, d. h. identisch im Speicher.is ergibt nur dann True, wenn zwei Variablen auf dasselbe Objekt verweisen.

