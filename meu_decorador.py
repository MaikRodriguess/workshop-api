import time
from functools import wraps

def decorador_maik(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            print("Faço muita coisa")
            time.sleep(1)
            result = func(*args, **kwargs)
            return result
    return wrapper
