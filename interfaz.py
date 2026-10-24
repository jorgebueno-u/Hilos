
import tkinter as tk
from tkinter import ttk, messagebox
from carrera import Carrera


class Ventana:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Competencia Automovilística")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        self.apuesta = tk.IntVar(value=1)
        self.rondas = tk.IntVar(value=3)
        self.carrera = None
        self.posiciones = [40] * 10

        self.canvas = tk.Canvas(
            self.root,
            width=900,
            height=450,
            bg="lightgreen"
        )
        self.canvas.pack(pady=10)

        colores = [
            "red", "blue", "green", "orange", "purple",
            "brown", "deeppink", "cyan", "gold", "gray"
        ]

        self.carros = []
        self.textos = []

        for i in range(10):
            y = 35 + i * 40

            self.canvas.create_rectangle(
                20, y - 17, 880, y + 17,
                fill="gray25",
                outline="white"
            )

            self.canvas.create_line(
                25, y + 19, 875, y + 19,
                fill="white",
                dash=(10, 8)
            )

            tag = f"carro{i + 1}"

            self.canvas.create_rectangle(
                35, y - 12, 70, y + 12,
                fill=colores[i],
                outline="black",
                tags=tag
            )

            self.canvas.create_polygon(
                70, y - 12,
                82, y - 5,
                82, y + 8,
                70, y + 12,
                fill=colores[i],
                outline="black",
                tags=tag
            )

            self.canvas.create_rectangle(
                49, y - 9, 65, y - 2,
                fill="lightblue",
                outline="black",
                tags=tag
            )

            self.canvas.create_oval(
                42, y + 7, 52, y + 17,
                fill="black",
                tags=tag
            )

            self.canvas.create_oval(
                68, y + 7, 78, y + 17,
                fill="black",
                tags=tag
            )

            self.canvas.create_text(
                58, y + 2,
                text=str(i + 1),
                fill="white",
                font=("Arial", 9, "bold"),
                tags=tag
            )

            self.carros.append(tag)

            texto = self.canvas.create_text(
                830, y,
                text="0/3",
                fill="white",
                font=("Arial", 9, "bold")
            )
            self.textos.append(texto)

        self.canvas.create_line(
            850, 15, 850, 435,
            fill="yellow",
            width=4
        )

        controles = tk.Frame(self.root)
        controles.pack(pady=10)

        ttk.Label(
            controles,
            text="Apostar por carro:"
        ).grid(row=0, column=0, padx=5)

        ttk.Combobox(
            controles,
            textvariable=self.apuesta,
            values=list(range(1, 11)),
            width=5,
            state="readonly"
        ).grid(row=0, column=1, padx=5)

        ttk.Label(
            controles,
            text="Vueltas:"
        ).grid(row=0, column=2, padx=5)

        ttk.Spinbox(
            controles,
            from_=1,
            to=20,
            textvariable=self.rondas,
            width=5
        ).grid(row=0, column=3, padx=5)

        self.slider = tk.Scale(
            controles,
            from_=1,
            to=10,
            orient="horizontal",
            label="Velocidad",
            command=self.cambiar_velocidad
        )
        self.slider.set(5)
        self.slider.grid(row=0, column=4, padx=5)

        self.boton = ttk.Button(
            controles,
            text="Iniciar carrera",
            command=self.iniciar
        )
        self.boton.grid(row=0, column=5, padx=5)

    def iniciar(self):
        if self.carrera is not None and self.carrera.corriendo:
            return

        try:
            vueltas = int(self.rondas.get())

            if vueltas < 1:
                raise ValueError

        except (ValueError, tk.TclError):
            messagebox.showerror(
                "Error",
                "Escribe un número válido de vueltas"
            )
            return

        for i in range(10):
            self.canvas.move(
                self.carros[i],
                40 - self.posiciones[i],
                0
            )

            self.posiciones[i] = 40

            self.canvas.itemconfig(
                self.textos[i],
                text=f"0/{vueltas}"
            )

        self.boton.config(state="disabled")

        self.carrera = Carrera(self, vueltas)
        self.carrera.velocidad_general = self.slider.get()
        self.carrera.iniciar()

    def actualizar_carro(self, numero, x, vueltas):
        self.root.after(
            0,
            self.dibujar_carro,
            numero,
            x,
            vueltas
        )

    def dibujar_carro(self, numero, x, vueltas):
        i = numero - 1

        self.canvas.move(
            self.carros[i],
            x - self.posiciones[i],
            0
        )

        self.posiciones[i] = x

        self.canvas.itemconfig(
            self.textos[i],
            text=f"{vueltas}/{self.rondas.get()}"
        )

    def cambiar_velocidad(self, valor):
        if self.carrera is not None and self.carrera.corriendo:
            self.carrera.velocidad_general = max(
                float(valor), 1
            )

    def mostrar_resultados(self, tiempos):
        orden = sorted(
            tiempos.items(),
            key=lambda elemento: elemento[1]
        )

        texto = "RESULTADOS FINALES\n\n"

        for puesto, (carro, tiempo) in enumerate(orden, 1):
            texto += (
                f"{puesto}. Carro {carro}: "
                f"{tiempo} segundos\n"
            )

        ganador = orden[0][0]

        if self.apuesta.get() == ganador:
            texto += "\n¡Ganaste la apuesta!"
        else:
            texto += f"\nGanó el carro {ganador}."

        self.root.after(
            0,
            lambda: self.finalizar(texto)
        )

    def finalizar(self, texto):
        self.boton.config(state="normal")
        messagebox.showinfo("Resultados", texto)

    def ejecutar(self):
        self.root.mainloop()
