
import threading
import random
import time


class Vehiculo(threading.Thread):

    def __init__(self, numero, carrera):
        super().__init__()
        self.numero = numero
        self.carrera = carrera
        self.velocidad = random.randint(3, 8)

    def run(self):
        while (
            self.carrera.corriendo
            and self.carrera.vueltas[self.numero - 1] < self.carrera.rondas
        ):
            velocidad = max(self.carrera.velocidad_general, 1)

            time.sleep(0.03 / velocidad)

            self.carrera.mover(self.numero, self.velocidad)

            self.velocidad = random.randint(3, 8)

        self.carrera.terminar(self.numero)
