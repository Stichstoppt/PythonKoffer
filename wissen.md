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
