#  Mini-app "Notas Rápidas" — Práctica 203: GUI y Manejo de Eventos
---
## Practica Académica
- Institución: Instituto Tecnológico de Mérida
- Materia: Tópicos Avanzados de Programación
- Carrera: Ingeniería en Sistemas Computacionales

---
## Integrantes

- **Balam Castillo Pedro**
- **Pech Cantun Diego**
- **Loreto Huerta Filiberto**
---

## Descripción  
En esta práctica se desarrolla una aplicación de escritorio con interfaz gráfica en Python, usando la biblioteca Tkinter. La aplicación, llamada Notas Rápidas, permite al usuario escribir notas, agregarlas a una lista, editarlas y eliminarlas, mientras un contador muestra cuántas notas hay.

El propósito es practicar la programación orientada a eventos: la aplicación reacciona a las acciones del usuario, como hacer clic en un botón, presionar una tecla o dar doble clic sobre un elemento de la lista. Para ello se enlazan estos eventos con métodos de una clase que concentra la lógica de la ventana, siguiendo buenas prácticas de nombres, organización y comentarios.

Como extensión, se agregó la opción de cambiar entre un tema claro y uno oscuro desde un botón de la propia interfaz.

---
## Objetivos

- Construir una ventana con controles básicos (botón, campo de texto, selectores).
- Identificar y manejar `ActionEvent`, `KeyEvent` y `MouseEvent` (o equivalentes en Tkinter).
- Encapsular la lógica de eventos siguiendo buenas prácticas (controladores/listeners).

---
## Insumos y requisitos

- **Python:** 3.10 o superior, con Tkinter incluido (viene con el instalador oficial de Python).
- (Opcional) un entorno virtual `venv`.
- Conocimientos básicos de POO y de estructura de proyectos.
  
---
## Dependencias

No requiere instalar paquetes externos. Solo necesita Python 3.10 o superior, que ya incluye las bibliotecas estándar utilizadas: Tkinter y ttk.

---
## Cómo ejecutar

1. Descargar o copiar el archivo `app.py` (carpeta notas_tk) en una carpeta de tu computadora.
2. Abrir el archivo con Visual Studio Code ya que soporta Python.
3. Ejecutar el programa con el botón **Run** (o **Ejecutar**).
4. Se abrirá la ventana de **Notas Rápidas**, lista para usarse.
---

## Funciones

| Acción | Cómo hacerlo |
|---|---|
| Agregar nota | Escribe en el campo y pulsa Agregar o la tecla Enter |
| Editar nota | Doble clic sobre la nota en la lista |
| Eliminar nota | Selecciónala y pulsa Eliminar |
| Cambiar tema | Pulsa el botón Tema claro o Tema oscuro|

---
## Eventos manejados

| Tipo | Evento | Widget | Manejador | Resultado |
|---|---|---|---|---|
| Botón (ActionEvent) | `command=` | Botón *Agregar* | `agregar()` | Agrega la nota a la lista |
| Botón (ActionEvent) | `command=` | Botón *Eliminar* | `eliminar()` | Elimina la nota seleccionada |
| Botón (ActionEvent) | `command=` | Botón *Tema* | `cambiar_tema()` | Alterna entre tema claro y oscuro |
| Teclado (KeyEvent) | `<Return>` | Campo de texto | `agregar()` | Agrega la nota con Enter |
| Ratón (MouseEvent) | `<Double-Button-1>` | Lista | `editar_item()` | Abre el diálogo para editar la nota |

---

## Extensión: Tema claro/oscuro
---
El programa inicia con el tema claro, el botón de tema alterna entre claro y oscuro, así que el método cambiar_tema() invierte la variable tema_oscuro y aplicar_tema() cambia los colores de la ventana, el campo de texto, los botones, la etiqueta y la lista de notas. El texto del botón indica el tema al que se cambiará con el siguiente clic.
---

## Entregables

- Código fuente funcional en Python (notas_tk/app.py).
- Capturas de pantalla en ejecución.
- README

