"""Renderizar el proyecto completo: manim -pql main.py ProyectoIntegral."""

from manim import FadeOut, Scene

from escenas import (
    creditos, presentacion, r1_rectangulos_fijos, r2_refinamiento, r3_limite_proceso,
)


class ProyectoIntegral(Scene):
    """Reproduce presentación, tres partes y créditos en un único video."""

    def construct(self):
        escenas = (
            presentacion.Presentacion,
            r1_rectangulos_fijos.R1RectangulosFijos,
            r2_refinamiento.R2Refinamiento,
            r3_limite_proceso.R3LimiteProceso,
            creditos.Creditos,
        )

        for indice, escena in enumerate(escenas):
            # Compartir la escena mantiene una sola línea de tiempo y un MP4.
            escena.construct(self)
            if indice < len(escenas) - 1:
                self.play(*[FadeOut(objeto) for objeto in self.mobjects], run_time=1)
                self.clear()
