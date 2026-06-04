import streamlit as st

st.title("Proyecto Final Diploma BI")

st.sidebar.title("Parametros")

st.image("Python_logo.png", width = 500)
st.sidebar.image("DMC.png", width = 300)

st.write("Elaborado por: Chris Perea")

archivo = st.file_uploader("Cargue el archivo excel o csv")

if archivo is not None :
  if archivo.name.endswith(".csv"):
    data = pd.read_csv(archivo)
    st.write(data)
  elif archivo.name.endswith(".xlsx")
   data = pd.read_excel(archivo)
else:
  st.write("Formato no Válido")

else:
 st.write("Por favor cargue su archivo")


