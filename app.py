import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gráficos 3D de Ecuaciones", layout="wide")
st.title("🎨 Graficador de Funciones 3D (sin Sympy)")

if "funciones" not in st.session_state:
    st.session_state.funciones = []

st.write("Ingresa expresiones para **z** en función de **x** y **y** (por ejemplo: `x**2 + y**2`)")

nueva_funcion = st.text_input("Nueva función z(x,y):")

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Agregar función"):
        if nueva_funcion.strip() != "":
            st.session_state.funciones.append(nueva_funcion.strip())
with col2:
    if st.button("🗑️ Limpiar lista"):
        st.session_state.funciones = []

st.subheader("📜 Funciones actuales")
if st.session_state.funciones:
    for i, f in enumerate(st.session_state.funciones, 1):
        st.write(f"{i}. `z = {f}`")
else:
    st.info("No hay funciones agregadas aún.")

if st.button("🎨 Generar Gráfico 3D"):
    if not st.session_state.funciones:
        st.warning("Agrega al menos una función primero.")
    else:
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Rango de valores
        X_vals = np.linspace(-5, 5, 50)
        Y_vals = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(X_vals, Y_vals)

        for f_text in st.session_state.funciones:
            try:
                # Evaluar z con numpy
                Z = eval(f_text, {"x": X, "y": Y, "np": np})
                ax.plot_surface(X, Y, Z, alpha=0.5)
            except Exception as e:
                st.error(f"Error con la función `{f_text}`: {e}")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        st.pyplot(fig)
