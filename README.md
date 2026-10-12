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
| Aylin Melillan | — | [@AilynMelillan](https://github.com/AilynMelillan) |

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
├── comun.py
└── escenas/
    ├── __init__.py
    ├── r1_rectangulos_fijos.py
    ├── r2_refinamiento.py
    └── r3_limite_proceso.py
```

### Descripción de los archivos

* **`README.md`**: documentación general del proyecto, sus objetivos e instrucciones de ejecución.
* **`main.py`**: punto de entrada principal del proyecto
* **`escenas/`**: directorio que contiene las escenas desarrolladas con Manim.
  * **`r1_rectangulos_fijos.py`**: visualización de la suma de Riemann izquierda con \(n=4\).
  * **`r2_refinamiento.py`**: animación del refinamiento de los rectángulos y la aproximación de la suma.
  * **`r3_limite_proceso.py`**: representación de la convergencia de las sumas de Riemann y explicación del límite \(n\to\infty\).

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
