"""Refinamiento de sumas de Riemann por el método del punto medio.

Ejecutar desde la raíz del proyecto:
    manim -pql escenas/r2_refinamiento.py R2Refinamiento

Duración: 60 segundos, sin audio; las pausas dejan espacio a la narración.
"""

from manim import (
    BLUE, DOWN, GREEN, LEFT, RIGHT, UP, WHITE, YELLOW,
    Axes, BraceBetweenPoints, Create, Dot, FadeIn, FadeOut,
    MathTex, ReplacementTransform, Scene, Text, VGroup, Write,
)


class R2Refinamiento(Scene):
    """Cuatro aproximaciones finitas al área bajo f(x) = x² + 1."""

    def construct(self):
        a, b = 0, 2
        niveles = (2, 4, 8, 16)
        area_exacta = 14 / 3

        def f(x):
            return x**2 + 1

        def decimal(valor):
            # La coma se agrupa para evitar el espacio de puntuación de TeX.
            return f"{valor:.4f}".replace(".", "{,}")

        titulo = Text("Refinamiento por punto medio", font_size=36).to_edge(UP)
        formula = MathTex(
            r"S_n=\sum_{i=0}^{n-1}f(x_i^*)\,\Delta x,"
            r"\qquad x_i^*=\frac{2i+1}{n},"
            r"\qquad \Delta x=\frac{b-a}{n}=\frac{2}{n}",
            font_size=29,
        ).next_to(titulo, DOWN, buff=0.24)

        ejes = Axes(
            x_range=[0, 2.25, 0.5],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=3.8,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 22},
        ).to_edge(LEFT, buff=0.65).shift(DOWN * 0.3)
        curva = ejes.plot(f, x_range=[a, b], color=YELLOW).set_z_index(3)
        nombre_curva = MathTex(
            r"f(x)=x^2+1", color=YELLOW, font_size=28,
        ).next_to(ejes.c2p(1.25, 4.5), UP, buff=0.12)
        ejes.set_z_index(2)

        exacta = VGroup(
            Text("Área exacta", font_size=24),
            MathTex(
                r"\int_0^2(x^2+1)\,dx=\frac{14}{3}", font_size=32,
            ),
            MathTex(r"\frac{14}{3}\approx4{,}6667", font_size=30, color=GREEN),
        ).arrange(DOWN, buff=0.18).move_to(RIGHT * 3.7 + DOWN * 1.55)

        nota = Text(
            "Cada altura se calcula en el punto medio del subintervalo.",
            font_size=23,
        ).to_edge(DOWN, buff=0.25)

        def refinamiento(n):
            """Construye los rectángulos de punto medio y sus indicadores para n.

            Devuelve los rectángulos, los puntos de muestreo, la llave del
            ancho y los valores calculados, para animarlos por separado.
            """
            dx = (b - a) / n
            puntos_medios = [a + (i + 0.5) * dx for i in range(n)]
            suma = sum(f(x) * dx for x in puntos_medios)
            rectangulos = ejes.get_riemann_rectangles(
                curva,
                x_range=[a, b],
                dx=dx,
                input_sample_type="center",
                color=[BLUE, GREEN],
                fill_opacity=0.55,
                stroke_width=1.2,
                stroke_color=WHITE,
                width_scale_factor=1,
            )
            puntos = VGroup(*[
                Dot(ejes.c2p(x, f(x)), radius=0.035, color=YELLOW)
                for x in puntos_medios
            ]).set_z_index(4)

            # La llave usa la misma escala horizontal que los rectángulos.
            inicio = ejes.c2p(a, 0) + DOWN * 0.5
            fin = ejes.c2p(a + dx, 0) + DOWN * 0.5
            llave = BraceBetweenPoints(inicio, fin, direction=DOWN, color=BLUE)
            ancho = VGroup(
                llave,
                MathTex(r"\Delta x", font_size=25, color=BLUE).next_to(
                    llave, DOWN, buff=0.08,
                ),
            )
            datos = VGroup(
                MathTex(rf"n={n}", font_size=37),
                MathTex(
                    rf"\Delta x=\frac{{2}}{{{n}}}={decimal(dx)}",
                    font_size=31, color=BLUE,
                ),
                MathTex(rf"S_{{{n}}}\approx{decimal(suma)}", font_size=35, color=GREEN),
                MathTex(
                    rf"\frac{{14}}{{3}}-S_{{{n}}}\approx{decimal(area_exacta - suma)}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.22).move_to(RIGHT * 3.7 + UP * 0.65)
            return rectangulos, puntos, ancho, datos

        self.play(Write(titulo), Write(formula), run_time=2)
        self.play(Create(ejes), Create(curva), Write(nombre_curva), run_time=2)
        self.wait(4)

        rectangulos, puntos, ancho, datos = refinamiento(niveles[0])
        self.play(
            Create(rectangulos), FadeIn(puntos), FadeIn(ancho), Write(datos),
            FadeIn(exacta), FadeIn(nota), run_time=2,
        )
        self.wait(2)

        ejemplo = VGroup(
            Text("Dos rectángulos: n = 2", font_size=25),
            MathTex(r"\Delta x=1,\quad x_0^*=0{,}5,\quad x_1^*=1{,}5", font_size=26),
            MathTex(r"f(0{,}5)=1{,}25,\quad f(1{,}5)=3{,}25", font_size=26),
            MathTex(r"S_2=(1{,}25+3{,}25)\cdot1=4{,}5", font_size=29, color=GREEN),
        ).arrange(DOWN, buff=0.22).move_to(RIGHT * 3.7 + UP * 0.65)
        self.play(ReplacementTransform(datos, ejemplo), run_time=1)
        self.wait(8)

        # Tabla acumulativa: las filas anteriores permanecen para comparar.
        columnas = (1.25, 2.45, 3.95, 5.55)
        cabecera = VGroup(*[
            MathTex(texto, font_size=25).move_to(RIGHT * x + UP * 1.55)
            for texto, x in zip(
                (r"n", r"\Delta x", r"S_n\approx", r"\mathrm{Error}\approx"), columnas,
            )
        ])
        filas = VGroup()
        for indice, n in enumerate(niveles):
            dx = (b - a) / n
            suma = sum(f(a + (i + 0.5) * dx) * dx for i in range(n))
            fila = VGroup(*[
                MathTex(valor, font_size=25).move_to(
                    RIGHT * x + UP * (1.05 - indice * 0.48),
                )
                for valor, x in zip(
                    (str(n), decimal(dx), decimal(suma), decimal(area_exacta - suma)),
                    columnas,
                )
            ])
            filas.add(fila)

        self.play(FadeOut(ejemplo), run_time=1)
        filas[0].set_color(YELLOW)
        self.play(Write(cabecera), Write(filas[0]), run_time=2)

        for indice, n in enumerate(niveles[1:], start=1):
            nuevos_rectangulos, nuevos_puntos, nuevo_ancho, nuevos_datos = refinamiento(n)
            filas[indice].set_color(YELLOW)
            self.play(
                ReplacementTransform(rectangulos, nuevos_rectangulos),
                ReplacementTransform(puntos, nuevos_puntos),
                ReplacementTransform(ancho, nuevo_ancho),
                filas[indice - 1].animate.set_color(WHITE),
                FadeIn(filas[indice]),
                run_time=2,
            )
            rectangulos, puntos = nuevos_rectangulos, nuevos_puntos
            ancho = nuevo_ancho
            self.wait(5)

        self.wait(3)

        conclusion = VGroup(
            MathTex(
                r"n\uparrow\quad\Longrightarrow\quad\Delta x\downarrow"
                r"\quad\Longrightarrow\quad S_n\longrightarrow\frac{14}{3}",
                font_size=25,
            ),
            Text(
                "Cada suma tiene n finito. No se sustituye n por infinito.",
                font_size=20,
            ),
            Text(
                "La animación ilustra el proceso; el límite requiere justificación.",
                font_size=18,
            ),
        ).arrange(DOWN, buff=0.13).to_edge(DOWN, buff=0.2)
        self.play(FadeOut(nota), FadeOut(ancho), run_time=1)
        self.play(Write(conclusion), run_time=2)
        self.wait(9)
