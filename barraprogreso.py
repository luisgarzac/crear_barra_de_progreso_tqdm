# Creamos una barra de progreso en Python
# Importamos las librerías tqdm y time
from tqdm import tqdm
from time import sleep

# Hacemos un iterable dentro de tqdm(). Podemos personalizar la barra utilizando sus funciones.
# desc -> 'texto', total -> 'número de iteraciones', colour -> 'color'
for i in tqdm(range(int(100)), desc = "Progreso", total = 100, colour = 'green'):
    sleep(.1) # sleep trabaja en segundos / (.1) -> 100 milisegundos (ms)

print("Proceso terminado")