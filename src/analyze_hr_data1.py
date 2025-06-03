# %%
import pandas as pd
from plotly import express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# %%
# 1. Daten laden
PATH = "../data/activity.csv"
df = pd.read_csv(PATH)

# %%
# 2. Maximale Herzfrequenz eingeben
max_hr = int(input("Enter your maximum heart rate: "))

# %%
# 3. Herzfrequenz-Zonen berechnen
hr_zones = {}
for i, percent in enumerate(range(50, 100, 10), start=1):
    hr_zones[f"Zone{i}"] = max_hr * (percent / 100)

# %%
# 4. Zone für jeden Messpunkt bestimmen
zone_labels = []
for hr in df["HeartRate"]:
    if hr > hr_zones["Zone5"]:
        zone_labels.append("Zone 5")
    elif hr > hr_zones["Zone4"]:
        zone_labels.append("Zone 4")
    elif hr > hr_zones["Zone3"]:
        zone_labels.append("Zone 3")
    elif hr > hr_zones["Zone2"]:
        zone_labels.append("Zone 2")
    else:
        zone_labels.append("Zone 1")

df["Zone"] = zone_labels

# %%
# 5. Zeit umrechnen und neue Zeitspalte anlegen
df["Time"] = df.index
df["Time_min"] = df["Time"] / 60

# %%
# 6. Plot vorbereiten
zone_ranges = [
    {"name": "Zone 1", "min": 0, "max": max_hr * 0.6, "color": "rgba(173,216,230,0.2)"},
    {"name": "Zone 2", "min": max_hr * 0.6, "max": max_hr * 0.7, "color": "rgba(144,238,144,0.2)"},
    {"name": "Zone 3", "min": max_hr * 0.7, "max": max_hr * 0.8, "color": "rgba(255,255,102,0.2)"},
    {"name": "Zone 4", "min": max_hr * 0.8, "max": max_hr * 0.9, "color": "rgba(255,165,0,0.2)"},
    {"name": "Zone 5", "min": max_hr * 0.9, "max": max_hr, "color": "rgba(255,99,71,0.2)"},
]

fig = make_subplots(specs=[[{"secondary_y": True}]])

# 6.1 Hintergrundfarben für Zonen
for zone in zone_ranges:
    fig.add_shape(
        type="rect",
        xref="x", yref="y1",
        x0=df["Time_min"].min(),
        x1=df["Time_min"].max(),
        y0=zone["min"],
        y1=zone["max"],
        fillcolor=zone["color"],
        layer="below",
        line_width=0,
    )

# 6.2 Herzfrequenz (linke y-Achse)
fig.add_trace(
    go.Scatter(x=df["Time_min"], y=df["HeartRate"], name="Heart Rate", line=dict(color="black")),
    secondary_y=False,
)

# 6.3 Power (rechte y-Achse)
fig.add_trace(
    go.Scatter(x=df["Time_min"], y=df["PowerOriginal"], name="Power [W]", line=dict(color="orange")),
    secondary_y=True,
)

# 6.4 Achsen, Layout und Anzeige
fig.update_layout(
    title="Herzfrequenz & Leistung über Zeit",
    xaxis_title="Zeit / [min]",
    yaxis_title="Heart Rate / [bpm]",
    legend_title="Legende",
    width=900,
    height=500,
    yaxis=dict(showline=True, zeroline=False),
    yaxis2=dict(showline=True, zeroline=False)
)

fig.update_xaxes(
    tickmode="array",
    tickvals=[0, 5, 10, 15, 20, 25, 30],
    ticktext=["0", "5", "10", "15", "20", "25", "30"],
    range=[0, 30],
    showgrid=False
)

fig.update_yaxes(title_text="Heart Rate / [bpm]", secondary_y=False, range=[0, max_hr], showgrid=False)
fig.update_yaxes(title_text="Power / [W]", secondary_y=True, range=[0, 450], showgrid=False)

fig.show()

# %%
# 7. Zeit pro Zone berechnen
time_per_zone = df["Zone"].value_counts().sort_index().rename("Anzahl Messpunkte").to_frame()
time_per_zone["Zeit [s]"] = time_per_zone["Anzahl Messpunkte"]
time_per_zone["Zeit [min]"] = (time_per_zone["Zeit [s]"] / 60).round(2)
time_per_zone["Leistung [W]"] = df.groupby("Zone")["PowerOriginal"].mean().round(2)
time_per_zone.drop(columns=["Anzahl Messpunkte"], inplace=True)

print(time_per_zone)
# %%
