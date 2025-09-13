import streamlit as st

st.set_page_config(page_title="Buscador de Ecuaciones Similares", page_icon="🔎")

st.title("🔎 Buscador de Ecuaciones Similares")
st.write("Ingresa ecuaciones lineales (en forma ax + b = c) y compara si tienen la misma solución para x.")

if "ecuaciones" not in st.session_state:
    st.session_state.ecuaciones = []

nueva_ecuacion = st.text_input("Escribe una ecuación (por ejemplo: 2*x+3=7):")

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

def resolver_lineal(ecuacion):
    """
    Resuelve ecuaciones lineales sencillas en x del tipo 'expresion = expresion'
    """
    try:
        izq, der = ecuacion.split('=')
        # reemplazar x por una variable python
        x = 1  # solo para que eval no falle
        # movemos todo al lado izquierdo
        expr = f"({izq})-({der})"
        # evaluamos coeficientes numéricos
        # tomamos derivadas numéricas para a y b
        # probamos dos valores para x para sacar a y b:
        x1 = 0
        x2 = 1
        val1 = eval(expr)
        x = x2
        val2 = eval(expr)
        a = val2 - val1
        b = val1  # porque en x=0 es solo b
        if a == 0:
            return None  # no es lineal o sin solución única
        sol = -b / a
        return sol
    except Exception:
        return None

if st.button("🔍 Comparar ecuaciones"):
    st.subheader("Resultados:")
    soluciones = [resolver_lineal(eq) for eq in st.session_state.ecuaciones]
    encontrado = False
    for i in range(len(soluciones)):
        for j in range(i+1, len(soluciones)):
            if soluciones[i] is not None and soluciones[j] is not None and abs(soluciones[i]-soluciones[j]) < 1e-6:
                st.success(f"✅ Las ecuaciones `{st.session_state.ecuaciones[i]}` y `{st.session_state.ecuaciones[j]}` tienen la misma solución x = {soluciones[i]}.")
                encontrado = True
    if not encontrado:
        st.info("No se encontraron ecuaciones con la misma solución para x.")

if st.button("🗑️ Limpiar lista"):
    st.session_state.ecuaciones = []
    st.success("Lista de ecuaciones reiniciada.")

