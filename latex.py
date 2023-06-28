import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image, ImageTk

def convert_latex_to_image(latex_formula, output_path):
    fig = plt.figure(figsize=(2.4, 2))
    
    # Cambiar el color de fondo de la figura (ejemplo: #2f3123)
    fig.patch.set_facecolor('#2f3123')
    
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.text(0, 0.5, latex_formula, fontsize=14, va='center', color='white')

    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    image = canvas.tostring_rgb()
    width, height = canvas.get_width_height()
    image = Image.frombytes("RGB", (width, height), image)

    image.save(output_path, "PNG")
    plt.close(fig)
    
# Ejemplo de uso
formula = r"$\theta$"
formula2= r"$\mu$"
formula3= r"$E_{ci}$"
latex_formula = "Donde: \n  - W = Trabajo \n  - F = Fuerza \n  - D = Desplazamiento \n  - "+(formula)+" = Angulo \n  - "+(formula2)+" = Coficiente \n  de Roce "
output_path = "latex_formula_8.png"
convert_latex_to_image(latex_formula, output_path)
print("La fórmula LaTeX se ha convertido en una imagen con fondo de color y letras blancas y se ha guardado en", output_path)
