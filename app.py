import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gráficos 3D de Ecuaciones", layout="wide")
st.title("🎨 Graficador de Ecuaciones 3D")

# --- Estado para guardar ecuaciones ---
if "ecuaciones" not in st.session_state:
    st.session_state.ecuaciones = []

st.write("Ingresa ecuaciones en términos de **x**, **y** y **z** (ejemplo: `x**2 + y**2 - z`)")

# Input para nueva ecuación
nueva_ecuacion = st.text_input("Nueva ecuación:")

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Agregar ecuación"):
        if nueva_ecuacion.strip() != "":
            st.session_state.ecuaciones.append(nueva_ecuacion.strip())
with col2:
    if st.button("🗑️ Limpiar lista"):
        st.session_state.ecuaciones = []

st.subheader("📜 Ecuaciones actuales")
if st.session_state.ecuaciones:
    for i, eq in enumerate(st.session_state.ecuaciones, 1):
        st.write(f"{i}. `{eq}`")
else:
    st.info("No hay ecuaciones agregadas aún.")

# --- Botón para generar gráfico 3D ---
if st.button("🎨 Generar Gráfico 3D"):
    if not st.session_state.ecuaciones:
        st.warning("Agrega al menos una ecuación primero.")
    else:
        x, y, z = sp.symbols('x y z')
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Rango de valores
        X_vals = np.linspace(-5, 5, 50)
        Y_vals = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(X_vals, Y_vals)

        for eq_text in st.session_state.ecuaciones:
            try:
                expr = sp.sympify(eq_text)
                # Resolver para z
                sol = sp.solve(sp.Eq(expr, 0), z)
                if sol:
                    Z = sp.lambdify((x, y), sol[0], "numpy")(X, Y)
                    ax.plot_surface(X, Y, Z, alpha=0.5)
                else:
                    st.warning(f"No se pudo resolver para z: `{eq_text}`")
            except Exception as e:
                st.error(f"Error con la ecuación `{eq_text}`: {e}")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        st.pyplot(fig)


