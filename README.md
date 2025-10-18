# Funciones Graficadas

Este proyecto permite escribir una función matemática en Python y graficarla automáticamente con Manim. La idea es simple: escribes la función que quieras, el programa la interpreta y genera una animación en alta calidad mostrando su forma, los ejes con valores y los puntos donde cruza las rectas.

## Cómo funciona

Al ejecutar el programa, pide una función en términos de x. Usa Manim para crear una escena donde se grafica la función y guarda el resultado como un video en la ruta configurada.

Ejemplo:
python main.py
> Ingresa la función (en x): sen(x) * exp(-x**2/5)

## Requisitos

Python 3.10 o superior  
ManimCE instalado  
LaTeX (necesario para mostrar los números en los ejes)

Instalación rápida:
pip install manim

Si estás en Windows, asegúrate de tener MiKTeX o TeX Live instalado.

## Estructura del proyecto

C:\Coding\Funciones graficadas
│
├── main.py  
└── grafica.mp4

## Personalización

Puedes ajustar los límites de los ejes (x_range, y_range), modificar la velocidad o el color de la animación y cambiar la calidad del video (por ejemplo, high_quality, fourk_quality).

## Ejemplos de funciones

sen(x) * exp(-x**2/5)  
cos(x/2) + sen(x)**2  
(x**3 - 3*x) * exp(-x**2/10)

## Salida

El video generado se guarda automáticamente en:
C:\Coding\Funciones graficadas\grafica.mp4
