"""El proceso del límite en la definición de la integral definida.

Escena autocontenida que visualiza y explica formalmente el paso al límite
en la suma de Riemann para f(x) = x² + 1 en [0, 2], demostrando por qué
n → ∞ es un proceso dinámico y no una sustitución numérica.

Ejecutar desde la raíz del proyecto:
    manim -pql escenas/r3_limite_proceso.py R3LimiteProceso

Para renderizado final de alta definición (1080p60):
    manim -qh escenas/r3_limite_proceso.py R3LimiteProceso

Duración aproximada: 79 segundos, sin audio; pausas para narración sincronizada.
Guía sugerida de narración:
----------------------------------------------------------------------------------
Tiempo   | Narración sugerida
----------------------------------------------------------------------------------
0–12 s   | Estudiamos el proceso del límite en la suma de Riemann para f(x) = x² + 1
         | en el intervalo cerrado cero dos.
12–26 s  | Comenzamos con cuatro rectángulos por punto medio. El ancho de cada uno
         | es dos dividido por n. Al hacer n tender a infinito, el ancho tiende
         | estrictamente a cero: no asignamos a n el valor infinito, sino que
         | aumentamos indefinidamente la cantidad de particiones.
26–49 s  | Al incrementar n sucesivamente a ocho, dieciséis, treinta y dos y
         | sesenta y cuatro rectángulos, el ancho disminuye y los rectángulos
         | se adaptan con precisión milimétrica a la curvatura, refinando el área.
49–65 s  | Analíticamente, la suma tiene una fórmula cerrada: catorce tercios menos
         | dos sobre tres n al cuadrado. Al aplicar el límite cuando n tiende a
         | infinito, el término de error desaparece por completo, entregando
         | catorce tercios exactos.
65–79 s  | En conclusión: cada suma de Riemann es finita. La integral definida no es
         | una suma de infinitos rectángulos, sino el valor límite exacto al que
         | convergen dichas sumas.
----------------------------------------------------------------------------------
"""

from manim import (
    BLUE, DOWN, GREEN, GREY, LEFT, RIGHT, UP, WHITE, YELLOW,
    Axes, BraceBetweenPoints, Create, Dot, FadeIn, FadeOut,
    MathTex, ReplacementTransform, RoundedRectangle, Scene, Text, VGroup, Write,
)


class R3LimiteProceso(Scene):
    """Representación del proceso de límite en sumas de Riemann para f(x) = x² + 1."""

    def construct(self):
        a, b = 0, 2
        area_exacta = 14 / 3
        niveles = (4, 8, 16, 32, 64)

        def f(x):
            return x**2 + 1

        def decimal(valor):
            # La coma entre llaves evita el espaciado de puntuación en modo matemático TeX
            return f"{valor:.4f}".replace(".", "{,}")

        # =====================================================================
        # 1. TÍTULO, SUBTÍTULO Y SISTEMA DE EJES
        # =====================================================================
        titulo = Text("El Límite en la Suma de Riemann", font_size=29).to_edge(UP, buff=0.30)
        subtitulo = MathTex(
            r"f(x) = x^2 + 1 \quad \text{en} \quad [0, 2]",
            font_size=21, color=YELLOW,
        ).next_to(titulo, DOWN, buff=0.10)

        ejes = Axes(
            x_range=[0, 2.25, 0.5],
            y_range=[0, 6, 1],
            x_length=5.3,
            y_length=3.7,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 20},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.35)
        ejes.set_z_index(2)

        curva = ejes.plot(f, x_range=[a, b], color=YELLOW).set_z_index(4)
        nombre_curva = MathTex(
            r"f(x) = x^2 + 1", color=YELLOW, font_size=26,
        ).next_to(ejes.c2p(1.25, 4.5), UP, buff=0.12)

        def construir_riemann(n):
            """Construye los rectángulos por punto medio, puntos de muestreo y llave de ancho."""
            dx = (b - a) / n
            puntos_medios = [a + (i + 0.5) * dx for i in range(n)]
            suma = sum(f(x) * dx for x in puntos_medios)

            rects = ejes.get_riemann_rectangles(
                curva,
                x_range=[a, b],
                dx=dx,
                input_sample_type="center",
                color=[BLUE, GREEN],
                fill_opacity=0.55,
                stroke_width=1.0 if n <= 16 else 0.4,
                stroke_color=WHITE if n <= 16 else BLUE,
                width_scale_factor=1,
            )
            rects.set_stroke(opacity=0.8 if n <= 16 else 0.35)

            if n <= 16:
                puntos = VGroup(*[
                    Dot(ejes.c2p(x, f(x)), radius=0.035, color=YELLOW)
                    for x in puntos_medios
                ]).set_z_index(5)
            else:
                puntos = VGroup()

            # Llave que ilustra el ancho del primer subintervalo [a, a + dx]
            inicio = ejes.c2p(a, 0) + DOWN * 0.4
            fin = ejes.c2p(a + dx, 0) + DOWN * 0.4
            llave = BraceBetweenPoints(inicio, fin, direction=DOWN, color=BLUE)
            texto_llave = MathTex(
                rf"\Delta x = \frac{{2}}{{{n}}}",
                font_size=21, color=BLUE,
            ).next_to(llave, DOWN, buff=0.08)
            indicador_ancho = VGroup(llave, texto_llave)

            return rects, puntos, indicador_ancho, dx, suma

        # Entrada inicial
        self.play(Write(titulo), FadeIn(subtitulo), run_time=1.5)
        self.play(Create(ejes), Create(curva), Write(nombre_curva), run_time=2)
        self.wait(1.5)

        # =====================================================================
        # 2. SUMA INICIAL (n = 4) Y FÓRMULAS FUNDAMENTALES
        # =====================================================================
        rects_actual, puntos_actual, ancho_actual, dx_actual, suma_actual = construir_riemann(niveles[0])

        panel_riemann = VGroup(
            Text("Suma de Riemann (Punto Medio)", font_size=20, color=BLUE),
            MathTex(
                r"S_n = \sum_{i=0}^{n-1} f\left(\frac{2i+1}{n}\right)\,\frac{2}{n}",
                font_size=24,
            ),
            MathTex(
                r"\text{Ancho de subintervalo:}\quad \Delta x = \frac{b-a}{n} = \frac{2}{n}",
                font_size=20, color=BLUE,
            ),
            VGroup(
                MathTex(rf"n = {niveles[0]}", font_size=22),
                MathTex(rf"\Delta x = {decimal(dx_actual)}", font_size=22, color=BLUE),
                MathTex(rf"S_4 = {decimal(suma_actual)}", font_size=22, color=GREEN),
            ).arrange(RIGHT, buff=0.30),
        ).arrange(DOWN, buff=0.12).move_to(RIGHT * 3.4 + UP * 1.75)

        self.play(
            Create(rects_actual),
            FadeIn(puntos_actual),
            FadeIn(ancho_actual),
            FadeIn(panel_riemann),
            run_time=2,
        )
        self.wait(4)

        # =====================================================================
        # 3. EXPLICACIÓN DEL ANCHO Δx -> 0 Y SIGNIFICADO DE n -> ∞
        # =====================================================================
        panel_limite_dx = VGroup(
            Text("Comportamiento del ancho al aumentar n:", font_size=18, color=BLUE),
            MathTex(
                r"\lim_{n \to \infty} \Delta x = \lim_{n \to \infty} \frac{2}{n} = 0",
                font_size=24, color=BLUE,
            ),
        ).arrange(DOWN, buff=0.10).move_to(RIGHT * 3.4 + UP * 0.10)

        # Cuadro conceptual 1: Significado de n -> infinito
        caja_infinito_fondo = RoundedRectangle(
            corner_radius=0.12, width=6.5, height=1.75,
            stroke_color=YELLOW, stroke_width=1.2,
            fill_color="#111827", fill_opacity=0.92,
        )
        caja_infinito_texto = VGroup(
            Text("Nota conceptual: el significado de n → ∞", font_size=16, color=YELLOW),
            Text("• n → ∞ significa tomar valores de n sucesivamente mayores.", font_size=14),
            Text("• No se asigna a n un valor numérico fijo llamado 'infinito'.", font_size=14),
            Text("• Al crecer n, cada rectángulo se hace más angosto y afina el área.", font_size=14),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        caja_infinito_texto.move_to(caja_infinito_fondo.get_center())
        caja_infinito = VGroup(caja_infinito_fondo, caja_infinito_texto).move_to(
            RIGHT * 3.4 + DOWN * 1.65
        )

        self.play(FadeIn(panel_limite_dx), FadeIn(caja_infinito), run_time=1.5)
        self.wait(6)

        # =====================================================================
        # 4. AUMENTO PROGRESIVO DE SUBINTERVALOS (REFINAMIENTO VISUAL)
        # =====================================================================
        self.play(
            FadeOut(panel_riemann),
            FadeOut(panel_limite_dx),
            FadeOut(caja_infinito),
            run_time=1,
        )

        panel_refinamiento_titulo = VGroup(
            Text("Aumento progresivo de subintervalos (n)", font_size=20, color=YELLOW),
            Text("Los rectángulos se ajustan cada vez mejor bajo la curva:", font_size=16, color=GREY),
        ).arrange(DOWN, buff=0.12).move_to(RIGHT * 3.4 + UP * 1.55)

        def crear_fila_estado(n_val, dx_val, s_val):
            err_val = abs(area_exacta - s_val)
            return VGroup(
                MathTex(rf"n = {n_val}", font_size=25),
                MathTex(rf"\Delta x = {decimal(dx_val)}", font_size=24, color=BLUE),
                MathTex(rf"S_{{{n_val}}} \approx {decimal(s_val)}", font_size=25, color=GREEN),
                MathTex(rf"\text{{Error}} \approx {decimal(err_val)}", font_size=22, color=GREY),
            ).arrange(RIGHT, buff=0.28).move_to(RIGHT * 3.4 + UP * 0.75)

        indicador_estado = crear_fila_estado(niveles[0], dx_actual, suma_actual)
        self.play(Write(panel_refinamiento_titulo), FadeIn(indicador_estado), run_time=1)
        self.wait(1.5)

        for n_siguiente in niveles[1:]:
            nuevos_rects, nuevos_puntos, nuevo_ancho, nuevo_dx, nueva_suma = construir_riemann(n_siguiente)
            nuevo_indicador = crear_fila_estado(n_siguiente, nuevo_dx, nueva_suma)

            animaciones = [
                ReplacementTransform(rects_actual, nuevos_rects),
                ReplacementTransform(indicador_estado, nuevo_indicador),
            ]
            if len(puntos_actual) > 0 and len(nuevos_puntos) > 0:
                animaciones.append(ReplacementTransform(puntos_actual, nuevos_puntos))
            elif len(puntos_actual) > 0:
                animaciones.append(FadeOut(puntos_actual))

            # Con n grandes la llave se retira para mantener la estética limpia
            if n_siguiente <= 16:
                animaciones.append(ReplacementTransform(ancho_actual, nuevo_ancho))
                ancho_actual = nuevo_ancho
            elif ancho_actual is not None:
                animaciones.append(FadeOut(ancho_actual))
                ancho_actual = None

            self.play(*animaciones, run_time=1.8)
            rects_actual = nuevos_rects
            puntos_actual = nuevos_puntos
            indicador_estado = nuevo_indicador
            self.wait(2.0)

        # Transición hacia el área continua exacta bajo la curva
        area_continua = ejes.get_area(
            curva, x_range=[a, b], color=[BLUE, GREEN], opacity=0.55,
        )
        texto_ajuste = Text(
            "Con n grande, la discretización converge al área continua.",
            font_size=17, color=WHITE,
        ).move_to(RIGHT * 3.4 + UP * 0.05)

        self.play(
            ReplacementTransform(rects_actual, area_continua),
            FadeIn(texto_ajuste),
            run_time=2,
        )
        self.wait(3.5)

        # =====================================================================
        # 5. FÓRMULAS ALGEBRAICAS Y RELACIÓN CON LA INTEGRAL DEFINIDA
        # =====================================================================
        self.play(
            FadeOut(panel_refinamiento_titulo),
            FadeOut(indicador_estado),
            FadeOut(texto_ajuste),
            run_time=1,
        )

        panel_algebra = VGroup(
            Text("Expresión algebraica exacta:", font_size=18, color=YELLOW),
            MathTex(
                r"S_n = \frac{14}{3} - \frac{2}{3n^2}",
                font_size=28,
            ),
            MathTex(
                r"\text{Para todo } n \text{ finito, } S_n < \frac{14}{3}"
                r"\quad \text{con error } \frac{2}{3n^2}",
                font_size=17, color=GREY,
            ),
            Text("Límite cuando n → ∞:", font_size=18, color=BLUE),
            MathTex(
                r"\lim_{n \to \infty} S_n = \lim_{n \to \infty}"
                r"\left(\frac{14}{3} - \frac{2}{3n^2}\right) = \frac{14}{3}",
                font_size=24, color=GREEN,
            ),
            Text("Relación con la integral definida:", font_size=18, color=GREEN),
            MathTex(
                r"\int_0^2 (x^2 + 1)\,dx = \lim_{n \to \infty} S_n = \frac{14}{3} \approx 4{,}6667",
                font_size=25, color=GREEN,
            ),
        ).arrange(DOWN, buff=0.13).move_to(RIGHT * 3.4 + UP * 0.90)

        self.play(Write(panel_algebra), run_time=3.5)
        self.wait(5)

        # =====================================================================
        # 6. CUADRO CONCEPTUAL DE CIERRE (FINITUD VS. LÍMITE)
        # =====================================================================
        caja_cierre_fondo = RoundedRectangle(
            corner_radius=0.12, width=6.5, height=1.9,
            stroke_color=GREEN, stroke_width=1.3,
            fill_color="#111827", fill_opacity=0.94,
        )
        caja_cierre_texto = VGroup(
            Text("Conclusiones conceptuales clave", font_size=16, color=YELLOW),
            Text("• Cada suma S_n es finita: suma n rectángulos de base medible.", font_size=14),
            Text("• La integral NO es una 'suma con infinitos rectángulos'.", font_size=14),
            Text("• Es estrictamente el LÍMITE matemático de las sumas: lím S_n.", font_size=14),
            Text("• El paso al límite anula el error analítico: lím (2 / 3n²) = 0.", font_size=14, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        caja_cierre_texto.move_to(caja_cierre_fondo.get_center())
        caja_cierre = VGroup(caja_cierre_fondo, caja_cierre_texto).move_to(
            RIGHT * 3.4 + DOWN * 2.15
        )

        self.play(FadeIn(caja_cierre), run_time=2)
        self.wait(9)
