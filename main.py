"""Renderizar el proyecto completo: manim -pql main.py ProyectoIntegral."""

from manim import FadeOut, Scene

from escenas import r1_rectangulos_fijos, r2_refinamiento, r3_limite_proceso


class ProyectoIntegral(Scene):
    """Reproduce las tres partes en orden dentro de un único video."""

    def construct(self):
        escenas = (
            r1_rectangulos_fijos.R1RectangulosFijos,
            r2_refinamiento.R2Refinamiento,
            r3_limite_proceso.R3LimiteProceso,
        )

        for indice, escena in enumerate(escenas):
            # Compartir la escena mantiene una sola línea de tiempo y un MP4.
            escena.construct(self)
            if indice < len(escenas) - 1:
                self.play(*[FadeOut(objeto) for objeto in self.mobjects], run_time=1)
                self.clear()
