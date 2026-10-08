# app.py
import tkinter as tk
from tkinter import simpledialog, messagebox


# La clase hereda de tk.Tk, por lo que la propia clase es la ventana principal
class NotasApp(tk.Tk):

    def __init__(self):
        # Inicializa la ventana base de Tkinter
        super().__init__()

        # Configuración de la ventana (título y tamaño inicial)
        self.title("Notas Rápidas (Tkinter)")
        self.geometry("600x380")

        # Variable para controlar el tema que se está mostrando:
        # El programa inicia con el tema claro
        self.tema_oscuro = False

        # Variable de control del contador 
        self.var_contador = tk.StringVar(value="0 notas")

        # Campo de entrada donde el usuario escribe la nota
        self.input = tk.Entry(self)
        self.input.pack(fill="x", padx=8, pady=8)

        # Evento de teclado: presionar enter agrega la nota
        self.input.bind("<Return>", lambda e: self.agregar())

        # Contenedor para los botones y el contador
        frame_btns = tk.Frame(self)
        frame_btns.pack(fill="x", padx=8)

        # Botón agregar al hacer clic ejecuta el método agregar
        tk.Button(frame_btns,text="Agregar",command=self.agregar).pack(side="left")

        # Botón eliminar al hacer clic ejecuta el método eliminar
        tk.Button(frame_btns,text="Eliminar",command=self.eliminar).pack(side="left", padx=6)

        # Botón para cambiar el tema
        self.btn_tema = tk.Button(frame_btns,text="Tema oscuro",command=self.cambiar_tema)
        self.btn_tema.pack(side="left", padx=6)

        # Etiqueta que muestra la cantidad de notas
        tk.Label(frame_btns,textvariable=self.var_contador).pack(side="left", padx=12)

        # Lista visual donde se muestran las notas
        self.lista = tk.Listbox(self)
        self.lista.pack( fill="both", expand=True, padx=8, pady=8)

        # Doble clic para editar una nota
        self.lista.bind("<Double-Button-1>",self.editar_item)

        # Lista interna con los textos de las notas
        self.notas = []

        # Muestra el contador inicial
        self.actualizar_contador()

        # Aplica el tema inicial el claro
        self.aplicar_tema()


    # Método que se ejecuta al presionar el botón de tema
    def cambiar_tema(self):
        # Alterna el tema de claro a oscuro
        self.tema_oscuro = not self.tema_oscuro

        # Pinta la interfaz con el tema que quedó activado
        self.aplicar_tema()


    # Método que pinta todos los widgets según el tema actual
    def aplicar_tema(self):

        if self.tema_oscuro:
            # Colores del tema oscuro
            fondo = "#2b2b2b"
            texto = "white"
            seleccion = "#505050"
            # El botón ofrece volver al tema claro
            self.btn_tema.config(text="Tema claro")

        else:
            # Colores del tema claro
            fondo = "white"
            texto = "black"
            seleccion = "#cce5ff"
            # El botón ofrece pasar al tema oscuro
            self.btn_tema.config(text="Tema oscuro")

        # Cambia el color de la ventana principal
        self.config(bg=fondo)

        # Recorre los widgets de la ventana para cambiar sus colores
        for widget in self.winfo_children():

            # Si es un contenedor (Frame), se pinta junto con lo que tiene dentro
            if isinstance(widget, tk.Frame): 
                widget.config(bg=fondo)

                for elemento in widget.winfo_children():
                    # A las etiquetas les cambia el fondo y color de letra
                   if isinstance(elemento, tk.Label):elemento.config(bg=fondo, fg=texto)

                    # A los botones les cambia el fondo, letra y colores al pasar o presionar
                   elif isinstance(elemento, tk.Button):elemento.config(bg=fondo,fg=texto,activebackground=seleccion,activeforeground=texto)

            #A los campo de textos les cambia el fondo, letra y color del cursor
            elif isinstance(widget, tk.Entry): widget.config(bg=fondo,fg=texto,insertbackground=texto)

            # A la Lista de notas le cambia el fondo, letra y colores de la selección
            elif isinstance(widget, tk.Listbox):widget.config(bg=fondo,fg=texto,selectbackground=seleccion,selectforeground=texto)

    # Metodo que cuenta las notas y actualiza el texto de la etiqueta
    def actualizar_contador(self):
        n = len(self.notas)
        self.var_contador.set(f"{n} nota" if n == 1 else f"{n} notas")


    def agregar(self):
        # Se obtiene el texto escrito y elimina espacios
        texto = self.input.get().strip()

        # Se agrega si el texto no está vacío
        if texto:
            # Guarda la nota en la lista interna y la muestra en la lista visual
            self.notas.append(texto)
            self.lista.insert("end", texto)

            # Limpia el campo de texto y actualiza el contador
            self.input.delete(0, "end")
            self.actualizar_contador()


    def eliminar(self):
        # Se obtiene los índices seleccionados
        sel = self.lista.curselection()

        # Si no hay selección, avisa al usuario
        if not sel:
            messagebox.showinfo("Eliminar", "Selecciona una nota.")
            return

        # Elimina la nota seleccionada de la lista visual y de la interna
        idx = sel[0]
        self.lista.delete(idx)
        self.notas.pop(idx)

        # Actualiza el contador
        self.actualizar_contador()


    def editar_item(self, event=None):
        # Se obtiene la nota seleccionada
        sel = self.lista.curselection()

        # Si no hay nota seleccionada, no hace nada
        if not sel:
            return

        # Guarda la posición y el texto actual de la nota
        idx = sel[0]
        actual = self.notas[idx]

        # Habla para editar el texto 
        nuevo = simpledialog.askstring("Editar nota", "Nuevo texto:", initialvalue=actual)

        # Guarda el cambio si el texto es válido
        if nuevo and nuevo.strip():
            # Actualiza la lista interna y reemplaza el elemento en la lista visual
            self.notas[idx] = nuevo.strip()
            self.lista.delete(idx)
            self.lista.insert(idx, nuevo.strip())


# Crea la ventana y la mantiene abierta
if __name__ == "__main__":
    NotasApp().mainloop()