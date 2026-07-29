# =========================================
# Falsy Values
# =========================================
falsy_list = [False, None, 0, 0.0, "", [], (), {}, set(), range(0)]

# =========================================
# Casts
# =========================================

# NACH INT CASTEN: int()
i1 = int(3.99)  # ⚠️ Nachkommastellen werden ABGESCHNITTEN (keine Rundung!) -> 3
i2 = int(-2.7)  # Schneidet Richtung Null ab -> -2
i3 = int("42")  # Reiner Zahlen-String wird zum Integer -> 42
i4 = int(True)  # Boolean True wird zu -> 1 (False wird zu 0)

# ❌ FALLE: int("42.5") -> ValueError! (Strings mit Dezimalpunkt direkt nach int casten schlägt fehl)
# Fix: Erst nach float, dann nach int -> int(float("42.5"))


# =============================================================================
# NACH FLOAT CASTEN: float()
# =============================================================================
f1 = float(42)  # Integer wird zu Float -> 42.0
f2 = float("3.14")  # String mit Punkt wird zu Float -> 3.14
f3 = float("42")  # Auch Ganzzahl-Strings funktionieren -> 42.0
f4 = float("inf")  # Erzeugt den Spezialwert "Unendlich" -> inf
f5 = float(True)  # Boolean True wird zu -> 1.0

# ❌ FALLE: float("3,14") -> ValueError! (Python akzeptiert nur Punkte, keine Kommas)


# =============================================================================
# NACH STRING CASTEN: str()
# =============================================================================
s1 = str(42)  # Integer zu String -> "42"
s2 = str(3.14)  # Float zu String -> "3.14"
s3 = str(True)  # Boolean zu String -> "True"
s4 = str(None)  # None zu String -> "None"
# Hinweis: Fast jedes Objekt in Python kann über str() in Text verwandelt werden.


# =============================================================================
# DIE HÄUFIGSTEN KLAUSUR-ABSTÜRZE (ValueError)
# =============================================================================
try:
    int("Hallo")  # Text ohne Zahlen lässt sich nicht casten
except ValueError as e:
    print(f"Absturz 1: {e}")

try:
    int(
        "42 "
    )  # 💡 Achtung: Führende/nachfolgende Leerzeichen trimmt Python automatisch! (Funktioniert)
    int("4 2")  # Aber Leerzeichen MITTENDRIN stürzen ab
except ValueError as e:
    print(f"Absturz 2: {e}")
