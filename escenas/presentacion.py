"""Presentación de 12 segundos: manim -pql escenas/presentacion.py Presentacion."""

from manim import BLUE, DOWN, GREEN, UP, FadeIn, Scene, Text, VGroup


class Presentacion(Scene):
    """Presenta el tema y la pregunta que guía el video, sin audio."""

    def construct(self):
        curso = Text("Cálculo Intermedio · Sección 1", font_size=23, color=GREEN)
        tema = Text(
            "El infinito en la\ndefinición de integral",
            font_size=40, line_spacing=1.1,
        )
        encabezado = VGroup(curso, tema).arrange(DOWN, buff=0.4).move_to(UP * 1.35)

        pregunta = VGroup(
            Text("Pregunta central", font_size=26, color=BLUE),
            Text(
                "¿Qué significa hacer n → ∞\n"
                "y por qué no se sustituye n por infinito?",
                font_size=29, line_spacing=1.2,
            ),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 1.35)

        self.play(FadeIn(encabezado), run_time=1)
        self.wait(2)
        self.play(FadeIn(pregunta), run_time=1)
        self.wait(8)
