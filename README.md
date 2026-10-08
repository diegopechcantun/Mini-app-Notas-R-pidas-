# Notas Rápidas — Práctica 203: GUI y Manejo de Eventos
---
## Integrantes

- **Balam Castillo Pedro**
- **Pech Cantun Diego**
- **Loreto Huerta Filiberto**
---

## Proyecto Académico
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

## Uso

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
| Ratón (MouseEvent) | `<Double-Button-1>` | Lista | `editar_item()` | Abre diálogo para editar la nota |

---
##  Funcionamiento
* `Lee números desde datos.txt`
*  `Ordena todos los números en forma ascendente.`
*  `Escribe los números ordenados en un archivo nuevo llamado datos_ordenados.txt`
*  `Crea una tabla hash de 100,003 cubetas. Cada número se almacena con su índice original usando la función: posición = número % 100003.`
* `El usuario ingresa un número o ingresa varios  números y el programa lo busca en la tabla hash, retornando todas las posiciones donde aparece.`
---

## Estructura del Repositorio
```
Búsqueda por Funciones Hash
│
├── metodo_hash.py
├── datos.txt
├── datos_ordenados.txt
└── README.md

```
---
## Video explicativo del codigo

### Video subido a YouTube 

[![Ver demostración del proyecto](https://img.shields.io/badge/▶%20Ver%20Video-Explicación-red?style=for-the-badge&logo=youtube)](https://youtu.be/aucYYLKTMn8)

---
## Análisis de Complejidad

El rendimiento de la búsqueda en una tabla hash depende principalmente de la función hash utilizada y de la cantidad de colisiones que se generen. En esta implementación, la clave se transforma para obtener un índice directo dentro de la tabla. 

### Complejidad Temporal

| Caso | Complejidad | Descripción |
|------|-------------|-------------|
| **Mejor caso** | **O(1)** |  El tiempo de búsqueda es constante, independientemente del tamaño de los datos. |
| **Caso promedio** | **O(1)** |Con una buena función hash, los datos se distribuyen correctamente y las colisiones son mínimas |
| **Peor caso** | **O(n)** |Ocurre cuando todos los elementos generan el mismo hash (mala función hash o muchas colisiones).|

### Complejidad del espacio

La complejidad espacial de una tabla hash es de O(n), donde n es la cantidad de elementos almacenados. 

Esto se debe a que cada elemento necesita espacio en la estructura principal y, en caso de colisiones, también puede ocupar espacio adicional en las listas internas. Sin embargo, este crecimiento es lineal y controlado, ya que cada elemento se almacena una sola vez dentro de la estructura.


---
## Casos de Uso

### Cuándo usar HASH

- Cuando se requiere un acceso rápido a los elementos basado en claves únicas. 
- En compiladores y intérpretes, la búsqueda hash se emplea para buscar rápidamente identificadores y variables.
- La búsqueda hash permite un acceso rápido a los datos almacenados en caché.
- Las funciones hash se utilizan en la generación de huellas digitales y firmas digitales.

### Cuándo no usar HASH

- Datos que requieren orden específico.
- Memoria muy limitada.
- Se necesita acceso ordenado por clave mínima o máxima.
- Cuando necesitas operaciones de rango o secuenciales.
---


## Comparativa Teórica: Búsqueda Hash vs Búsqueda Binaria


| Característica       |         Hash        |     Búsqueda Binaria  |
|----------------------|---------------------|-----------------------|
| Complejidad Promedio | O(1)                | O(log n)              |
| Complejidad Promedio | O(n)                | O(log n)              |
| Requiere Orden       | No                  | Sí                    |
| Espacio Extra        | O(n)                | O(1)                  |
| Mejor Para           | Búsquedas frecuentes| Datos ordenados, rango|
#### **Análisis**


* `Búsqueda Binaria:` Divide el espacio de búsqueda por la mitad repetidamente, comparando el elemento objetivo con el punto medio. Requiere que los datos estén previamente ordenados.

* ` Búsqueda Hash:`  Calcula un índice mediante una función hash, permitiendo acceso directo a los datos. Realiza un acceso aleatorio al almacenamiento mediante transformación de clave.
  

---


## Comparativa Teórica: Búsqueda Hash vs Búsqueda Secuencial


| Característica       |         Hash        |  Búsqueda Secuencial  |
|----------------------|---------------------|-----------------------|
| Complejidad Promedio | O(1)                |   O(n)                |
| Complejidad Peor caso| O(n)                |   O(n)                |
| Requiere Orden       | No                  |   No                  |
| Espacio Extra        | O(n)                |   O(1)                |
| Mejor Para           | Búsquedas frecuentes|  Datos sin ordenar    |


**Análisis**

* `Búsqueda Secuencial:` Examina cada elemento uno por uno desde el inicio hasta encontrar el objetivo o agotar la colección. Requiere múltiples comparaciones y accesos secuenciales.

* `Búsqueda Hash:` 
Obtiene el índice directamente mediante función hash. Un acceso de O(1) en promedio, sin necesidad de comparaciones múltiples.


---
