#%% CSV Einlesen und in dataframe speichern
import pandas as pd
#%%
def find_peaks(df_ekg, threshold, min_peak_distance):
    """
    A function that takes a DataFrame and returns a list of index-positions of the peaks
    """
    list_of_index_of_peaks = []
    last_peaks_index = 0
    for index, row in df_ekg.iterrows():
        if index < df_ekg.index.max() -1:
            # wenn rowin["Voltage in mV"] > als das vorhergehende und das folgende Element
            if row["Voltage in mV"] >= df_ekg.iloc[index-1]["Voltage in mV"] and row["Voltage in mV"] >= df_ekg.iloc[index+1]["Voltage in mV"]:
                # dann füge den aktuellen Index der Liste hinzu
                # wenn der threshold überschritten ist und auch der letzte gespeicherte INdex mindestens den Abstand hat

                if row["Voltage in mV"] > threshold and index - last_peaks_index > min_peak_distance:
                    list_of_index_of_peaks.append(index)
                    last_peaks_index = index
    return list_of_index_of_peaks
if __name__ == "__main__":
    # test
    df_ekg = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep = "\t", names = ["Voltage in mV", "Time in ms"])
    df_ekg = df_ekg.iloc[0:5000]
    threshold = 0.95 * df_ekg["Voltage in mV"].max()  # Set threshold to 95% of the maximum voltage
    min_peak_distance = 10
    list_of_index_of_peaks = find_peaks(df_ekg, threshold, min_peak_distance)

#%% Plot
# plot the row["Voltage in mV"] and mark the peaks with red dots
import plotly.express as plx
#make the figure wider
plx.defaults.width = 1200
fig = plx.line(df_ekg, x="Time in ms", y="Voltage in mV", title="EKG Signal with Detected Peaks")
#mark the peaks in the plot with red dots
fig.add_scatter(x=df_ekg.iloc[list_of_index_of_peaks]["Time in ms"],
                    y=df_ekg.iloc[list_of_index_of_peaks]["Voltage in mV"],
                    mode='markers',
                    marker=dict(color='red', size=10),
                    name='Peaks')
# show the figure
fig.show()