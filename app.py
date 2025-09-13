import streamlit as st
from sympy import Eq, solve, sympify, Symbol

st.set_page_config(page_title="Buscador de Ecuaciones Similares", page_icon="🔎")

st.title("🔎 Buscador de Ecuaciones Similares")
st.write("Ingresa ecuaciones (por ejemplo: `x - 5 = 0`, `3*x - 15 = 0`) y compara si tienen la misma solución para x.")

x = Symbol('x')  # declaramos la variable x

if "ecuaciones" not in st.session_state:
    st.session_state.ecuaciones = []

nueva_ecuacion = st.text_input("Escribe una ecuación:")

if st.button("➕ Agregar ecuación"):
    if nueva_ecuacion.strip() != "":
        st.session_state.ecuaciones.append(nueva_ecuacion)
        st.success(f"Ecuación agregada: `{nueva_ecuacion}`")
    else:
        st.warning("Por favor, escribe una ecuación antes de agregarla.")

if st.session_state.ecuaciones:
    st.subheader("Ecuaciones ingresadas:")
    for i, eq in enumerate(st.session_state.ecuaciones, 1):
        st.write(f"{i}. `{eq}`")

def resolver_ecuacion(eq_str):
    try:
        # dividir en izquierda y derecha
        if '=' in eq_str:
            izq, der = eq_str.split('=')
        else:
            izq, der = eq_str, '0'
        expr_izq = sympify(izq)
        expr_der = sympify(der)
        ecuacion = Eq(expr_izq, expr_der)
        soluciones = solve(ecuacion, x)
        if len(soluciones) == 1:
            return soluciones[0]
        else:
            # devolvemos tupla o lista de soluciones
            return tuple(soluciones)
    except Exception:
        return None

if st.button("🔍 Comparar ecuaciones"):
    st.subheader("Resultados:")
    soluciones = [resolver_ecuacion(eq) for eq in st.session_state.ecuaciones]
    encontrado = False
    for i in range(len(soluciones)):
        for j in range(i+1, len(soluciones)):
            if soluciones[i] is not None and soluciones[j] is not None and soluciones[i] == soluciones[j]:
                st.success(
                    f"✅ Las ecuaciones `{st.session_state.ecuaciones[i]}` y `{st.session_state.ecuaciones[j]}` tienen la misma solución: x = {soluciones[i]}"
                )
                encontrado = True
    if not encontrado:
        st.info("No se encontraron ecuaciones con la misma solución para x.")

if st.button("🗑️ Limpiar lista"):
    st.session_state.ecuaciones = []
    st.success("Lista de ecuaciones reiniciada.")
