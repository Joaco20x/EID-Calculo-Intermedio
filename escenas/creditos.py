"""Créditos de 32 segundos: manim -pql escenas/creditos.py Creditos."""

from manim import BLUE, DOWN, GREEN, UP, FadeIn, FadeOut, Scene, Text, VGroup


class Creditos(Scene):
    """Integrantes y fuentes del proyecto, sin enlaces en pantalla."""

    def construct(self):
        def tarjeta(titulo, entradas):
            """Agrupa cada título con su autor y ajusta el texto al encuadre."""
            encabezado = Text(titulo, font_size=36, color=BLUE).to_edge(UP, buff=0.65)
            bloques = VGroup()
            for nombre, autor in entradas:
                obra = Text(nombre, font_size=27, line_spacing=1.15)
                firma = Text(autor, font_size=23, color=GREEN)
                for texto in (obra, firma):
                    if texto.width > 12:
                        texto.scale_to_fit_width(12)
                bloques.add(VGroup(obra, firma).arrange(DOWN, buff=0.16))
            bloques.arrange(DOWN, buff=0.55).move_to(DOWN * 0.2)
            return VGroup(encabezado, bloques)

        integrantes = tarjeta("Créditos", (
            ("El infinito en la definición de integral", "Cálculo Intermedio · Sección 1"),
            ("Joaquín Valenzuela\nGabriel Gutiérrez\nAilyn Melillan", "Integrantes"),
        ))
        fuentes = tarjeta("Fuentes matemáticas y material docente", (
            ("Cálculo volumen 1 · OpenStax", "Gilbert Strang y Edwin Herman"),
            ("Cálculo (Apex) · LibreTexts", "Gregory Hartman y colaboradores"),
            ("Introducción a la integral", "Universidad Católica de Temuco"),
        ))
        recursos = tarjeta("Recursos y herramientas", (
            ("Este teorema lo cambió todo | ¿Qué es la integral?\n"
             "El famoso nexo entre derivadas e integrales", "BlueDot"),
            ("Manim Community Documentation", "Manim Community Developers"),
            ("ChatGPT", "OpenAI"),
        ))

        for pantalla, pausa in ((integrantes, 6), (fuentes, 12), (recursos, 8)):
            self.play(FadeIn(pantalla), run_time=1)
            self.wait(pausa)
            self.play(FadeOut(pantalla), run_time=1)
