try:
    n = int("no-number")
    print(f" {n=}")
except ValueError as e:
    print(f" => value error: {e}")
    # raise                             # if you want to raise it again

try:
    n = int("12")
except ValueError as e:
    print(f" => value error: {e}")
except (AssertionError, ArithmeticError) as e:
    print(f" => assertion error: {e}")
else:  # runs if the try block is successful
    print(" 3| everything was ok")
finally:
    print(" 4| in any case")

print(" 5| assert...", end="")
try:
    n = -1
    assert n > 0, f"n ({n}) is not positive"
except AssertionError as e:
    print(f" => assertion error: {e}")

print(" 6| division by 0...", end="")
try:
    n = int(1 / 0)
    print(f" {n=}")
except Exception as e:  # pylint: disable=broad-exception-caught
    print(f" => unknown error: {e}")  # optional: e.with_traceback()

print(" 7| raise by myself...", end="")
try:
    raise RuntimeError("something is wrong")
except RuntimeError as e:
    print(f" => runtime error: {e}")
