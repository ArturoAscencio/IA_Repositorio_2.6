# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import numpy as np
import matplotlib.pyplot as plt

# Definir los valores posibles del dado (1 al 6)
valores = np.arange(1, 7)

# Definir las probabilidades de obtener cada valor en un dado justo
probabilidades = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# Crear un gráfico de barras para visualizar la distribución de probabilidad
plt.bar(valores, probabilidades, tick_label=valores)
plt.xlabel('Valor del Dado')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad de un Dado de 6 Caras')

# Mostrar el gráfico
plt.show()
