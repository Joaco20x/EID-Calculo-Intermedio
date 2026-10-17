# EID-Cálculo-Intermedio

> Proyecto de visualización matemática con **Manim** sobre el infinito en la definición de integral.

## Curso

- **Asignatura:** Cálculo Intermedio
- **Sección:** 1

## Integrantes y cuentas

| Integrante | Cuenta de GitHub |
|---|---|
| Joaquín Valenzuela | [@Joaco20x](https://github.com/Joaco20x) |
| Gabriel Gutiérrez | [@Gabrielgutierrez1](https://github.com/Gabrielgutierrez1) |
| Ailyn Melillan | [@AilynMelillan](https://github.com/AilynMelillan) |

## Tema

**El infinito en la definición de integral.**

## Pregunta central

> ¿Qué significa realmente hacer n → ∞ y por qué no se "sustituye" n por infinito?

## Versiones

- **Python:** 3.14.7
- **Manim:** 0.21.0

## Dependencias

Instalar con:

```bash
pip install manim==0.21.0
```

## Estructuras de carpetas

```text
EID-Calculo-Intermedio/
├── README.md
├── main.py
└── escenas/
    ├── __init__.py
    ├── presentacion.py
    ├── r1_rectangulos_fijos.py
    ├── r2_refinamiento.py
    ├── r3_limite_proceso.py
    └── creditos.py
```

### Descripción de los archivos

* **`README.md`**: documentación general del proyecto, sus objetivos e instrucciones de ejecución.
* **`main.py`**: escena `ProyectoIntegral`, que reúne presentación, R1, R2, R3 y créditos en un solo video.
* **`escenas/`**: directorio que contiene las escenas desarrolladas con Manim.
  * **`presentacion.py`**: tema y pregunta central del proyecto.
  * **`r1_rectangulos_fijos.py`**: visualización de la suma de Riemann por punto medio con \(n=4\).
  * **`r2_refinamiento.py`**: animación del refinamiento de los rectángulos y la aproximación de la suma.
  * **`r3_limite_proceso.py`**: representación de la convergencia de las sumas de Riemann y explicación del límite \(n\to\infty\).
  * **`creditos.py`**: integrantes y fuentes del proyecto, con títulos y autores sin enlaces en pantalla.

## Instrucciones de ejecución

1. Clonar el repositorio:

```bash
   git clone https://github.com/Joaco20x/EID-Calculo-Intermedio.git
   cd EID-Calculo-Intermedio
```

2. Crear y activar un entorno virtual:

```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux / macOS
   .venv\Scripts\activate         # Windows
```

3. Instalar las dependencias:

```bash
   pip install manim==0.21.0
```

4. Renderizar una escena (calidad baja, con vista previa):

```bash
   manim -pql [archivo].py [NombreEscena]
```

### Video completo

Desde la raíz del proyecto, con el entorno virtual activado:

```bash
manim -pql main.py ProyectoIntegral
```

Ejecuta la presentación, R1 (rectángulos fijos), R2 (refinamiento), R3 (límite)
y los créditos, en ese orden,
con un desvanecimiento de un segundo entre escenas. Las escenas también
pueden renderizarse individualmente con sus comandos originales.

Para exportar el conjunto en 1080p a 60 fps:

```bash
manim -qh main.py ProyectoIntegral
```

El archivo resultante es `media/videos/main/1080p60/ProyectoIntegral.mp4`.
El render incluye la presentación y los créditos; la voz se agrega al montaje final.
La duración comprobada en calidad baja es de aproximadamente **5 minutos y 40 segundos**,
dentro del máximo de 6 minutos.

### Presentación

La escena dura 12 segundos, sin audio, y muestra el tema y la pregunta central.
El video completo añade un segundo de desvanecimiento antes de comenzar R1.

```bash
manim -pql escenas/presentacion.py Presentacion
```

### Créditos

La escena dura 32 segundos y muestra integrantes, fuentes matemáticas,
material docente y herramientas en tres pantallas, sin enlaces.

```bash
manim -pql escenas/creditos.py Creditos
```

Fuentes utilizadas:

- *Cálculo volumen 1* (OpenStax) — G. Strang y E. Herman. Secciones 5.1 y 5.2.
- *Cálculo (Apex)* (LibreTexts) — G. Hartman y colaboradores. Secciones 5.2 y 5.3.
- *Introducción a la integral* — Universidad Católica de Temuco.
- *Este teorema lo cambió todo | ¿Qué es la integral? El famoso nexo entre derivadas e integrales* — BlueDot.
- *Manim Community Documentation* — Manim Community Developers.

Declaración de inteligencia artificial: se utilizó ChatGPT (OpenAI) como apoyo
para investigar conceptos matemáticos, organizar contenidos y revisar
explicaciones y código. Según el registro de fuentes del equipo, la verificación
se realizó contrastando las fuentes académicas citadas y comprobando los cálculos
y las animaciones desarrolladas.

### R2: refinamiento por punto medio

La escena es autocontenida y dura **60 segundos, sin audio**. Es un segmento
del video grupal de 4 a 6 minutos; las pausas permiten incorporar la voz al editar.

```bash
manim -pql escenas/r2_refinamiento.py R2Refinamiento
```

Guía sugerida de narración (ajustar al ritmo de quien grabe):

| Tiempo | Narración |
|---|---|
| 0–12 s | Aproximamos el área bajo la curva x al cuadrado más uno, entre cero y dos. Dividimos el intervalo en partes iguales y usamos el punto medio para calcular cada altura. |
| 12–24 s | Con dos rectángulos, el ancho es uno. Los puntos medios son cero coma cinco y uno coma cinco. Sus alturas son uno coma veinticinco y tres coma veinticinco: la suma de áreas es cuatro coma cinco. |
| 24–31 s | Con cuatro rectángulos, el ancho se reduce a la mitad. La suma aumenta a cuatro coma seiscientos veinticinco y el error disminuye. |
| 31–38 s | Con ocho, los rectángulos son más estrechos. La tabla conserva los resultados para comparar cómo mejora esta aproximación. |
| 38–48 s | Con dieciséis, la suma se acerca todavía más a catorce tercios. Sigue siendo una aproximación: el error es pequeño, pero positivo. |
| 48–60 s | Cada suma utiliza una cantidad finita de rectángulos. Tender a infinito significa estudiar cómo se comportan las sumas al aumentar n sin límite. Esta animación ilustra el proceso; la justificación matemática viene al estudiar el límite. |

Para el montaje final, renderizar en 1080p a 60 fps:

```bash
manim -qh escenas/r2_refinamiento.py R2Refinamiento
```

El MP4 se guarda en `media/videos/r2_refinamiento/1080p60/`.
La carpeta `media/` se genera localmente y está excluida de Git.
