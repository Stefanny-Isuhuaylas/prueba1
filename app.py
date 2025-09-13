import streamlit as st
from sympy import sympify, simplify

st.set_page_config(page_title="Buscador de Ecuaciones Similares", page_icon="🔎")

st.title("🔎 Buscador de Ecuaciones Similares")
st.write("Ingresa ecuaciones matemáticas y compara si son equivalentes o producen el mismo resultado.")

# Inicializamos lista de ecuaciones en sesión
if "ecuaciones" not in st.session_state:
    st.session_state.ecuaciones = []

# Entrada de ecuación
nueva_ecuacion = st.text_input("Escribe una ecuación:")

# Botón para agregar ecuación
if st.button("➕ Agregar ecuación"):
    if nueva_ecuacion.strip() != "":
        st.session_state.ecuaciones.append(nueva_ecuacion)
        st.success(f"Ecuación agregada: `{nueva_ecuacion}`")
    else:
        st.warning("Por favor, escribe una ecuación antes de agregarla.")

# Mostramos las ecuaciones ingresadas
if st.session_state.ecuaciones:
    st.subheader("Ecuaciones ingresadas:")
    for i, eq in enumerate(st.session_state.ecuaciones, 1):
        st.write(f"{i}. `{eq}`")

# Botón para comparar ecuaciones
if st.button("🔍 Comparar ecuaciones"):
    ecuaciones_simplificadas = []
    for eq in st.session_state.ecuaciones:
        try:
            # Simplificamos la ecuación con sympy
            expr = simplify(sympify(eq))
            ecuaciones_simplificadas.append(expr)
        except Exception:
            ecuaciones_simplificadas.append(None)

    # Comparamos
    st.subheader("Resultados:")
    encontrado = False
    for i in range(len(ecuaciones_simplificadas)):
        for j in range(i+1, len(ecuaciones_simplificadas)):
            e1 = ecuaciones_simplificadas[i]
            e2 = ecuaciones_simplificadas[j]
            if e1 is not None and e2 is not None and simplify(e1 - e2) == 0:
                st.success(f"✅ Las ecuaciones `{st.session_state.ecuaciones[i]}` y `{st.session_state.ecuaciones[j]}` son equivalentes o tienen el mismo resultado.")
                encontrado = True

    if not encontrado:
        st.info("No se encontraron ecuaciones equivalentes en la lista.")

# Botón para limpiar
if st.button("🗑️ Limpiar lista"):
    st.session_state.ecuaciones = []
    st.success("Lista de ecuaciones reiniciada.")
