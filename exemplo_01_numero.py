import random
import time 
from meu_decorador import decorador_maik

@decorador_maik
def gerar_numero_aleatorio():
    return random.randint(1,10)
    print(num)

if __name__ == "__main__":
    while True:
        num = gerar_numero_aleatorio()
        print(num)
        time.sleep(1)