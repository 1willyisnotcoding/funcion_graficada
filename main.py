from manim import *
import sympy as sp
import numpy as np
import os

class GraficaFuncion(Scene):
    def __init__(self, eq, **kwargs):
        super().__init__(**kwargs)
        self.eq = eq

    def construct(self):
        eq = self.eq.replace("^", "**").replace("sen", "sin")
        x = sp.Symbol('x')
        try:
            expr = sp.sympify(eq)
            func = sp.lambdify(x, expr, 'numpy')
        except Exception as e:
            print("Error en la función:", e)
            return

        plano = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4}
        )
        plano.add_coordinates()

        grafica = plano.plot(lambda t: func(t), color=YELLOW)
        titulo = Text(f"f(x) = {eq}", font_size=28).to_edge(UP)

        self.play(Create(plano))
        self.play(Write(titulo))
        self.play(Create(grafica), run_time=5)

        intersecciones = []

        try:
            y_intercept = func(0)
            if np.isfinite(y_intercept):
                intersecciones.append((0, y_intercept))
        except Exception:
            pass

        try:
            soluciones = sp.solve(expr, x)
            for sol in soluciones:
                if sol.is_real:
                    intersecciones.append((float(sol), 0))
        except Exception:
            pass

        puntos = VGroup()
        for p in intersecciones:
            dot = Dot(plano.coords_to_point(p[0], p[1]), color=RED)
            label = MathTex(f"({p[0]:.2f}, {p[1]:.2f})").scale(0.5).next_to(dot, UP)
            puntos.add(dot, label)
            self.play(FadeIn(dot), FadeIn(label))

        self.wait(3)

if __name__ == "__main__":
    eq = input("Ingresa la función (en x): ").strip()
    if not eq:
        print("No se ingresó ninguna función.")
    else:
        output_path = r"C:\Coding\Funciones graficadas"
        os.makedirs(output_path, exist_ok=True)

        from manim import config, tempconfig
        config.media_width = "100%"
        config.verbosity = "WARNING"

        with tempconfig({
            "preview": True,
            "quality": "fourk_quality",
            "output_file": os.path.join(output_path, "grafica.mp4")
        }):
            scene = GraficaFuncion(eq)
            scene.render()

        print(f"\nVideo guardado en: {os.path.join(output_path, 'grafica.mp4')}")
