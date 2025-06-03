import streamlit as st
from src.load_user_data import load_user_data, get_all_names, get_image
from src.analyze_hr_data_functions import load_data, calculate_hr_zones, assign_zones, prepare_time_columns, plot_heart_rate_power, calculate_time_per_zone


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


df = load_data()
max_hr = st.number_input("Maximale Herzfrequenz eingeben:", min_value=100, max_value=220, value=190, step=1)
hr_zones = calculate_hr_zones(max_hr)

df = assign_zones(df, hr_zones)
df = prepare_time_columns(df)

st.plotly_chart(plot_heart_rate_power(df, max_hr))

time_zone_stats = calculate_time_per_zone(df)
print(time_zone_stats)

# Viel Spaß
st.write("")
st.write("Viel Spaß mit der App!")