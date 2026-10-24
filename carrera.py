
import time
from vehiculo import Vehiculo


class Carrera:

    def __init__(self, gui, rondas):
        self.gui = gui
        self.rondas = rondas
        self.pos = [40] * 10
        self.vueltas = [0] * 10
        self.velocidad_general = 5
        self.corriendo = True
        self.tiempo = {}
        self.inicio = 0
        self.hilos = []

    def iniciar(self):
        self.inicio = time.time()

        for i in range(1, 11):
            hilo = Vehiculo(i, self)
            self.hilos.append(hilo)
            hilo.start()

    def mover(self, numero, pasos):
        i = numero - 1
        self.pos[i] += pasos

        if self.pos[i] >= 850:
            self.pos[i] = 40
            self.vueltas[i] += 1

        self.gui.actualizar_carro(
            numero,
            self.pos[i],
            self.vueltas[i]
        )

    def terminar(self, numero):
        if numero not in self.tiempo:
            self.tiempo[numero] = round(
                time.time() - self.inicio, 2
            )

        if len(self.tiempo) == 10:
            self.corriendo = False
            self.gui.mostrar_resultados(self.tiempo)
