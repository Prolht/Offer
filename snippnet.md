### 线程安全地单例模式
```py
import threading
class Singleton:
    _instance_lock = threading.Lock()
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._intance = object.__new__(cls)
        return Singleton._instance
```