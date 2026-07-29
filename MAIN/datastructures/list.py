##############
#####LIST#####
##############

"""Erzeugung & Slicing (Syntax: [start:stop:step])"""

lst = [10, 20, 30, 40, 50]
rev = lst[::-1]  # Liste umdrehen -> [50, 40, 30, 20, 10]
every_2nd = lst[::2]  # Jedes 2. Element -> [10, 30, 50]
copy_lst = lst[:]  # Flache Kopie (Shallow Copy)
lst2 = [1, 2, 3, 4]
lst += lst2  # Konkatenation (Verkettung) -> [10, 20, 30, 40, 50, 1, 2, 3, 4]

""" Wichtige Laufzeiten (O-Notation) """
lst.append(60)  # O(1) - Sehr schnell am Ende
lst.extend([70, 80, 90])  # Add all.
lst.pop()  # O(1) - Sehr schnell am Ende entfernen
lst.insert(0, 5)  # O(n) - KATASTROPHE! Verschiebt alle Elemente nach rechts
lst.pop(0)  # O(n) - KATASTROPHE! Verschiebt alle Elemente nach links
val = lst[2]  # O(1) - Direkter Index-Zugriff ist extrem schnell
exists = 30 in lst  # O(n) - Langsam! Lineare Suche von links nach rechts
lst.index(30)  # O(n) - Langsam! Lineare Suche von links nach rechts
# lst.clear() # O(n) - Löscht die Liste (alle Referenzen werden entfernt)
lst.reverse()  # In-place.

""" Sortierung """
lst.sort()  # O(n log n) - Sortiert die Liste direkt (In-place)
new_lst = sorted(lst)  # O(n log n) - Gibt eine NEUE sortierte Liste zurück

""" Löschen """
del lst[1]  # Löscht das Element an Index 1
lst.remove(30)  # Löscht das erste Vorkommen von 30

""" Immutable list ist ein Tuple! """
tupel = (1, 2, 3)

""" Shallow vs. Deep Kopie """
import copy

nested = [[1, 2], [3, 4]]
shallow = nested.copy()  # Änderungen an nested[0][0] ändern AUCH shallow!
deep = copy.deepcopy(nested)  # Vollständig isoliert
