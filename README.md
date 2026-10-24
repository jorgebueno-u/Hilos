markdown
# Simulador de Competencia Automovilística con Hilos en Python

Este proyecto consiste en una aplicación gráfica interactiva que simula una carrera de 10 vehículos concurrentes utilizando **programación multihilo (Threading)** y la biblioteca **Tkinter** para la interfaz gráfica en Python. Desarrollado como práctica de laboratorio para la asignatura de Programación III de la Universidad Militar Nueva Granada.

## 🚀 Características

- **Concurrencia Real:** Cada uno de los 10 vehículos se ejecuta de manera independiente en su propio hilo de ejecución (`threading.Thread`).
- **Velocidades Aleatorias:** Los automóviles avanzan a ritmos dinámicos e impredecibles calculados en tiempo real con el módulo `random`.
- **Panel de Configuración:** Control interactivo para definir el número de idas y vueltas (rondas) de la competencia.
- **Sistema de Apuestas:** Permite al usuario seleccionar un vehículo antes del inicio y validar si su predicción coincide con el ganador.
- **Control del Tiempo General:** Incorpora un *slider* dinámico que acelera o desacelera el paso del tiempo en la simulación.
- **Tabla de Resultados:** Al concluir la carrera, despliega un orden jerárquico preciso del primer al último puesto según los tiempos exactos de ejecución.

## 🛠️ Estructura del Proyecto

El código está estructurado bajo el paradigma de la Programación Orientada a Objetos (POO):

- `main.py`: Punto de entrada que inicializa y lanza la aplicación.
- `carrera.py`: Contiene la lógica del negocio, control de estados de la competencia y sincronización de hilos.
- `vehiculo.py`: Define la clase `Vehiculo` (heredera de `threading.Thread`), encargada del movimiento individual y registro del tiempo.
- `interfaz.py`: Administra toda la renderización de la pista de carreras, las imágenes de los vehículos y los widgets de control en Tkinter.

## 💻 Requisitos

- Python 3.x
- Biblioteca estándar de Tkinter (incluida en las distribuciones oficiales de Python)

## 🔧 Instalación y Ejecución

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Hilos
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## 👥 Autores
- **Jorge Bueno** - *Estudiante de Ingeniería Mecatrónica* - [jorgebueno-u](https://github.com/jorgebueno-u)
- **Miguel Duran** - *Estudiante de Ingeniería Mecatrónica*
