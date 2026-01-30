from collections.abc import Callable
from functools import wraps


def validate_non_negative(func: Callable[[], int]) -> Callable[[], int]:
    @wraps(func)
    def wrapper() -> int:
        n = func()
        if n < 0:
            raise SystemExit("error: n must be non-negative")
        return n
    return wrapper

