"""Suma de Riemann por punto medio con un número fijo de rectángulos (n = 4).

Ejecutar desde la raíz del proyecto:
    manim -pql escenas/r1_rectangulos_fijos.py R1RectangulosFijos

Escena autocontenida: no importa otras escenas del proyecto.
Duración: 2:56 (176 s)

Objetivo (escenas/objetivo.txt):
    Representar f(x) = x² + 1 en [0, 2], dividir el intervalo en cuatro
    subintervalos, construir un rectángulo por subintervalo tomando la altura
    en su punto medio y mostrar que la suma de las áreas (S_4 = 4,625)
    aproxima el área bajo la curva.
"""

from manim import (
    BLUE, DOWN, GREEN, LEFT, RIGHT, UP, WHITE, YELLOW,
    Axes, BraceBetweenPoints, Create, DashedLine, Dot, FadeIn, FadeOut,
    MathTex, ReplacementTransform, Scene, Text, VGroup, Write,
)


class R1RectangulosFijos(Scene):
    """Aproximación por punto medio al área bajo f(x) = x² + 1 con n = 4."""

    def construct(self):
        a, b, n = 0, 2, 4
        area_exacta = 14 / 3

        def f(x):
            return x**2 + 1

        def decimal(valor, cifras=4):
            # Coma decimal agrupada para evitar el espacio de puntuación de TeX.
            texto = f"{valor:.{cifras}f}".rstrip("0").rstrip(".")
            return (texto or "0").replace(".", "{,}")

        dx = (b - a) / n
        medios = [a + (i + 0.5) * dx for i in range(n)]
        alturas = [f(x) for x in medios]
        areas = [altura * dx for altura in alturas]
        suma = sum(areas)  # 4.625

        # ------------------------------------------------------------------ texto
        titulo = Text(
            "Suma de Riemann por punto medio: n = 4", font_size=32,
        ).to_edge(UP)
        formula = MathTex(
            r"S_4=\sum_{i=0}^{3}f(x_i^*)\,\Delta x,"
            r"\qquad \Delta x=\frac{b-a}{n}=\frac{2}{4}=0{,}5",
            font_size=26,
        ).next_to(titulo, DOWN, buff=0.22)

        # -------------------------------------------------------------------- ejes
        ejes = Axes(
            x_range=[0, 2.25, 0.5],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=3.6,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 22},
        ).to_edge(LEFT, buff=0.65).shift(DOWN * 0.2)
        curva = ejes.plot(f, x_range=[a, b], color=YELLOW).set_z_index(4)
        nombre_curva = MathTex(
            r"f(x)=x^2+1", color=YELLOW, font_size=28,
        ).next_to(ejes.c2p(1.55, 4.7), UP, buff=0.1)
        ejes.set_z_index(3)

        # Cuatro subintervalos: divisiones verticales y llaves con el ancho.
        divisiones = VGroup(*[
            DashedLine(
                ejes.c2p(x, 0), ejes.c2p(x, f(x)),
                color=WHITE, stroke_width=1.5, stroke_opacity=0.45,
                dash_length=0.09,
            )
            for x in [a + i * dx for i in range(1, n)]
        ]).set_z_index(5)
        llaves = VGroup(*[
            BraceBetweenPoints(
                ejes.c2p(a + i * dx, 0) + DOWN * 0.5,
                ejes.c2p(a + (i + 1) * dx, 0) + DOWN * 0.5,
                direction=DOWN, color=BLUE,
            )
            for i in range(n)
        ])
        ancho = VGroup(
            llaves,
            MathTex(r"\Delta x=0{,}5", font_size=25, color=BLUE).next_to(
                llaves[0], DOWN, buff=0.06,
            ),
        )

        # Rectángulos (uno por subintervalo), alturas y puntos medios.
        rectangulos = ejes.get_riemann_rectangles(
            curva,
            x_range=[a, b],
            dx=dx,
            input_sample_type="center",
            color=[BLUE, GREEN, BLUE, GREEN],
            fill_opacity=0.55,
            stroke_width=1.2,
            stroke_color=WHITE,
            width_scale_factor=1,
        ).set_z_index(2)
        alturas_lineas = VGroup(*[
            DashedLine(
                ejes.c2p(x, 0), ejes.c2p(x, f(x)),
                color=BLUE, stroke_width=2, dash_length=0.07,
            )
            for x in medios
        ]).set_z_index(6)
        puntos = VGroup(*[
            Dot(ejes.c2p(x, f(x)), radius=0.04, color=BLUE)
            for x in medios
        ]).set_z_index(7)

        # --------------------------------------------------- tabla del lado derecho
        columnas = (1.65, 2.85, 4.35, 5.9)
        cabecera = VGroup(*[
            MathTex(texto, font_size=24).move_to(RIGHT * x + UP * 1.65)
            for texto, x in zip((r"i", r"x_i^*", r"f(x_i^*)", r"A_i"), columnas)
        ])
        filas = VGroup()
        for i in range(n):
            fila = VGroup(*[
                MathTex(valor, font_size=24).move_to(
                    RIGHT * x + UP * (1.05 - i * 0.5),
                )
                for valor, x in zip(
                    (
                        str(i),
                        decimal(medios[i], 2),
                        decimal(alturas[i], 4),
                        decimal(areas[i], 5),
                    ),
                    columnas,
                )
            ])
            filas.add(fila)

        etiqueta = MathTex(
            r"\text{Suma acumulada}=", font_size=26,
        ).move_to(RIGHT * 2.35 + DOWN * 1.15)
        valor = MathTex("0", font_size=26).next_to(etiqueta, RIGHT, buff=0.12)

        total = MathTex(
            r"S_4=4{,}625", font_size=38, color=GREEN,
        ).move_to(RIGHT * 3.9 + DOWN * 1.95)
        exacta = MathTex(
            r"\int_0^2(x^2+1)\,dx=\frac{14}{3}\approx4{,}6667",
            font_size=28, color=GREEN,
        ).move_to(RIGHT * 3.9 + DOWN * 2.7)
        nota = Text(
            "La suma de los cuatro rectángulos aproxima el área bajo la curva.",
            font_size=22,
        ).to_edge(DOWN, buff=0.18)

        # --------------------------------------------------------------- animación
        # Tiempos sincronizados con escenas/transcripcion.srt (duración 2:56).
        self.play(Write(titulo), run_time=3.5)                       # 0:00
        self.wait(2.5)                                               # 0:03,5
        # f(x) = x² + 1 sobre [0, 2].
        self.play(                                                    # 0:06
            Create(ejes), Create(curva), Write(nombre_curva), run_time=7.5,
        )
        self.wait(11.5)                                              # 0:13,5
        # Fórmula de la suma de Riemann y del ancho Δx.
        self.play(Write(formula), run_time=6.0)                      # 0:25
        # Dividir [0, 2] en cuatro subintervalos y mostrar Δx = 0,5.
        self.play(                                                    # 0:31
            Create(divisiones), Create(llaves), Write(ancho), run_time=18.0,
        )
        self.wait(6.0)                                               # 0:49
        # Encabezado de la tabla de puntos de muestreo y áreas.
        self.play(Write(cabecera), run_time=6.0)                     # 0:55
        self.play(FadeIn(etiqueta), Write(valor), run_time=1.0)      # 1:01
        # Construir un rectángulo por subintervalo, acumulando la suma.
        acumulado = 0.0
        for i in range(n):
            acumulado += areas[i]
            nuevo_valor = MathTex(
                decimal(acumulado, 5), font_size=26,
            ).next_to(etiqueta, RIGHT, buff=0.12)
            self.play(                                                # 1:02 / 1:11,5 / ...
                Create(rectangulos[i]),
                FadeIn(alturas_lineas[i]),
                FadeIn(puntos[i]),
                FadeIn(filas[i]),
                ReplacementTransform(valor, nuevo_valor),
                run_time=7.0,
            )
            valor = nuevo_valor
            self.wait(2.5)
        # Explicación de la suma acumulada y de la fórmula de la sumatoria.
        self.wait(44.0)                                              # 1:40
        # Integral definida: valor exacto del área.
        self.play(                                                    # 2:24
            FadeOut(etiqueta), FadeOut(valor), Write(exacta), run_time=7.0,
        )
        self.wait(6.0)                                               # 2:31
        # Aproximación con cuatro rectángulos (S_4 = 4,625).
        self.play(Write(total), run_time=6.0)                        # 2:37
        self.wait(2.0)                                               # 2:43
        # Cierre: es una buena aproximación, pero no el valor exacto.
        self.play(Write(nota), run_time=3.0)                         # 2:45
        self.wait(8.0)                                               # 2:48 → 2:56
