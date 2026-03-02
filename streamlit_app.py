import streamlit as st
import matplotlib.pyplot as plt

# Datos de ejemplo
y_coordinate = -125

# Función para dibujar círculo (equivalente a turtle)
def draw_circle(ax, fill_color, border_color, x, y, radius):
    circle = plt.Circle((x, y), radius, facecolor=fill_color, edgecolor=border_color, linewidth=3)
    ax.add_patch(circle)

st.title("Dibujo estilo Turtle en Streamlit")

# Botón para dibujar
if st.button("Dibujar círculos"):
    fig, ax = plt.subplots(figsize=(6,6))
    
    # Ajustes del canvas
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    ax.set_aspect('equal')
    ax.axis('off')  # Oculta ejes

    # Ejemplo de círculos
    draw_circle(ax, fill_color="red", border_color="black", x=0, y=y_coordinate, radius=50)
    draw_circle(ax, fill_color="blue", border_color="green", x=100, y=y_coordinate+50, radius=30)
    draw_circle(ax, fill_color="yellow", border_color="orange", x=-100, y=y_coordinate+100, radius=40)
    
    st.pyplot(fig)
