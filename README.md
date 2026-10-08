#  Mini-app "Notas Rápidas" — Práctica 203: GUI y Manejo de Eventos
---
## Integrantes

- **Balam Castillo Pedro**
- **Pech Cantun Diego**
- **Loreto Huerta Filiberto**
---

## Practica Académica
- Institución: Instituto Tecnológico de Mérida
- Materia: Tópicos Avanzados de Programación
- Carrera: Ingeniería en Sistemas Computacionales

---

## Descripción  
En esta práctica se desarrolla una aplicación de escritorio con interfaz gráfica en Python, usando Tkinter y su módulo ttk. La aplicación, llamada Notas Rápidas, permite al usuario escribir notas, agregarlas a una lista, editarlas y eliminarlas, mientras un contador muestra cuántas notas hay.

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

1. Descargar o copiar el archivo `notas_rapidas.py` en una carpeta de tu computadora.
2. Abrir el archivo con Visual studio Code ya que soporta Python.
3. Ejecutar el programa con el botón **Run** (o **Ejecutar**).
4. Se abrirá la ventana de **Notas Rápidas**, lista para usarse.
---

## Funcion

| Acción | Cómo hacerlo |
|---|---|
| Agregar nota | Escribe en el campo y pulsa **Agregar** o la tecla **Enter** |
| Editar nota | **Doble clic** sobre la nota en la lista |
| Eliminar nota | Selecciónala y pulsa **Eliminar** (o la tecla **Supr**) |
| Cambiar tema | Pulsa el botón **Tema claro o Tema oscuro** |

---
## Eventos manejados

| Tipo | Evento | Widget | Manejador | Resultado |
|---|---|---|---|---|
| Botón (ActionEvent) | `command=` | Botón *Agregar* | `agregar()` | Agrega la nota a la lista |
| Botón (ActionEvent) | `command=` | Botón *Eliminar* | `eliminar()` | Elimina la nota seleccionada |
| Botón (ActionEvent) | `command=` | Botón *Tema* | `cambiar_tema()` | Alterna entre tema claro y oscuro |
| Teclado (KeyEvent) | `<Return>` | Campo de texto | `agregar()` | Agrega la nota con Enter |
| Teclado (KeyEvent) | `<Delete>` | Lista | `eliminar()` | Elimina la nota seleccionada |
| Ratón (MouseEvent) | `<Double-Button-1>` | Lista | `editar_item()` | Abre el diálogo para editar la nota |

---

## Extensión: Tema claro/oscuro

Los colores de cada tema están definidos en el diccionario TEMAS. El método `aplicar_tema()` los aplica con `ttk.Style` (tema base `clam`) a los widgets `ttk` y de forma directa al `Listbox`, que no tiene versión `ttk`. El botón de tema alterna entre ambos y muestra el nombre del tema al que se cambiará.

---

## Entregables

- Código fuente funcional (Java y/o Python).
- Capturas de pantalla en ejecución.
- README

