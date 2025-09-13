import streamlit as st

st.set_page_config(page_title="Buscador de Ecuaciones Similares", page_icon="🔎")

st.title("🔎 Buscador de Ecuaciones Similares")
st.write("Ingresa ecuaciones matemáticas y compara si producen el mismo resultado numérico.")

# Inicializamos lista de ecuaciones en sesión
if "ecuaciones" not in st.session_state:
    st.session_state.ecuaciones = []

# Entrada de ecuación
nueva_ecuacion = st.text_input("Escribe una ecuación (usa x como variable):")

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
    st.subheader("Resultados:")
    encontrado = False
    # probamos varios valores para x
    valores_prueba = [0, 1, 2, 3, 5, 10]

    for i in range(len(st.session_state.ecuaciones)):
        for j in range(i+1, len(st.session_state.ecuaciones)):
            eq1 = st.session_state.ecuaciones[i]
            eq2 = st.session_state.ecuaciones[j]
            iguales = True
            for x in valores_prueba:
                try:
                    res1 = eval(eq1)
                    res2 = eval(eq2)
                except Exception:
                    iguales = False
                    break
                if abs(res1 - res2) > 1e-6:
                    iguales = False
                    break
            if iguales:
                st.success(f"✅ Las ecuaciones `{eq1}` y `{eq2}` parecen dar el mismo resultado numérico para varios valores de x.")
                encontrado = True

    if not encontrado:
        st.info("No se encontraron ecuaciones equivalentes en la lista.")

# Botón para limpiar
if st.button("🗑️ Limpiar lista"):
    st.session_state.ecuaciones = []
    st.success("Lista de ecuaciones reiniciada.")

