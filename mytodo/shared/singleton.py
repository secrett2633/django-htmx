from threading import Lock
from typing import Any


class Singleton:
    _instance = None
    _lock: Lock = Lock()

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        with cls._lock:
            if not isinstance(cls._instance, cls):
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance