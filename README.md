# Tarea 1 – Procesos Estocásticos

Aqui dejo los codigos que se tienen que ejecutar para ver resuelta la tarea.

## Archivos:

### random_telegraph.py
Simulación del proceso dicotómico (Random Telegraph Process).

### toggle_switch.py
Simulación estocástica del toggle switch usando el algoritmo de Gillespie.

### langevin_magnetic.py
Simulación de la ecuación de Langevin para una partícula en un campo magnético.

## Para ejecutar los códigos utilice:

- numpy
- matplotlib

### Instalar:
```bash
pip install numpy matplotlib
```

### Ejecutar:
```bash
python nombre_del_archivo.py
```

---

## Problema 1 – Dichotomic Markov process

Simulación del proceso dicotómico (Random Telegraph Process). Este proceso alterna entre dos estados (+1 y -1) con tiempos de espera exponencialmente distribuidos.

```python
import numpy as np
import matplotlib.pyplot as plt

gamma = 1.0
Tmax = 20

t = 0
y = 1

times = [t]
states = [y]

while t < Tmax:
    tau = -np.log(np.random.rand()) / gamma
    t += tau
    y = -y
    
    times.append(t)
states.append(y)

plt.step(times, states)
plt.xlabel("t")
plt.ylabel("Y(t)")
plt.title("Random Telegraph Process")
plt.show()
```