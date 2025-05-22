import streamlit as st
from src.load_user_data import load_user_data, get_all_names, get_image


# Sicherstellen, dass auch vor der Nutzerauwahl schon ein Wert im SessionState ist
if "current_user" not in st.session_state:
    st.session_state.current_user = "None"

FILE_PATH = 'data/person_db.json'  # Replace with the actual path to your JSON file
user_data = load_user_data(FILE_PATH)

name_list = get_all_names(user_data)

st.title('EKG App')

# Eine Überschrift der zweiten Ebene 
st.write('# Versuchsperson auswählen')

st.write("Versuchsperson auswählen")

# Eine Auswahlbox
st.session_state["current_user"] = st.selectbox(
    'Versuchsperson',
    options= name_list, key="sbVersuchsperson")

st.write("Aktuelle Versuchsperson: ", st.session_state["current_user"])
         
# Anzeigen eines Bilds mit Caption
st.image(get_image(st.session_state["current_user"]), caption=st.session_state["current_user"])

# Viel Spaß
st.write("")
st.write("Viel Spaß mit der App!")