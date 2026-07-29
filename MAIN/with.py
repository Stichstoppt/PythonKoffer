import time


def foo(): ...


# ============================
# class context manager
# ============================
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        print("start")
        return self  # so that "as" works

    def __exit__(self, *args):  # args needed but unused, see below
        elapsed = time.perf_counter() - self.start
        print(f"stop: {elapsed=:0.4f}s")


with Timer():
    foo()


"""
exc = exception
def __exit__(self, exc_type, exc_value, exc_tb):        # _tb traceback
    if isinstance(exc_value, IndexError):
        print(f">>>>>>>>>> IndexError... Really? Again?")
        print(f"           block: {exc_type}")
        print(f"<<<<<<<<<< message: {exc_value}")
        return True                 # 'swallow' exceptions
    return False                    # technically not necessary
"""


# ============================
# function context manager
# ============================
from contextlib import contextmanager


@contextmanager
def datei_oeffner(dateiname):
    f = open(dateiname, "w")
    try:
        yield f  # Gibt die Datei an den with-Block
    finally:
        f.close()  # Garantiert, dass die Datei IMMER geschlossen wird, selbst bei Fehlern!


# ================================
# class context manager with close
# ================================

from contextlib import closing, contextmanager


class Resource:
    def close(self):
        print("cleaning happens here")


with closing(Resource()) as res:
    print(f"    type res: {type(res)}")
